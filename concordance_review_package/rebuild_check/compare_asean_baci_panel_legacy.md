# Compare panel -- /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/07_main_estimation_stata/asean_baci_panel.csv  vs  /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/internal_handoff_log_for_claude/concordance_review_package/rebuild_check/asean_baci_panel_rebuilt_legacy.csv

**Verdict:** DIFFERENCES (xem chi tiet + diagnosis)

- schema_equal=False | cols_only_old=['cohort', 'treated', 'post', 'etime', 'did'] | cols_only_new=[]
- rows old=292500 new=292500
- key uniqueness: old unique=True (dup=0) | new unique=True (dup=0)
- key coverage: common=292500 | only_old=0 | only_new=0
- sorted-normalized checksum: equal=False
    - old_sha256=3a6063a215f9d8b43e659f8acbba683b7a97842fb023dfdc5acf3e40f3307f25
    - new_sha256=45c7ea8d4976bb9cf08d27abe2996fe30a590f4f19a6601e61ee57c615b50c66
- value-sum: old=204947397 new=204947397 diff=-0

## Numeric columns (tren common keys)

| col | max_abs | max_rel | mean_abs | #>tol |
|---|---|---|---|---|
| eu | 0 | 0 | 0 | 0 |
| value | 0 | 0 | 0 | 0 |

_diff keys -> /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/internal_handoff_log_for_claude/concordance_review_package/rebuild_check/compare_asean_baci_panel_legacy_diff.csv ; machine-readable -> /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/internal_handoff_log_for_claude/concordance_review_package/rebuild_check/compare_asean_baci_panel_legacy.json_
