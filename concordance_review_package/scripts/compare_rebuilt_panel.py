#!/usr/bin/env python3
"""compare_rebuilt_panel.py --old --new --keys k1 k2 --numeric-tol --out-md --out-diff"""
import argparse, pandas as pd, numpy as np
ap=argparse.ArgumentParser()
ap.add_argument('--old',required=True); ap.add_argument('--new',required=True); ap.add_argument('--keys',nargs='+',required=True)
ap.add_argument('--numeric-tol',type=float,default=1e-8); ap.add_argument('--out-md',required=True); ap.add_argument('--out-diff',required=True)
a=ap.parse_args()
o=pd.read_csv(a.old,dtype=str).fillna(''); n=pd.read_csv(a.new,dtype=str).fillna('')
for df in (o,n):
    for k in a.keys:
        if k in df: df[k]=df[k].astype(str).str.replace('.0','',regex=False)
ok=set(map(tuple,o[a.keys].values.tolist())); nk=set(map(tuple,n[a.keys].values.tolist()))
L=['# Compare\n',f"- old: {a.old} ({len(o)} rows)\n",f"- new: {a.new} ({len(n)} rows)\n",
   f"- schema old: {list(o.columns)}\n",f"- schema new: {list(n.columns)}\n",
   f"- keys old={len(ok)} new={len(nk)} | chung={len(ok&nk)} | chỉ-old={len(ok-nk)} | chỉ-new={len(nk-ok)}\n"]
# numeric diff on common keys
common=ok&nk
numcols=[c for c in o.columns if c not in a.keys and c in n.columns]
om=o.set_index(a.keys); nm=n.set_index(a.keys)
maxdiff={}
diffrows=[]
for c in numcols:
    try:
        ov=pd.to_numeric(om.loc[list(common),c],errors='coerce'); nv=pd.to_numeric(nm.loc[list(common),c],errors='coerce')
        dd=(ov-nv).abs(); maxdiff[c]=float(dd.max()) if len(dd) else 0
    except Exception as e: maxdiff[c]=f"err {e}"
L.append(f"- max |diff| numeric: {maxdiff}\n")
open(a.out_md,'w',encoding='utf-8').writelines(L)
# diff CSV: keys only-old + only-new
import csv
with open(a.out_diff,'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(list(a.keys)+['side'])
    for k in list(ok-nk)[:5000]: w.writerow(list(k)+['only_old'])
    for k in list(nk-ok)[:5000]: w.writerow(list(k)+['only_new'])
print(open(a.out_md).read())
