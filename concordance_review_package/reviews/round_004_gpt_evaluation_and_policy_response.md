# Round 004 — GPT evaluation and policy response

Reviewer: GPT-5.5 Pro  
Date: 2026-06-29  
Scope: `round_004_cowork_to_gpt_rac_vs_coverage_policy.md`, `data/concordance_release_long.csv`, `reviews/adjudication_decisions.csv`, `sources/product_codes_HS12_V202601.csv`

## Overall assessment

Round 004 is a strong improvement over the previous release-long logic. The move from a mechanical `eu_code.endswith("0000")` rule to explicit `release_policy` is correct. The restored commodity rows — tea, coffee, cocoa, carob, hops and algae — should remain in release outputs when they are in the study scope. The log files are also useful and should stay in the repository so later agents can reconstruct GPT/cowork decisions.

However, this round should not be treated as final yet. There are two blockers:

1. `build_release_long.py` and `validate_release_long.py` point to `concordance_review_package/outputs/...`, while the repository files supplied for review are under `concordance_review_package/data/...`. In a clean checkout this can make CI validate/build a different location or fail if `outputs/` does not exist.
2. `data/concordance_final_asean.csv` currently does not expose `release_policy` / `release_reason` columns, while `release_long` already contains them. The source-of-truth table and generated release are therefore out of sync.

There is also one likely product omission to check: fruit strawberries `0152000` are present in `concordance_final_asean.csv` as `081010`, but I did not find `0152000` in the current `concordance_release_long.csv` chunks reviewed. This should be checked by script before accepting the current release file.

## Recommended general policy

Use a two-layer approach, not a single blanket RAC-only or blanket trade-coverage policy.

Main econometric release should be `TRADE_COVERAGE_PRIMARY`: include HS6 codes that preserve the same commodity identity and capture real ASEAN export flows, including shelling, seed/non-seed split, and whole/crushed split where HS2012 treats them as paired forms of the same commodity. This avoids assigning MRL treatment only to small or irrelevant HS flows.

Keep a second strict robustness release, `CORE_RAC_ONLY`, containing only the closest raw/RAC HS6 forms. This lets the paper report whether findings are robust to a narrower legal interpretation.

Do not include downstream processed goods such as oils, extracts, flours, prepared foods, mixtures, confectionery, or beverages unless a separate processed-food treatment design is created.

## Policy decisions requested by cowork

```csv
eu_code,eu_desc,recommended_hs6,release_policy,rationale
0120010,Almonds,080211;080212,EXPORT_PRODUCT,"Use both in-shell and shelled. HS2012 separates the same nut by shelling state; shelling does not change commodity identity enough to drop trade coverage. Tag 080211=CORE_RAC and 080212=PRIMARY_EQUIVALENT if tiering is added."
0120020,Brazil nuts,080121;080122,EXPORT_PRODUCT,"Use both in-shell and shelled for trade coverage; same commodity identity."
0120030,Cashew nuts,080131;080132,EXPORT_PRODUCT,"Use both, with 080132 essential for ASEAN/Vietnam trade coverage. RAC-only 080131 would miss a large share of actual cashew kernel trade."
0120040,Chestnuts,080241;080242,EXPORT_PRODUCT,"Use both in-shell and shelled."
0120050,Coconuts,080111;080112;080119,EXPORT_PRODUCT,"Current 080111-only is too narrow and is desiccated coconut. Include 080112 and 080119; consider 080112/080119 as CORE/primary and 080111 as primary processed coverage."
0120060,Hazelnuts/cobnuts,080221;080222,EXPORT_PRODUCT,"Use both in-shell and shelled."
0120070,Macadamias,080261;080262,EXPORT_PRODUCT,"Use both in-shell and shelled."
0120080,Pecans,080290,EXPORT_PRODUCT,"HS2012 has no pecan-specific in-shell/shelled split at HS6; keep 080290."
0120090,Pine nut kernels,080290,EXPORT_PRODUCT,"HS2012 has no pine-nut-specific HS6; keep 080290."
0120100,Pistachios,080251;080252,EXPORT_PRODUCT,"Use both in-shell and shelled."
0120110,Walnuts,080231;080232,EXPORT_PRODUCT,"Use both in-shell and shelled."
0820060,"Peppercorn (black, green and white)",090411;090412,EXPORT_PRODUCT,"Use whole + crushed/ground for trade coverage; same Piper commodity."
0820070,Vanilla,090510;090520,EXPORT_PRODUCT,"Use neither-crushed + crushed/ground."
0830010,Cinnamon,090611;090619;090620,EXPORT_PRODUCT,"Use cinnamon whole forms plus crushed/ground. 090619 covers non-C. zeylanicum and cinnamon-tree flowers; include if Annex commodity is cinnamon broadly."
0850010,Cloves,090710;090720,EXPORT_PRODUCT,"Use neither-crushed + crushed/ground."
0810090,Nutmeg,090811;090812,EXPORT_PRODUCT,"Use neither-crushed + crushed/ground."
0870010,Mace,090821;090822,EXPORT_PRODUCT,"Use neither-crushed + crushed/ground."
0820040,Cardamom,090831;090832,EXPORT_PRODUCT,"Use neither-crushed + crushed/ground."
0810040,Coriander,090921;090922,EXPORT_PRODUCT,"Use neither-crushed + crushed/ground."
0810050,Cumin,090931;090932,EXPORT_PRODUCT,"Use neither-crushed + crushed/ground."
0810010,Anise/aniseed,090961;090962,EXPORT_PRODUCT,"Use paired neither-crushed + crushed/ground bucket."
0810070,Fennel,090961;090962,EXPORT_PRODUCT,"Use paired neither-crushed + crushed/ground bucket."
0820030,Caraway,090961;090962,EXPORT_PRODUCT,"Use paired neither-crushed + crushed/ground bucket."
0820050,Juniper berry,090961;090962,EXPORT_PRODUCT,"Use paired neither-crushed + crushed/ground bucket."
0840020,Ginger,091011;091012,EXPORT_PRODUCT,"Use neither-crushed + crushed/ground."
0840030,Turmeric/curcuma,091030,EXPORT_PRODUCT,"Keep 091030; HS2012 has no separate crushed/ground split for turmeric at HS6."
0860010,Saffron,091020,EXPORT_PRODUCT,"Keep 091020."
0620000,Coffee beans,090111;090112,EXPORT_PRODUCT,"Main release: green/not-roasted only. Add 090121;090122 only to a coverage/sensitivity release because roasting is a stronger processing step."
0700000,HOPS,121010;121020,EXPORT_PRODUCT,"For trade coverage include both hop cones and ground/powder/pellet/lupulin. If maintaining strict RAC, keep 121010 as CORE and tag 121020 as PRIMARY_PROCESSED/SENSITIVITY."
0140020,Cherries (sweet),080929,EXPORT_PRODUCT,"Keep parent-only mapping to sweet/other cherries. Add 080921 only in an Annex-subitem-expanded release, not in the parent-only main release."
```

## Required pipeline changes

1. Make `data/concordance_final_asean.csv` the source of truth, or explicitly move source files into `outputs/` and commit them. Do not let scripts read from a path that is not in the review package.
2. Add `release_policy`, `release_reason`, and preferably `coverage_tier` to the source table that build scripts actually read.
3. Add a validation step: every `EXPORT_PRODUCT` row in the source with nonblank `hs6` must appear in `release_long` after exploding HS6.
4. Add a validation step: `release_long` must not contain rows whose source policy is not `EXPORT_PRODUCT`.
5. Add a validation step for high-value known commodities: `0152000`, `0610000`, `0620000`, `0640000`, `0650000`, `0700000`, `0290000` must be present if the source marks them as `EXPORT_PRODUCT`.
6. Keep `ROUND_LOG.md`, `agent_rounds_log.csv`, and `adjudication_decisions.csv` under version control and update them every round.

## Acceptance criteria for next cowork push

- `build_release_long.py` runs from repo root on a clean checkout.
- `validate_release_long.py` runs from repo root on a clean checkout.
- `concordance_final_asean.csv`, `concordance_release_long.csv`, and `adjudication_decisions.csv` agree on policy.
- Pending RAC-vs-coverage decisions are resolved or explicitly represented using `coverage_tier`.
- Fruit strawberries `0152000 -> 081010` are present or a written reason for exclusion is recorded.
