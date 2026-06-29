#!/usr/bin/env python3
"""compare_rebuilt_panel.py -- audit-grade compare giua hai panel CSV (old vs new).

Checks (Round 011):
  1 schema equality        6 numeric: max-abs / max-rel / mean-abs / count-over-tol
  2 row count              7 categorical column mismatch counts
  3 key uniqueness         8 NA/blank mismatch counts
  4 duplicate-key sample   9 sorted-normalized checksum (old_sha256, new_sha256)
  5 key coverage          10 optional value-sum check (trade panel)

Output: --out-md + --out-diff (CSV) + --out-json (machine-readable).

Vi du:
  python compare_rebuilt_panel.py --old <old.csv> --new <new.csv> \
      --keys exp hs6 dest year --numeric-tol 1e-8 \
      --out-md compare.md --out-diff diff.csv --out-json compare.json
"""
import argparse, csv, json, hashlib
import pandas as pd, numpy as np

def norm_key_series(s):
    return s.astype(str).str.replace('.0','',regex=False).str.strip()

def is_numeric_col(series):
    v = pd.to_numeric(series, errors='coerce')
    nonblank = series.astype(str).str.strip().replace('', np.nan).notna()
    if nonblank.sum() == 0: return False
    return (v.notna().sum() / max(nonblank.sum(),1)) >= 0.95

def sorted_norm_sha256(df, keys, numcols, ndigits=6):
    d = df.copy()
    for c in numcols:
        d[c] = pd.to_numeric(d[c], errors='coerce').round(ndigits)
    d = d[sorted(d.columns)]
    sk = [k for k in keys if k in d.columns]
    if sk: d = d.sort_values(sk, kind='mergesort').reset_index(drop=True)
    return hashlib.sha256(d.to_csv(index=False).encode('utf-8')).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--old', required=True); ap.add_argument('--new', required=True)
    ap.add_argument('--keys', nargs='+', required=True)
    ap.add_argument('--numeric-tol', type=float, default=1e-8)
    ap.add_argument('--value-col', default='value')
    ap.add_argument('--out-md', required=True); ap.add_argument('--out-diff', required=True)
    ap.add_argument('--out-json', required=True)
    a = ap.parse_args()

    o = pd.read_csv(a.old, dtype=str).fillna(''); n = pd.read_csv(a.new, dtype=str).fillna('')
    for df in (o, n):
        for k in a.keys:
            if k in df: df[k] = norm_key_series(df[k])

    R = {'old_file': a.old, 'new_file': a.new, 'keys': a.keys, 'numeric_tol': a.numeric_tol}
    R['schema_old'] = list(o.columns); R['schema_new'] = list(n.columns)
    R['schema_equal'] = list(o.columns) == list(n.columns)
    R['cols_only_old'] = [c for c in o.columns if c not in n.columns]
    R['cols_only_new'] = [c for c in n.columns if c not in o.columns]
    R['rows_old'] = len(o); R['rows_new'] = len(n)

    ot = o[a.keys].apply(tuple, axis=1); nt = n[a.keys].apply(tuple, axis=1)
    R['dup_keys_old'] = int(ot.duplicated().sum()); R['dup_keys_new'] = int(nt.duplicated().sum())
    R['key_unique_old'] = R['dup_keys_old'] == 0; R['key_unique_new'] = R['dup_keys_new'] == 0
    dup_sample = []
    for side, t in (('old', ot), ('new', nt)):
        for k in list(t[t.duplicated()].unique())[:25]:
            dup_sample.append({'side': side, **{kk: vv for kk, vv in zip(a.keys, k)}})

    ok = set(ot); nk = set(nt); common = ok & nk
    R['keys_old'] = len(ok); R['keys_new'] = len(nk)
    R['only_old'] = len(ok - nk); R['only_new'] = len(nk - ok); R['common'] = len(common)

    om = o.drop_duplicates(a.keys).set_index(a.keys); nm = n.drop_duplicates(a.keys).set_index(a.keys)
    common_list = list(common)
    shared = [c for c in o.columns if c not in a.keys and c in n.columns]
    numcols = [c for c in shared if is_numeric_col(o[c]) and is_numeric_col(n[c])]
    catcols = [c for c in shared if c not in numcols]
    R['numeric_cols'] = numcols; R['categorical_cols'] = catcols
    numeric_report = {}; cat_report = {}; na_report = {}
    if common_list:
        oc = om.loc[common_list]; nc = nm.loc[common_list]
        for c in numcols:
            ov = pd.to_numeric(oc[c], errors='coerce'); nv = pd.to_numeric(nc[c], errors='coerce')
            dd = (ov - nv).abs(); rel = dd / ov.abs().replace(0, np.nan)
            numeric_report[c] = {
                'max_abs_diff': float(np.nanmax(dd)) if len(dd) else 0.0,
                'max_rel_diff': float(np.nanmax(rel)) if rel.notna().any() else 0.0,
                'mean_abs_diff': float(np.nanmean(dd)) if len(dd) else 0.0,
                'count_over_tol': int((dd > a.numeric_tol).sum())}
            na_report[c] = {'na_mismatch': int((ov.isna() != nv.isna()).sum())}
        for c in catcols:
            mm = (oc[c].astype(str) != nc[c].astype(str))
            cat_report[c] = {'mismatch': int(mm.sum())}
            na_report[c] = {'blank_mismatch': int((oc[c].astype(str).eq('')).ne(nc[c].astype(str).eq('')).sum())}
    R['numeric'] = numeric_report; R['categorical'] = cat_report; R['na'] = na_report

    R['old_sha256'] = sorted_norm_sha256(o, a.keys, numcols)
    R['new_sha256'] = sorted_norm_sha256(n, a.keys, numcols)
    R['checksum_equal'] = R['old_sha256'] == R['new_sha256']

    if a.value_col in numcols:
        R['value_sum_old'] = float(pd.to_numeric(o[a.value_col], errors='coerce').sum())
        R['value_sum_new'] = float(pd.to_numeric(n[a.value_col], errors='coerce').sum())
        R['value_sum_diff'] = R['value_sum_new'] - R['value_sum_old']

    with open(a.out_json, 'w', encoding='utf-8') as f:
        json.dump(R, f, ensure_ascii=False, indent=2)
    with open(a.out_diff, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(list(a.keys) + ['side'])
        for k in list(ok - nk)[:5000]: w.writerow(list(k) + ['only_old'])
        for k in list(nk - ok)[:5000]: w.writerow(list(k) + ['only_new'])
        for d in dup_sample: w.writerow([d.get(kk, '') for kk in a.keys] + ['dup_' + d['side']])

    exact = (R['schema_equal'] and R['rows_old']==R['rows_new'] and R['only_old']==0 and R['only_new']==0
             and all(v['count_over_tol']==0 for v in numeric_report.values())
             and all(v['mismatch']==0 for v in cat_report.values()))
    L = []
    L.append(f"# Compare panel -- {a.old}  vs  {a.new}\n\n")
    L.append(f"**Verdict:** {'EXACT (0-diff)' if exact else 'DIFFERENCES (xem chi tiet + diagnosis)'}\n\n")
    L.append(f"- schema_equal={R['schema_equal']} | cols_only_old={R['cols_only_old']} | cols_only_new={R['cols_only_new']}\n")
    L.append(f"- rows old={R['rows_old']} new={R['rows_new']}\n")
    L.append(f"- key uniqueness: old unique={R['key_unique_old']} (dup={R['dup_keys_old']}) | new unique={R['key_unique_new']} (dup={R['dup_keys_new']})\n")
    L.append(f"- key coverage: common={R['common']} | only_old={R['only_old']} | only_new={R['only_new']}\n")
    L.append(f"- sorted-normalized checksum: equal={R['checksum_equal']}\n    - old_sha256={R['old_sha256']}\n    - new_sha256={R['new_sha256']}\n")
    if 'value_sum_old' in R:
        L.append(f"- value-sum: old={R['value_sum_old']:.0f} new={R['value_sum_new']:.0f} diff={R['value_sum_diff']:.0f}\n")
    L.append("\n## Numeric columns (tren common keys)\n\n| col | max_abs | max_rel | mean_abs | #>tol |\n|---|---|---|---|---|\n")
    for c, v in numeric_report.items():
        L.append(f"| {c} | {v['max_abs_diff']:.6g} | {v['max_rel_diff']:.6g} | {v['mean_abs_diff']:.6g} | {v['count_over_tol']} |\n")
    if cat_report:
        L.append("\n## Categorical mismatch\n\n| col | #mismatch |\n|---|---|\n")
        for c, v in cat_report.items(): L.append(f"| {c} | {v['mismatch']} |\n")
    L.append(f"\n_diff keys -> {a.out_diff} ; machine-readable -> {a.out_json}_\n")
    with open(a.out_md, 'w', encoding='utf-8') as f: f.writelines(L)
    print(''.join(L))

if __name__ == '__main__':
    main()
