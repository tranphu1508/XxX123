#!/usr/bin/env python3
"""validate_release_long.py — kiểm release_long theo acceptance criteria GPT round-3."""
import pandas as pd, re, sys
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/"outputs"
HS=Path(__file__).resolve().parents[2]/"01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601/product_codes_HS12_V202601.csv"
def pad6(s): return str(s).replace('.0','').strip().zfill(6)
def main():
    rel=pd.read_csv(OUT/"concordance_release_long.csv",dtype=str).fillna('')
    valid={pad6(x) for x in pd.read_csv(HS)['code']}
    e=[]
    for i,r in rel.iterrows():
        h=r['hs6']
        if not h or h.lower()=='nan': e.append(f"row {i}: hs6 trống/nan")
        elif not re.fullmatch(r'\d{6}',h): e.append(f"row {i}: hs6 không 6 số: {h}")
        elif h not in valid: e.append(f"row {i}: hs6 ngoài HS2012: {h}")
        if ';' in h: e.append(f"row {i}: còn ';' trong hs6")
    dup=rel.duplicated(['eu_code','hs6']).sum()
    if dup: e.append(f"{dup} cặp eu_code-hs6 trùng")
    if e:
        print("FAIL:"); [print("  -",x) for x in e[:20]]; return 1
    print(f"OK: release_long PASS ({len(rel)} dòng, mọi HS6 ∈ HS2012, không ';', không trùng).")
    return 0
if __name__=="__main__": sys.exit(main())
