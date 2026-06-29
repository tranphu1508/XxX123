# Compare panel -- /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/04_maximum_residue_level_panel/outputs/asean_mrl_panel.csv  vs  /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/internal_handoff_log_for_claude/concordance_review_package/rebuild_check/asean_mrl_panel_rebuilt_current.csv

**Verdict:** DIFFERENCES (xem chi tiet + diagnosis)

- schema_equal=False | cols_only_old=['lump_divergent'] | cols_only_new=[]
- rows old=1781 new=1404
- key uniqueness: old unique=True (dup=0) | new unique=True (dup=0)
- key coverage: common=1062 | only_old=719 | only_new=342
- sorted-normalized checksum: equal=False
    - old_sha256=1e12e3632b8711f1b6a614cf8baf489021f0a128917d9cdbcaf757ec88aa9395
    - new_sha256=dacae9b9fb36ff80cfbd14bc223658079c92e266adce267d7f6ff3b15e4cf2cf

## Numeric columns (tren common keys)

| col | max_abs | max_rel | mean_abs | #>tol |
|---|---|---|---|---|
| n_eu_codes | 10 | 0.909091 | 1.14407 | 477 |
| lumped | 1 | 1 | 0.440678 | 468 |
| min_mrl_weakest | 0.007 | 4 | 0.000244821 | 72 |
| stringency | 1.6095 | 0.261422 | 0.0609772 | 72 |

_diff keys -> /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/internal_handoff_log_for_claude/concordance_review_package/rebuild_check/compare_asean_mrl_panel_diff.csv ; machine-readable -> /sessions/modest-dazzling-tesla/mnt/EU standards Effects on ASEAN Agri-food Exports/eu_maximum_residue_level_asean_export_study/internal_handoff_log_for_claude/concordance_review_package/rebuild_check/compare_asean_mrl_panel.json_
