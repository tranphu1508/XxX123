#!/usr/bin/env python3
"""build_asean_mrl_panel.py — dựng MRL stringency panel (HS6×year, weakest-link).
Logic: map binding-panel EU product_code → HS6 (concordance) → min MRL across substances×products → stringency=-ln(min).
Modes: --mode current (concordance hiện tại) | legacy (backup pre-fix). --out path."""
import argparse, pandas as pd, numpy as np, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STUDY=ROOT.parents[1]
def pad6(s): return str(s).replace('.0','').strip().zfill(6)
def norm_eu(s): return str(s).replace('.0','').strip().lstrip('0')
ap=argparse.ArgumentParser(); ap.add_argument('--mode',default='current'); ap.add_argument('--out',default=str(ROOT/'rebuild_check'/'asean_mrl_panel_rebuilt_current.csv')); a=ap.parse_args()
conc = ROOT/'data'/'concordance_final_asean.csv' if a.mode=='current' else (STUDY/'03_concordance_product_code_to_harmonized_system_six_digit/outputs/concordance_final_asean_pre_hsfix_2026-06-29.csv')
cc=pd.read_csv(conc,dtype=str).fillna('')
# eu_code → list HS6 (explode multi-code)
m={}
for _,r in cc.iterrows():
    codes=[pad6(c) for c in re.findall(r'\d{6}',str(r['hs6']))]
    if codes: m[norm_eu(r['eu_code'])]=codes
b=pd.read_csv(STUDY/'04_maximum_residue_level_panel/outputs/eu_mrl_binding_panel_reference_jan01_2026-06-26.csv',dtype=str,low_memory=False)
b['euN']=b['product_code'].apply(norm_eu); b['mrl']=pd.to_numeric(b['mrl_mg_kg'],errors='coerce'); b['year']=pd.to_numeric(b['year'],errors='coerce')
b=b[(b['year']>=2015)&(b['year']<=2023)].dropna(subset=['mrl'])
rows=[]
for _,r in b.iterrows():
    for h in m.get(r['euN'],[]):
        rows.append((h,int(r['year']),r['euN'],r['mrl']))
d=pd.DataFrame(rows,columns=['hs6','year','eu','mrl'])
g=d.groupby(['hs6','year']).agg(n_eu_codes=('eu','nunique'),min_mrl_weakest=('mrl','min')).reset_index()
g['lumped']=(g['n_eu_codes']>1).astype(int)
g['stringency']=(-np.log(g['min_mrl_weakest'])).round(4)
g=g.sort_values(['hs6','year'])
Path(a.out).parent.mkdir(parents=True,exist_ok=True); g.to_csv(a.out,index=False)
print(f"[{a.mode}] MRL panel rebuilt: {len(g)} dòng | {g['hs6'].nunique()} HS6 | years {g['year'].min()}-{g['year'].max()} → {a.out}")
