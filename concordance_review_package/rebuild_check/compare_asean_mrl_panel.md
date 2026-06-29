# Compare
- old: /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/04_maximum_residue_level_panel/outputs/asean_mrl_panel.csv (1781 rows)
- new: concordance_review_package/rebuild_check/asean_mrl_panel_rebuilt_current.csv (1404 rows)
- schema old: ['hs6', 'year', 'n_eu_codes', 'lumped', 'min_mrl_weakest', 'stringency', 'lump_divergent']
- schema new: ['hs6', 'year', 'n_eu_codes', 'min_mrl_weakest', 'lumped', 'stringency']
- keys old=1781 new=1404 | chung=1062 | chỉ-old=719 | chỉ-new=342
- max |diff| numeric: {'n_eu_codes': 10.0, 'lumped': 1.0, 'min_mrl_weakest': 0.007, 'stringency': 1.6094999999999997}
