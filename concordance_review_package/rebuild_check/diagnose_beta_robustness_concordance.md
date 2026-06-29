# Does the corrected concordance change the headline β? — clean decomposition (Round 010)

**Question.** After ~80 concordance fixes across 9 review rounds, does the corrected stringency overturn the published result (continuous-stringency PPML, S1 = −1.47***)?

**Design.** Hold the BACI panel, the treatment construction (`treatment = stringency × eu`), the fixed effects, the cluster, and the year window **identical**. Vary only the **stringency source** (old frozen MRL panel vs new rebuilt MRL panel) and the **HS6 sample**. PPML = `pyfixest.fepois`, CRV1 cluster on exp×dest. S1 = `exp×hs6×year + dest×year`; S2 = S1 + `exp×dest×hs6`.

## Results (`beta_robustness_summary.csv`)

| id | sample (HS6) | stringency | cov | **S1 β** | sig | S2 β | sig |
|----|---|---|---|---|---|---|---|
| **A** | frozen 125 | **old** | 100% | **−1.4685** | *** | +0.149 | * |
| **B** | frozen 125 | **new** | 85.6% | **−0.0160** | ns | +0.137 | * |
| **C** | **common 107** | **old** | 100% | **−1.5232** | *** | +0.163 | ** |
| **D** | **common 107** | **new** | 100% | **−1.5219** | *** | +0.162 | ** |
| E | new coverage 169 | new | 92.3% | −0.0606 | ns | +0.129 | * |
| F | new core-RAC 126 | new | 90.5% | −0.0107 | ns | −0.177 | ns |

## What this proves

**1. The old result replicates exactly.** Spec A = −1.4685*** recovers the published −1.47***. The estimation pipeline is sound and reproducible.

**2. The concordance VALUE-corrections are immaterial to β.** On the **common 107 HS6** (present in both old and new stringency panels), old and new give **virtually identical** coefficients: **C = −1.5232*** vs **D = −1.5219*** (S1) and +0.163 vs +0.162 (S2). Consistent with the stringency values themselves: corr(old,new) = **0.962**, **990/1062 (hs6,year) cells identical**, means 5.614 vs 5.570. → *The corrected concordance does NOT overturn the core finding.* This is the reassuring headline.

**3. The scary "β → 0" (spec B, E, F) is an HS6-SET / aggregation artifact, not a stringency-value effect.**
- **Spec B** drops to −0.02 purely because **18 frozen-panel HS6 (12.4% of trade value) are orphaned to treatment=0** under the new MRL panel — chiefly **HS 081090 "other fresh fruit" ($17.0M, ~8% of panel)**. The corrected concordance deliberately **splits** this catch-all into dedicated codes (durian 0163100, longan, rambutan…). On the frozen 125-HS6 grid those dedicated codes don't exist, so 081090's products simply vanish from treatment → mechanical collapse. Not a data error.
- **Specs E/F** use the *correct* new HS6 universe, yet still attenuate to ≈0. Mechanism: once the catch-all is split into dedicated codes **and** processed-form coverage is added (milled rice, shelled nuts, crushed spices — the bulk of ASEAN value), the strong negative signal that was **concentrated in the aggregated fruit code + fresh-RAC core** no longer dominates the value-weighted average; separation also removes 47k–269k obs, shrinking identifying variation.

## Honest interpretation (do NOT over-claim)

- ✅ **Defensible:** the corrected concordance is sound; on a like-for-like sample it leaves the −1.5*** result intact (C≈D). The reviewers' fixes did not manufacture or destroy the effect.
- ⚠️ **Open analytical question (NOT a settled "effect vanished"):** the headline magnitude is **sensitive to HS6 aggregation level and product coverage**. The strong effect lives in aggregated/fresh produce (esp. 081090); it attenuates when trade is disaggregated to dedicated codes and broadened to processed forms. This is exactly the **FE/specification sign-and-magnitude instability** flagged in Xiong & Beghin and matches this project's own earlier same-sample diagnostic (concordance errors immaterial to β).
- **Implication for the paper:** report A (replication) + C/D (robustness to concordance) as the core; treat E/F (disaggregated/coverage) as a **specification-sensitivity section**, with 081090 as the worked example of why aggregation matters. Do not present E/F as a refutation of A.

## Next analytical step (not yet done)
Decide the **estimand**: aggregated-RAC (paper's current −1.5 story) vs disaggregated-dedicated (≈0). This is a modeling choice for the author + reviewers, not a data-correctness issue. Recommend an explicit aggregation-robustness table in the manuscript.

## Files
`beta_robustness_summary.csv`, `beta_common_hs6.csv`, build logs `beta_*_log.txt`, panels `asean_baci_panel_rebuilt_{legacy,current}.csv`, `asean_mrl_panel_rebuilt_current.csv`.
