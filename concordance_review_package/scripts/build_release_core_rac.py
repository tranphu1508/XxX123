"""build_release_core_rac.py — ROBUSTNESS release CORE_RAC_ONLY.
ĐỊNH NGHĨA (GPT r8): Option A — STRICT RAW/PRIMARY form, 1 HS6/commodity.
= token HS6 ĐẦU của mỗi EXPORT_PRODUCT, với thứ tự hs6 đã curate RAC/commodity-first
  (in-shell/whole/fresh/grain trước; seed-for-sowing & processed sau).
Lưu ý: rice=100610 (paddy, thô nhất) theo định nghĩa strict-raw; nếu muốn binding-trade-RAC
  (milled 100630 theo Nguyen 2026) thì build variant riêng. So main coverage = trade-coverage.
"""
import pandas as pd, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def pad6(s): return str(s).replace('.0','').strip().zfill(6)
def main():
    cc=pd.read_csv(ROOT/"data"/"concordance_final_asean.csv",dtype=str).fillna('')
    valid={pad6(x) for x in pd.read_csv(ROOT/"sources"/"product_codes_HS12_V202601.csv")['code']}
    rows=[]
    for _,r in cc.iterrows():
        if r.get('release_policy','')!='EXPORT_PRODUCT': continue
        toks=[pad6(c) for c in re.split(r'[;,\s]+',r['hs6']) if re.fullmatch(r'\d{6}',pad6(c)) and pad6(c) in valid]
        if toks:
            rows.append({'eu_code':r['eu_code'],'eu_desc':r['eu_desc'],'hs6':toks[0],
                         'annex1_legal_ref':r['annex1_legal_ref'],'release_variant':'CORE_RAC_ONLY'})
    rel=pd.DataFrame(rows).drop_duplicates(['eu_code','hs6'])
    rel.to_csv(ROOT/"data"/"concordance_release_core_rac.csv",index=False)
    print(f"CORE_RAC release: {len(rel)} dòng (1 RAC-HS6/commodity)")
    return 0
if __name__=="__main__": sys.exit(main())
