#!/usr/bin/env python3
"""validate_release_core_rac.py — CORE_RAC robustness: 1 HS6/commodity, hợp lệ HS2012, không trùng."""
import pandas as pd, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def pad6(s): return str(s).replace('.0','').strip().zfill(6)
def main():
    r=pd.read_csv(ROOT/"data"/"concordance_release_core_rac.csv",dtype=str).fillna('')
    valid={pad6(x) for x in pd.read_csv(ROOT/"sources"/"product_codes_HS12_V202601.csv")['code']}
    e=[]
    for i,row in r.iterrows():
        if not re.fullmatch(r'\d{6}',pad6(row['hs6'])): e.append(f"row {i}: hs6 không 6 số")
        elif pad6(row['hs6']) not in valid: e.append(f"row {i}: hs6 ngoài HS2012: {row['hs6']}")
    dup=r.groupby('eu_code').size()
    multi=dup[dup>1]
    if len(multi): e.append(f"{len(multi)} commodity có >1 HS6 (CORE_RAC phải 1/commodity): {list(multi.index)[:5]}")
    if e:
        print(f"FAIL ({len(e)}):"); [print("  -",x) for x in e[:20]]; return 1
    print(f"OK: CORE_RAC PASS ({len(r)} dòng, 1 RAC-HS6/commodity, mọi HS6 ∈ HS2012).")
    return 0
if __name__=="__main__": sys.exit(main())
