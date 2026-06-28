#!/usr/bin/env python3
import pandas as pd, numpy as np, time
import pyfixest as pf
BASE="/sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports"
STUDY=BASE+"/eu_maximum_residue_level_asean_export_study"
def pad6(series):
    s=pd.Series(series).astype(str).str.replace(r'\.0$','',regex=True).str.strip()
    return s.str.zfill(6)
print("LOAD",flush=True)
old=pd.read_csv(BASE+"/Version 2/Model Run/regression_panel_FINAL.csv",dtype={'k':str},low_memory=False)
old['k6']=pad6(old['k'])
old=old.dropna(subset=['v','treatment_M1']).copy()
old['v']=old['v'].clip(lower=0)
for col,grp in [('ikt',['i','k6','t']),('jt',['j','t']),('ijk',['i','j','k6']),('jj',['j']),('tt',['t']),('clustij',['i','j'])]:
    old[col]=old.groupby(grp).ngroup()
print("rows:",len(old),"HS6:",old['k6'].nunique(),"exp:",old['i'].nunique(),"dest:",old['j'].nunique(),"yrs:",sorted(old['t'].unique()),flush=True)
nb=pd.read_csv(STUDY+"/07_main_estimation_stata/asean_baci_panel.csv",low_memory=False)
clean_baci=set(pad6(nb['hs6'].unique()))
mp=pd.read_csv(STUDY+"/04_maximum_residue_level_panel/outputs/asean_mrl_panel.csv",low_memory=False)
clean_mrl=set(pad6(mp['hs6'].unique()))
oc=set(old['k6'].unique())
kept_baci=oc&clean_baci; drop_baci=oc-clean_baci; kept_mrl=oc&clean_mrl
print(f"OLD={len(oc)} kept_baci={len(kept_baci)} dropped={len(drop_baci)} | kept_mrl={len(kept_mrl)} dropped={len(oc-clean_mrl)}",flush=True)
samples={'FULL_185':old,'KEPT_baci':old[old['k6'].isin(kept_baci)],'DROPPED_baci':old[old['k6'].isin(drop_baci)],'KEPT_mrl':old[old['k6'].isin(kept_mrl)]}
specs={'S1_pref(ikt+jt)':"v ~ treatment_M1 | ikt + jt",'S3_min(ikt+j+t)':"v ~ treatment_M1 | ikt + jj + tt",'S2_cons(ikt+jt+ijk)':"v ~ treatment_M1 | ikt + jt + ijk"}
rows=[]
for sname,sdf in samples.items():
    print("\n#### SAMPLE",sname,"rows=",len(sdf),"HS6=",sdf['k6'].nunique(),flush=True)
    for spname,fml in specs.items():
        t0=time.time()
        try:
            m=pf.fepois(fml,data=sdf,vcov={"CRV1":"clustij"})
            b=m.coef()['treatment_M1']; se=m.se()['treatment_M1']; p=m.pvalue()['treatment_M1']; n=int(m._N)
            star='***' if p<0.01 else '**' if p<0.05 else '*' if p<0.10 else ''
            print(f"  [{spname:22}] beta={b:+8.4f} SE={se:.4f} z={b/se:+6.2f} p={p:.4f}{star} N={n} ({time.time()-t0:.0f}s)",flush=True)
            rows.append(dict(sample=sname,spec=spname,beta=round(b,4),se=round(se,4),z=round(b/se,2),p=round(p,4),N=n,nHS6=sdf['k6'].nunique()))
        except Exception as e:
            print(f"  [{spname:22}] ERROR: {repr(e)[:140]}",flush=True)
            rows.append(dict(sample=sname,spec=spname,beta=None,se=None,z=None,p=None,N=None,nHS6=sdf['k6'].nunique()))
res=pd.DataFrame(rows)
res.to_csv("/sessions/modest-dazzling-tesla/mnt/outputs/samesample_results.csv",index=False)
print("\n==== SUMMARY ===="); print(res.to_string(index=False)); print("\nDONE",flush=True)
