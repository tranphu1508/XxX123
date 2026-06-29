#!/usr/bin/env python3
"""build_asean_baci_panel.py — dựng analysis panel ASEAN-5 × HS6 × 52 đích × năm (balanced).
Input: BACI year CSVs (giải nén từ BACI_HS12_V202601.zip) + concordance release HS6 set.
--mode current (HS6 từ release_long hiện tại) | legacy (HS6 từ panel frozen). --years 2015-2023.
Lưu ý: cần BACI giải nén tại 01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601/."""
import argparse, pandas as pd, numpy as np, re, glob, os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; STUDY=ROOT.parents[1]
BACI=STUDY/'01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601'
ASEAN5=[360,458,608,704,764]
def pad6(s): return str(s).replace('.0','').strip().zfill(6)
ap=argparse.ArgumentParser(); ap.add_argument('--mode',default='current'); ap.add_argument('--out',default=str(ROOT/'rebuild_check'/'asean_baci_panel_rebuilt_current.csv')); a=ap.parse_args()
# HS6 set
if a.mode=='current':
    rel=pd.read_csv(ROOT/'data'/'concordance_release_long.csv',dtype=str); hs6set=set(rel['hs6'].apply(pad6))
else:
    fr=pd.read_csv(STUDY/'07_main_estimation_stata/asean_baci_panel.csv',dtype=str); hs6set=set(fr['hs6'].apply(pad6))
# 52 đích + eu_dummy lấy từ panel frozen (giữ cùng tập đích & định nghĩa EU-27 để so sánh)
fr=pd.read_csv(STUDY/'07_main_estimation_stata/asean_baci_panel.csv',dtype=str); dests=sorted(set(int(x) for x in fr['dest']))
eu_dests=set(int(x) for x in fr.loc[fr['eu'].astype(str).isin(['1','1.0']),'dest'])
yfiles=sorted(glob.glob(str(BACI/'BACI_HS12_Y20*_V202601.csv')))
if not yfiles: print("!! Chưa giải nén BACI year files. Giải nén BACI_HS12_V202601.zip trước."); raise SystemExit(2)
parts=[]
for yf in yfiles:
    y=int(re.search(r'Y(\d{4})',yf).group(1))
    if not (2015<=y<=2023): continue
    df=pd.read_csv(yf,dtype=str)
    df.columns=[c.strip() for c in df.columns]
    # BACI cols: t,i,j,k,v,q  (i=exporter,j=importer,k=hs6,v=value)
    df['i']=pd.to_numeric(df['i'],errors='coerce'); df['j']=pd.to_numeric(df['j'],errors='coerce')
    df['k6']=df['k'].apply(pad6)
    df=df[(df['i'].isin(ASEAN5)) & (df['j'].isin(dests)) & (df['k6'].isin(hs6set))]
    df['v']=pd.to_numeric(df['v'],errors='coerce')
    parts.append(df[['t','i','j','k6','v']].rename(columns={'t':'year','i':'exp','j':'dest','k6':'hs6'}))
    print(f"  Y{y}: {len(df)} dòng ASEAN-5 in-scope",flush=True)
trade=pd.concat(parts,ignore_index=True); trade['year']=pd.to_numeric(trade['year'])
# balanced panel: ASEAN5 × hs6set × dests × years
import itertools
years=sorted(trade['year'].unique())
idx=pd.DataFrame(list(itertools.product(ASEAN5,sorted(hs6set),dests,years)),columns=['exp','hs6','dest','year'])
g=trade.groupby(['exp','hs6','dest','year'],as_index=False)['v'].sum().rename(columns={'v':'value'})
panel=idx.merge(g,on=['exp','hs6','dest','year'],how='left'); panel['value']=panel['value'].fillna(0)
panel['eu']=panel['dest'].isin(eu_dests).astype(int)  # EU-27 dummy theo định nghĩa panel frozen
panel.to_csv(a.out,index=False)
print(f"[{a.mode}] BACI panel rebuilt: {len(panel)} dòng | {panel['hs6'].nunique()} HS6 | {panel['dest'].nunique()} đích | {len(years)} năm → {a.out}",flush=True)
