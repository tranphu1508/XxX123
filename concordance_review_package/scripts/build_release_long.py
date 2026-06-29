#!/usr/bin/env python3
"""build_release_long.py — sinh concordance_release_long.csv từ concordance_final_asean.csv
theo release_policy tường minh (thay luật đuôi-0000). Per GPT round-3 spec."""
import pandas as pd, re, sys
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/"outputs"
CONC=OUT/"concordance_final_asean.csv"
HS=Path(__file__).resolve().parents[2]/"01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601/product_codes_HS12_V202601.csv"
def pad6(s): return str(s).replace('.0','').strip().zfill(6)
def main():
    cc=pd.read_csv(CONC,dtype=str).fillna('')
    valid={pad6(x) for x in pd.read_csv(HS)['code']}
    rows=[]
    for _,r in cc.iterrows():
        if r.get('release_policy','')!='EXPORT_PRODUCT': continue
        for c in re.split(r'[;,\s]+',r['hs6']):
            c=c.strip()
            if not c or c.lower()=='nan': continue
            c=pad6(c)
            if not re.fullmatch(r'\d{6}',c): continue
            rows.append({'eu_code':r['eu_code'],'eu_desc':r['eu_desc'],'hs6':c,
                         'annex1_legal_ref':r['annex1_legal_ref'],'release_policy':r['release_policy'],
                         'release_reason':r.get('release_reason','')})
    rel=pd.DataFrame(rows).drop_duplicates(['eu_code','hs6'])
    bad=set(rel['hs6'])-valid
    if bad: print("WARN HS6 ngoài HS2012:",bad)
    rel.to_csv(OUT/"concordance_release_long.csv",index=False)
    print(f"release_long: {len(rel)} dòng | {rel['eu_code'].nunique()} EU | {rel['hs6'].nunique()} HS6 distinct")
    return 0
if __name__=="__main__": sys.exit(main())
