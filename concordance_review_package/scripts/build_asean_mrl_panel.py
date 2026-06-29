#!/usr/bin/env python3
"""build_asean_mrl_panel.py -- dung MRL stringency panel (HS6 x year, weakest-link).

Logic: map binding-panel EU product_code -> HS6 (concordance) -> min MRL across
substances x products mapped to that HS6 -> stringency = -ln(min_mrl).

Portable (Round 011): moi input co CLI arg; default theo layout du an; in resolved paths.

Vi du:
  python build_asean_mrl_panel.py --mode current \
      --concordance concordance_review_package/data/concordance_final_asean.csv \
      --binding-panel 04_maximum_residue_level_panel/outputs/eu_mrl_binding_panel_reference_jan01_2026-06-26.csv \
      --year-min 2015 --year-max 2023 \
      --out concordance_review_package/rebuild_check/asean_mrl_panel_rebuilt_current.csv
"""
import argparse, re
from pathlib import Path
import pandas as pd, numpy as np

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT.parents[1]

DEF_CONC   = ROOT/'data'/'concordance_final_asean.csv'
DEF_LEGACY = STUDY/'03_concordance_product_code_to_harmonized_system_six_digit/outputs/concordance_final_asean_pre_hsfix_2026-06-29.csv'
DEF_BIND   = STUDY/'04_maximum_residue_level_panel/outputs/eu_mrl_binding_panel_reference_jan01_2026-06-26.csv'
DEF_OUT    = ROOT/'rebuild_check'/'asean_mrl_panel_rebuilt_current.csv'

def pad6(s):    return str(s).replace('.0','').strip().zfill(6)
def norm_eu(s): return str(s).replace('.0','').strip().lstrip('0')

def main():
    ap = argparse.ArgumentParser(description="Build ASEAN MRL weakest-link stringency panel.")
    ap.add_argument('--mode', choices=['current','legacy'], default='current')
    ap.add_argument('--concordance', default=None)
    ap.add_argument('--legacy-concordance', default=None)
    ap.add_argument('--binding-panel', default=None)
    ap.add_argument('--year-min', type=int, default=2015)
    ap.add_argument('--year-max', type=int, default=2023)
    ap.add_argument('--out', default=None)
    a = ap.parse_args()

    conc = Path(a.concordance) if a.concordance else (DEF_CONC if a.mode=='current' else (Path(a.legacy_concordance) if a.legacy_concordance else DEF_LEGACY))
    bind = Path(a.binding_panel) if a.binding_panel else DEF_BIND
    out  = Path(a.out) if a.out else DEF_OUT

    print(f"USING mode={a.mode}")
    print(f"USING concordance={conc}")
    print(f"USING binding_panel={bind}")
    print(f"USING year_window={a.year_min}-{a.year_max}")
    print(f"USING output={out}")
    for p in (conc, bind):
        if not p.exists(): raise SystemExit(f"!! khong tim thay input: {p}")

    cc = pd.read_csv(conc, dtype=str).fillna('')
    m = {}
    for _, r in cc.iterrows():
        codes = [pad6(c) for c in re.findall(r'\d{6}', str(r['hs6']))]
        if codes: m[norm_eu(r['eu_code'])] = codes

    b = pd.read_csv(bind, dtype=str, low_memory=False)
    b['euN']  = b['product_code'].apply(norm_eu)
    b['mrl']  = pd.to_numeric(b['mrl_mg_kg'], errors='coerce')
    b['year'] = pd.to_numeric(b['year'], errors='coerce')
    b = b[(b['year'] >= a.year_min) & (b['year'] <= a.year_max)].dropna(subset=['mrl'])

    rows = []
    for _, r in b.iterrows():
        for h in m.get(r['euN'], []):
            rows.append((h, int(r['year']), r['euN'], r['mrl']))
    d = pd.DataFrame(rows, columns=['hs6','year','eu','mrl'])
    g = d.groupby(['hs6','year']).agg(n_eu_codes=('eu','nunique'), min_mrl_weakest=('mrl','min')).reset_index()
    g['lumped']     = (g['n_eu_codes'] > 1).astype(int)
    g['stringency'] = (-np.log(g['min_mrl_weakest'])).round(4)
    g = g.sort_values(['hs6','year'])

    out.parent.mkdir(parents=True, exist_ok=True)
    g.to_csv(out, index=False)
    print(f"[{a.mode}] MRL panel rebuilt: {len(g)} dong | {g['hs6'].nunique()} HS6 | years {int(g['year'].min())}-{int(g['year'].max())} -> {out}")

if __name__ == '__main__':
    main()
