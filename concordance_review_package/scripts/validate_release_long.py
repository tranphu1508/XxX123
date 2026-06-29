#!/usr/bin/env python3
"""validate_release_long.py — self-contained. Check cấu trúc + known-commodity-presence (GPT r4)."""
import pandas as pd, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def pad6(s): return str(s).replace('.0','').strip().zfill(6)
def main():
    rel=pd.read_csv(ROOT/"data"/"concordance_release_long.csv",dtype=str).fillna('')
    cc=pd.read_csv(ROOT/"data"/"concordance_final_asean.csv",dtype=str).fillna('')
    valid={pad6(x) for x in pd.read_csv(ROOT/"sources"/"product_codes_HS12_V202601.csv")['code']}
    e=[]
    for i,r in rel.iterrows():
        h=r['hs6']
        if not h or h.lower()=='nan': e.append(f"row {i}: hs6 trống")
        elif not re.fullmatch(r'\d{6}',pad6(h)): e.append(f"row {i}: hs6 không 6 số: {h}")
        elif pad6(h) not in valid: e.append(f"row {i}: hs6 ngoài HS2012: {h}")
        if ';' in str(h): e.append(f"row {i}: còn ';'")
    if rel.duplicated(['eu_code','hs6']).sum(): e.append("có cặp eu_code-hs6 trùng")
    # known-commodity-presence: mọi EXPORT_PRODUCT+hs6 trong source phải có mặt trong release
    relset={(r['eu_code'],pad6(r['hs6'])) for _,r in rel.iterrows()}
    for _,r in cc[cc['release_policy']=='EXPORT_PRODUCT'].iterrows():
        for c in re.split(r'[;,\s]+',str(r['hs6'])):
            c=c.strip()
            if c and c.lower()!='nan' and re.fullmatch(r'\d{6}',pad6(c)) and pad6(c) in valid:
                if (r['eu_code'],pad6(c)) not in relset:
                    e.append(f"MISSING: {r['eu_code']} {r['eu_desc'][:20]} hs6 {pad6(c)} không có trong release_long")
    if e:
        print(f"FAIL ({len(e)}):"); [print("  -",x) for x in e[:25]]; return 1
    print(f"OK: release_long PASS ({len(rel)} dòng; cấu trúc + known-commodity-presence đều đạt).")
    return 0
if __name__=="__main__": sys.exit(main())
