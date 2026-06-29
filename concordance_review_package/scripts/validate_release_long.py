#!/usr/bin/env python3
"""validate_release_long.py — self-contained. Structure + known-commodity-presence + CHILDREN_ONLY phải có con-EXPORT thật (GPT r7)."""
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
    # known-commodity-presence
    relset={(r['eu_code'],pad6(r['hs6'])) for _,r in rel.iterrows()}
    for _,r in cc[cc['release_policy']=='EXPORT_PRODUCT'].iterrows():
        for c in re.split(r'[;,\s]+',str(r['hs6'])):
            c=c.strip()
            if c and c.lower()!='nan' and re.fullmatch(r'\d{6}',pad6(c)) and pad6(c) in valid:
                if (r['eu_code'],pad6(c)) not in relset:
                    e.append(f"MISSING: {r['eu_code']} {r['eu_desc'][:20]} hs6 {pad6(c)} không trong release")
    # GPT r7: CHILDREN_ONLY chỉ hợp lệ nếu có con-EXPORT_PRODUCT thật (structural, không suffix)
    cc['eu7']=cc['eu_code'].astype(str).str.replace('.0','',regex=False).str.zfill(7)
    exp7=set(cc[cc['release_policy']=='EXPORT_PRODUCT']['eu7'])
    for _,r in cc[cc['release_policy']=='EXPORT_CHILDREN_ONLY'].iterrows():
        stem=r['eu7'].rstrip('0')
        kids=[x for x in exp7 if x!=r['eu7'] and x.startswith(stem) and len(x.rstrip('0'))>len(stem)]
        if not kids:
            e.append(f"NO_EXPORTED_CHILD: {r['eu_code']} {r['eu_desc'][:24]} CHILDREN_ONLY nhưng không có con EXPORT_PRODUCT")
    if e:
        print(f"FAIL ({len(e)}):"); [print("  -",x) for x in e[:25]]; return 1
    print(f"OK: release_long PASS ({len(rel)} dòng; structure + presence + children-structural đều đạt).")
    return 0
if __name__=="__main__": sys.exit(main())
