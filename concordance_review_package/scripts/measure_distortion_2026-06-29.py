import pandas as pd, numpy as np, time
import pyfixest as pf
STUDY="/sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study"
def pad6(s): return pd.Series(s).astype(str).str.replace(r'\.0$','',regex=True).str.strip().str.zfill(6)
print("LOAD",flush=True)
nb=pd.read_csv(STUDY+"/07_main_estimation_stata/asean_baci_panel.csv",low_memory=False)
nb['h6']=pad6(nb['hs6'])
mp=pd.read_csv(STUDY+"/04_maximum_residue_level_panel/outputs/asean_mrl_panel.csv",low_memory=False)
mp['h6']=pad6(mp['hs6'])
nb=nb.merge(mp[['h6','year','stringency']],on=['h6','year'],how='left')
print("merge stringency: matched",nb['stringency'].notna().mean()*100,"%",flush=True)
nb['treatment']=nb['stringency'].fillna(0)*nb['eu']
nb['value']=nb['value'].clip(lower=0)
for col,grp in [('fe_ikt',['exp','h6','year']),('fe_jt',['dest','year']),('fe_ijk',['exp','dest','h6']),('cl',['exp','dest'])]:
    nb[col]=nb.groupby(grp).ngroup()
# suspect set
cl=pd.read_csv(STUDY+"/12_audit/concordance_full_review_classified_2026-06-29.csv")
cl['h']=pad6(cl['h'])
suspect=set(cl[cl['cls'].isin(['ERROR','LUMPING']) & (cl['inpanel']==True)]['h'])
suspect |= {'520100','080390','071410','080112','120740','120730','120721','120750','080232','071120','070992'}
suspect &= set(nb['h6'].unique())
print(f"\nSuspect HS6 trong panel: {len(suspect)} mã | dòng panel dính: {nb['h6'].isin(suspect).sum()} / {len(nb)} ({100*nb['h6'].isin(suspect).sum()/len(nb):.1f}%)",flush=True)
specs={'S1(ikt+jt)':"value ~ treatment | fe_ikt + fe_jt",'S2(ikt+jt+ijk)':"value ~ treatment | fe_ikt + fe_jt + fe_ijk"}
def run(df,lbl):
    print(f"\n#### {lbl}: {len(df)} dòng, {df['h6'].nunique()} HS6",flush=True)
    for sn,fml in specs.items():
        t0=time.time()
        try:
            m=pf.fepois(fml,data=df,vcov={"CRV1":"cl"})
            b=m.coef()['treatment'];se=m.se()['treatment'];p=m.pvalue()['treatment']
            st='***' if p<.01 else '**' if p<.05 else '*' if p<.1 else ''
            print(f"   [{sn:16}] beta={b:+.4f} SE={se:.4f} p={p:.4f}{st} N={int(m._N)} ({time.time()-t0:.0f}s)",flush=True)
        except Exception as e:
            print(f"   [{sn:16}] ERR {repr(e)[:80]}",flush=True)
run(nb,"BASELINE (toàn 125 mã)")
run(nb[~nb['h6'].isin(suspect)],"LOẠI mã lỗi+lumping")
print("\nDONE",flush=True)
