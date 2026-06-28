# Inventory audit (19 artifact) — 2026-06-26

| label | path | exists | n_rows | n_cols | sha256 | key_cols | key_unique | n_null_critical | claimed_vs_actual |
|---|---|---|---|---|---|---|---|---|---|
| 01 BACI zip | 01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601.zip | True | 1267950839B |  | 2dd0dd6174f1… |  | n/a | n/a | tồn tại (1267950839B) |
| 01 EU MRL snapshot | 01_raw_data_frozen/european_union_maximum_residue_level_snapshot/eu_mrl_bulkdownload_snapshot_2026-05-27.json | True | 519650 |  | bc3643ec8a99… |  | n/a | n/a | KHỚP (519650) |
| 01 Annex I legal | 01_raw_data_frozen/eu_annex1_legal/L_2018018EN.01000101.xml.html | True | 1430139B |  | c4cb8987f2d7… |  | n/a | n/a | tồn tại (1430139B) |
| 01 MARD MASTER | 01_raw_data_frozen/vn_mard_circulars/MASTER_pesticide_crop_parsed.csv | True | 26877 | 12 | 7361eb9feca7… |  | n/a | n/a | KHỚP (claim 26878=wc-l incl header; data=26877) |
| 03 concordance_final_vn | 03_concordance_product_code_to_harmonized_system_six_digit/outputs/concordance_final_vn_2026-06-26.csv | True | 27 | 10 | f3c4810fb146… | eu_code+hs6 | YES | 0 | KHỚP (27) |
| 03 annex1_species_to_code | 01_raw_data_frozen/eu_annex1_legal/annex1_species_to_code.csv | True | 1305 | 5 | 0a8ec7045eed… | parent_code+sub_code | YES | 25 | KHỚP (1305) |
| 04 panel jan01 reference | 04_maximum_residue_level_panel/outputs/eu_mrl_binding_panel_reference_jan01_2026-06-26.csv | True | 578090 | 16 | 5b2c3b52c8a3… | pesticide_residue_id+product_code+year | YES | 141023 | KHỚP (claim 578091=wc-l incl header; data=578090; null=not_yet_set139699+pending1324) |
| 04 panel jan01 extended | 04_maximum_residue_level_panel/outputs/eu_mrl_binding_panel_vn_extended_jan01_2026-06-26.csv | True | 36050 | 16 | 5becea8789f1… | pesticide_residue_id+product_code+year | YES | 9198 | KHỚP (36050) |
| 04 mrl_time_variation_diag | 04_maximum_residue_level_panel/outputs/mrl_time_variation_diagnostic.csv | True | 8755 | 10 | 748e0521fd2f… | substance_id+product_code | YES | 0 | KHỚP (8755) |
| 05 omega_basket | 05_active_ingredient_set_and_classification/omega_vn_registration_basket.csv | True | 918 | 11 | 600d479d8bfb… | substance+eu_code+omega_source_period | YES | 0 | KHỚP (918) |
| 05 omega_national_fallback | 05_active_ingredient_set_and_classification/omega_vn_national_fallback.csv | True | 54 | 5 | 51508f8f1511… | substance+omega_source_period | YES | 0 | KHỚP (54) |
| 05 A_k_members | Xây Panel Merge/Xây Ak/A_k_members.csv | True | 57957 | 15 | f7ccf0d9d6d7… | eu_code+pest_res_id | YES | 0 | KHỚP (57957) |
| 07 index_variants | 07_main_estimation_stata/index/vn_stringency_index_variants.csv | True | 272 | 17 | 8ad513bfe3a1… | product_code+year | YES | 0 | KHỚP (272) |
| 07 index_weighted | 07_main_estimation_stata/index/vn_stringency_index_weighted.csv | True | 272 | 11 | de7af65b18c3… | product_code+year | YES | 0 | KHỚP (272) |
| 07 natural_experiments | 07_main_estimation_stata/index/vn_change_natural_experiments.csv | True | 62 | 6 | c9867339ac5c… |  | n/a | 0 | KHỚP (62) |
| 07 baci_eventstudy_panel | 07_main_estimation_stata/baci_eventstudy_panel.csv | True | 7488 | 10 | ba0450e5584d… | product+dest+year | YES | 0 | KHỚP (7488) |
| RASFF T4 | 02_data_collection_and_api_scripts/rasff_feasibility_scan/outputs/T4_vn_pesticide_product_x_year.csv | True | 78 | 3 | 370935f651d9… | group+year | YES | 0 | (không claim; 78 dòng) |
| RASFF T5 | 02_data_collection_and_api_scripts/rasff_feasibility_scan/outputs/T5_vn_active_substance_counts.csv | True | 18 | 2 | cff916a70157… |  | n/a | 0 | KHỚP (18) |
| RASFF all_records | 02_data_collection_and_api_scripts/rasff_feasibility_scan/outputs/all_records_2026-06-26.csv | True | 328 | 7 | e2a5d89939c5… |  | n/a | 96 | KHỚP (328) |
