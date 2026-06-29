#!/usr/bin/env python3
"""build_release_long.py — self-contained trong concordance_review_package.
Đọc data/concordance_final_asean.csv (+ release_policy), sinh data/concordance_release_long.csv.
Chạy: python concordance_review_package/scripts/build_release_long.py"""
import pandas as pd, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"concordance_final_asean.csv"
HS=ROOT/"sources"/"product_codes_HS12_V202601.csv"
OUT=ROOT/"data"/"concordance_release_long.csv"
def pad6(s): return str(s).replace('.0','').strip().zfill(6)
def main():
    cc=pd.read_csv(DATA,dtype=str).fillna('')
    valid={pad6(x) for x in pd.read_csv(HS)['code']}
    rows=[]
    for _,r in cc.iterrows():
        if r.get('release_policy','')!='EXPORT_PRODUCT': continue
        for c in re.split(r'[;,\s]+',r['hs6']):
            c=c.strip()
            if not c or c.lower()=='nan': continue
            c=pad6(c)
            if re.fullmatch(r'\d{6}',c) and c in valid:
                rows.append({'eu_code':r['eu_code'],'eu_desc':r['eu_desc'],'hs6':c,
                             'annex1_legal_ref':r['annex1_legal_ref'],'release_policy':r['release_policy'],
                             'release_reason':r.get('release_reason','')})
    rel=pd.DataFrame(rows).drop_duplicates(['eu_code','hs6'])
    rel.to_csv(OUT,index=False)
    print(f"release_long: {len(rel)} dòng | {rel['eu_code'].nunique()} EU | {rel['hs6'].nunique()} HS6 distinct")
    return 0
if __name__=="__main__": sys.exit(main())
