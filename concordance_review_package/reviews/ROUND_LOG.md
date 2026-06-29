# Concordance review round log

## Round 001 — GPT independent audit (381 mã)
- Date: 2026-06-29 | Actor: GPT-5.5 Pro | Input: commit 2c0d161 (concordance_final_asean.csv)
- Findings: 85 SAI + 196 NGỜ. Cowork adjudicate → **70 lỗi map thật** (fungi→ớt, brassica→súp lơ, beans Phaseolus, kumquat→citrus, dedicated chicory/ginseng/mate, missing hops/cocoa/algae/carob).
- Output: 70 GPTFIX trong concordance. Evidence: audit_evidence/GPT_independent_audit_2026-06-29.csv + GPT_review_adjudication_2026-06-29.md.

## Round 002 — GPT structured proposals (85, P0/P1/P2) + validator
- Date: 2026-06-29 | Actor: GPT-5.5 Pro | Input: commit 256e572
- Findings: sweet-cherry 080921(chua)→080929; 8 ca seed↔grain split; data hygiene (nan/stale flags); validator.
- Output: 10 GPT2FIX + group-heading flag + hygiene; concordance PASS validator GPT. Evidence: reviews/gpt_concordance_post_cowork_proposals_2026-06-28.csv.

## Round 003 — Release_long export policy + audit logging
- Date: 2026-06-29 | Actor: cowork (responding to GPT round-3 memo)
- Source commit: 256e572 | Memo: reviews/round_003_gpt_to_cowork_release_long_policy_and_logging.md
- BLOCKER FIXED: luật đuôi-0000 loại nhầm Tea/Coffee/Cocoa/Hops/Algae/Carob (XK lớn) → thay bằng cột **release_policy** tường minh; khôi phục 6 commodity.
- Output: release_policy (EXPORT_PRODUCT 213 / EXPORT_CHILDREN_ONLY 58 / EXCLUDE_NEC 31 / EXCLUDE_NONFOOD 77 / ADJUDICATE 2); build_release_long.py + validate_release_long.py; release_long rebuild = 234 dòng, validator PASS.
- PENDING (cần user chốt scope): RAC-only vs trade-coverage cho coffee-roasted / hops-ground / tree-nuts-shelled / spices-crushed; cherry parent-only vs +subitems.
