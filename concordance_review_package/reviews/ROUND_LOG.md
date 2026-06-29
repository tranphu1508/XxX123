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

## Round 004 — GPT eval + RAC-vs-coverage policy → cowork incorporate
- Date: 2026-06-29 | Actor: GPT eval (round_004_gpt_evaluation...) → cowork
- GPT bắt: (a) script trỏ sai path (outputs/ + raw-frozen) → đã đổi đọc data/ + sources/ (self-contained); (b) package data/ chưa có release_policy → đã sync; (c) **strawberries 081010 RỚT** do luật "(b).." loại nhầm → thay bằng **luật có-con-thật** (parent chỉ children-only NẾU thực sự có dòng con); (d) thêm validator **known-commodity-presence**.
- POLICY (GPT chốt): **hai tầng** — main=TRADE_COVERAGE_PRIMARY, robustness=CORE_RAC_ONLY. Đã áp coverage: nuts in-shell+shelled (cashew 080131;080132...), spices whole+crushed (pepper 090411;090412...), coffee green-only baseline, hops 121010 baseline, cherry 080929 parent-only.
- Output: concordance_final_asean.csv (release_policy luật mới: EXPORT_PRODUCT 216/CHILDREN_ONLY 56/NEC 31/NONFOOD 77/ADJ 1); build+validate self-contained; **release_long 262 dòng, validator PASS (gồm presence check)**.
- CÒN: build CORE_RAC_ONLY robustness release (cần tag dạng-RAC từng category; cereal RAC=grain không phải seed). Chờ user duyệt hướng coverage trước khi coi final.

## Round 005 — Opus independent third review → cowork
- Date: 2026-06-29 | Actor: Opus (reviewer độc lập #3) | Input: commit round-3 (234 dòng release_long)
- Phương pháp: kiểm 234/234 dòng release_long + dựng lại 168/168 mã loại; check "orphan heading".
- HỘI TỤ với round-4 (cowork làm độc lập): 7 commodity Opus báo bị loại (khoai tây/dâu tây/ngô ngọt/su hào/cải xoong/lá nho/witloof) ĐÃ được round-4 cứu qua **cùng luật có-con-thật** Opus đề xuất; coconut/cinnamon đã có mã RAC. Opus xác nhận ~80 fix trước ĐÚNG.
- Áp thêm theo Opus: cinnamon RAC=cassia 090619 lên đầu; coconut RAC=080119 lên đầu. Policy: Opus đồng thuận GPT (trade-coverage với RAC làm sàn; cashew=080132 bắt buộc).
- Adjudication Opus (18 dòng) merge vào adjudication_decisions.csv.
- CÒN (P1 nhỏ): sweet-pepper 231020 (070960 + Capsicum khô — nhất quán theo policy spice-coverage, hoặc trim); bay-leaf 256090 note; đổi nhãn EXCLUDED_nonfood(animal)→EXCLUDE_ANIMAL (mật/trứng là food).

## Round 006 — Terminal-commodity bug fix + literature synthesis
- Date: 2026-06-30 | Actor: GPT round-006 memo → cowork
- Bug (GPT r6): luật group nhầm anh-em-thành-con (rstrip) → durian/pumpkin/swede/pistachio bị loại oan. Sửa: chỉ mã kết-thúc-"000" mới group-suspect → 4 commodity vào lại. release_long 262→267.
- Literature (yêu cầu GPT): đọc 11 bài + EU Reg 396/2005 Art.20 + Nguyen2026 (đối thủ) + Hejazi2022. Kết: TRADE_COVERAGE_PRIMARY+CORE_RAC_ONLY có cơ sở pháp lý+học thuật. Nguyen xác nhận green-coffee 97.6% + milled-rice 97.9%. Artifacts: literature_inventory/policy_matrix/synthesis.

## Round 007 — Governance/housekeeping (GPT repo check @57f0722)
- Date: 2026-06-30 | Actor: GPT round-007 → cowork
- Sửa: allspice +090422 (whole+ground); reorder 9 mã RAC-first; **build CORE_RAC_ONLY release (220 dòng)**; validator dùng kiểm con-thật (bỏ suffix); cập nhật logs+adjudication statuses; dọn wording synthesis.
- release_long coverage = 268 dòng; CORE_RAC = 220 dòng.
