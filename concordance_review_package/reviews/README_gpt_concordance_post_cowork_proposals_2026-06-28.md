# GPT concordance proposals after cowork push — 2026-06-28

Source reviewed:
- `concordance_review_package/data/concordance_final_asean.csv`
- Git blob SHA observed via GitHub connector: `bc546a073d8dabec38a4181bb93dcc30f4d8cdc4`
- Raw URL: https://raw.githubusercontent.com/tranphu1508/XxX123/main/concordance_review_package/data/concordance_final_asean.csv
- HS2012 source: https://raw.githubusercontent.com/tranphu1508/XxX123/main/concordance_review_package/sources/product_codes_HS12_V202601.csv
- Annex/species source: https://raw.githubusercontent.com/tranphu1508/XxX123/main/concordance_review_package/sources/annex1_species_to_code.csv

Purpose:
- Provide row-level and pipeline-level proposals for the EU Annex I → HS2012 HS6 concordance.
- Intended path in repo: `concordance_review_package/reviews/gpt_concordance_post_cowork_proposals_2026-06-28.csv`.

Interpretation of priorities:
- `P0`: should block release or be adjudicated before econometric merge.
- `P1`: should be resolved for exactness, but can be tracked as methodological scope if intentionally excluded.
- `P2`: policy decision; include/exclude depending on study scope.

Core recommendations:
1. Do not export group headings to the final `release_long` file. Use child product rows only.
2. Convert literal `nan` in `hs6` to a true empty cell.
3. Explode all semicolon-delimited HS6 fields into one row per `eu_code`–`hs6`.
4. Add CI checks for HS2012 existence, no stale `NO_HS6`, no stale `hs6_lumped`, no group heading export, no excluded rows in release.
5. Adjudicate global policies for:
   - seed vs non-seed cereal/oilseed HS splits;
   - in-shell vs shelled tree nut HS splits;
   - whole vs crushed/ground spice HS splits;
   - fresh-only vs fresh+frozen vegetables;
   - RAC-only vs processed-form inclusion for tea/coffee/spices.

Counts in proposal file:
- Total proposal rows: 85
- P0 rows: 24
- P1 rows: 41
- P2 rows: 20

Notes:
- Rows already fixed in the cowork-pushed file are not repeated unless there is still a residual split, group-heading, metadata or policy issue.
- `recommended_hs6_or_policy` may contain `NO_DIRECT_GROUP_MAP` for group headings. These rows should be excluded from `release_long`, not literally written as HS codes.
