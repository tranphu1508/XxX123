#!/usr/bin/env python3
"""build_asean_baci_panel.py -- dung analysis panel ASEAN-5 x HS6 x 52 dich x nam (balanced).

Input: BACI year CSVs (giai nen tu BACI_HS12_V202601.zip) + concordance release HS6 set
+ frozen panel (lay tap dich 52 nuoc & dinh nghia EU-27 dummy de so sanh dong nhat).
BACI cols: t,i,j,k,v,q  (i=exporter, j=importer, k=hs6, v=value).

--mode current : HS6 universe = concordance_release_long.csv (corrected coverage)
--mode legacy  : HS6 universe = frozen panel (tai lap exact frozen)

Portable (Round 011): moi input co CLI arg; in resolved paths.

Vi du:
  python build_asean_baci_panel.py --mode legacy \
      --baci-dir 01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601 \
      --frozen-panel 07_main_estimation_stata/asean_baci_panel.csv \
      --release-long concordance_review_package/data/concordance_release_long.csv \
      --year-min 2015 --year-max 2023 \
      --out concordance_review_package/rebuild_check/asean_baci_panel_rebuilt_legacy.csv
"""
import argparse, re, glob, itertools
from pathlib import Path
import pandas as pd, numpy as np

ROOT  = Path(__file__).resolve().parents[1]
STUDY = ROOT.parents[1]
ASEAN5 = [360, 458, 608, 704, 764]

DEF_BACI   = STUDY/'01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601'
DEF_FROZEN = STUDY/'07_main_estimation_stata/asean_baci_panel.csv'
DEF_REL    = ROOT/'data'/'concordance_release_long.csv'
DEF_OUT    = ROOT/'rebuild_check'/'asean_baci_panel_rebuilt_current.csv'

def pad6(s): return str(s).replace('.0','').strip().zfill(6)

def main():
    ap = argparse.ArgumentParser(description="Build balanced ASEAN-5 BACI analysis panel.")
    ap.add_argument('--mode', choices=['current','legacy'], default='current')
    ap.add_argument('--baci-dir', default=None)
    ap.add_argument('--frozen-panel', default=None)
    ap.add_argument('--release-long', default=None)
    ap.add_argument('--year-min', type=int, default=2015)
    ap.add_argument('--year-max', type=int, default=2023)
    ap.add_argument('--out', default=None)
    a = ap.parse_args()

    baci   = Path(a.baci_dir) if a.baci_dir else DEF_BACI
    frozen = Path(a.frozen_panel) if a.frozen_panel else DEF_FROZEN
    rel    = Path(a.release_long) if a.release_long else DEF_REL
    out    = Path(a.out) if a.out else DEF_OUT

    print(f"USING mode={a.mode}")
    print(f"USING baci_dir={baci}")
    print(f"USING frozen_panel={frozen}")
    print(f"USING release_long={rel}")
    print(f"USING year_window={a.year_min}-{a.year_max}")
    print(f"USING output={out}")

    if not frozen.exists(): raise SystemExit(f"!! khong tim thay frozen panel: {frozen}")
    fr = pd.read_csv(frozen, dtype=str)
    dests    = sorted(set(int(x) for x in fr['dest']))
    eu_dests = set(int(x) for x in fr.loc[fr['eu'].astype(str).isin(['1','1.0']), 'dest'])

    if a.mode == 'current':
        if not rel.exists(): raise SystemExit(f"!! khong tim thay release_long: {rel}")
        hs6set = set(pd.read_csv(rel, dtype=str)['hs6'].apply(pad6))
    else:
        hs6set = set(fr['hs6'].apply(pad6))
    print(f"  HS6 universe ({a.mode}) = {len(hs6set)} | dich = {len(dests)} | EU-27 dummy = {len(eu_dests)} nuoc")

    yfiles = sorted(glob.glob(str(baci/'BACI_HS12_Y20*_V202601.csv')))
    if not yfiles:
        raise SystemExit(f"!! Chua giai nen BACI year files trong {baci}. Giai nen BACI_HS12_V202601.zip truoc (xem reviews/raw_download_manual_steps.md).")
    parts = []
    for yf in yfiles:
        y = int(re.search(r'Y(\d{4})', yf).group(1))
        if not (a.year_min <= y <= a.year_max): continue
        df = pd.read_csv(yf, dtype=str); df.columns = [c.strip() for c in df.columns]
        df['i'] = pd.to_numeric(df['i'], errors='coerce'); df['j'] = pd.to_numeric(df['j'], errors='coerce')
        df['k6'] = df['k'].apply(pad6)
        df = df[(df['i'].isin(ASEAN5)) & (df['j'].isin(dests)) & (df['k6'].isin(hs6set))]
        df['v'] = pd.to_numeric(df['v'], errors='coerce')
        parts.append(df[['t','i','j','k6','v']].rename(columns={'t':'year','i':'exp','j':'dest','k6':'hs6'}))
        print(f"  Y{y}: {len(df)} dong ASEAN-5 in-scope", flush=True)
    trade = pd.concat(parts, ignore_index=True); trade['year'] = pd.to_numeric(trade['year'])

    years = list(range(a.year_min, a.year_max+1))
    idx = pd.DataFrame(list(itertools.product(ASEAN5, sorted(hs6set), dests, years)),
                       columns=['exp','hs6','dest','year'])
    g = trade.groupby(['exp','hs6','dest','year'], as_index=False)['v'].sum().rename(columns={'v':'value'})
    panel = idx.merge(g, on=['exp','hs6','dest','year'], how='left')
    panel['value'] = panel['value'].fillna(0.0)
    panel['eu'] = panel['dest'].isin(eu_dests).astype(int)

    out.parent.mkdir(parents=True, exist_ok=True)
    panel.to_csv(out, index=False)
    print(f"[{a.mode}] BACI panel rebuilt: {len(panel)} dong | {panel['hs6'].nunique()} HS6 | {panel['dest'].nunique()} dich | {len(years)} nam -> {out}")

if __name__ == '__main__':
    main()
