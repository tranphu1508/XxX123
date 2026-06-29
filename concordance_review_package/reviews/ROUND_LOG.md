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

## Round 008 — CORE_RAC fix + CI (GPT repo check @0d4ed0)
- Date: 2026-06-30 | GPT round-008 → cowork
- Verdict GPT: main coverage = ANALYSIS-READY ✓; CORE_RAC near-ready.
- Sửa CORE_RAC first-token errors: Wheat 100111→100199 (commodity grain), Cotton 120721→120729 (oilseed). Rice 100610 = strict-raw (đã ghi định nghĩa Option A vào build script).
- Thêm validate_release_core_rac.py + .github/workflows/concordance-ci.yml (build+validate cả 2 release). Provenance: 57f0722→0d4ed0.

## Round 009 — End-to-end reproducibility package report (GPT request @70f6ff4)
- Date: 2026-06-30 | GPT round-009 → cowork
- GPT verdict: concordance main + CORE_RAC = ACCEPT; yêu cầu báo cáo reproducibility end-to-end.
- Tạo `reviews/reproducibility_package_report.md` (9 mục A–I): inventory+checksum, data freeze, cleaning, MRL imputation, merge keys (stringency↔BACI 100%), policy, literature/legal, rebuild commands, status matrix.
- TRUNG THỰC: concordance+releases REPRODUCIBLE+CI; raw frozen+checksum (re-download manual); **2 script build panel (asean_mrl_panel, asean_baci_panel) CÒN THIẾU** → ghi rõ là lỗ hổng, sẽ đóng khi rebuild panel.

## Round 010 — Panel rebuild test + β robustness (GPT request @70f6ff4 → tiếp)
- Date: 2026-06-30 | Actor: GPT round-010 memo → cowork
- GPT yêu cầu: viết + CHẠY 2 script build panel, COMPARE vs frozen, DIAGNOSE nếu lệch ("Không được ghi REPRODUCIBLE nếu chưa compare/diagnose").
- **Đóng lỗ hổng:** build_asean_mrl_panel.py + build_asean_baci_panel.py + compare_rebuilt_panel.py (trong scripts/).
- **BACI legacy = KHỚP TUYỆT ĐỐI:** 292,500 dòng, only-old=only-new=0, value 100% khớp, max|diff|=0.0, Σvalue 204,947,397 trùng. → asean_baci_panel REPRODUCIBLE exact.
- **MRL current rebuild:** 1,404 dòng/156 HS6/2015-2023; lệch frozen (1,781/137/2011-2023) = intentional (year-window back-fill + concordance fixes 19 drop/38 add). diagnose_mrl_panel_mismatch.md.
- **β robustness (bonus, quan trọng):** giữ nguyên BACI+treatment+FE+mẫu, chỉ đổi nguồn stringency.
  - A frozen125+old = S1 −1.4685*** (replicate công bố −1.47 CHÍNH XÁC).
  - C/D common-107-HS6: old −1.5232*** vs new −1.5219*** → **GIỐNG HỆT** (corr stringency 0.962, 990/1062 identical). → concordance VALUE-fixes immaterial to β.
  - B/E/F (≈0, NS) = artifact do lệch tập HS6 / mức gộp, KHÔNG do giá trị: 18 HS6 (12.4% value, chủ yếu 081090 "other fruit" $17M) bị orphan→treat=0 khi split catch-all thành mã chuyên biệt.
  - KẾT LUẬN TRUNG THỰC: concordance đã sửa KHÔNG lật kết quả lõi; magnitude nhạy với aggregation level (Xiong-consistent) → đề xuất bảng aggregation-robustness trong manuscript. KHÔNG over-claim "effect vanished".
- Artifacts: rebuild_check/{asean_mrl_panel_rebuilt_current, asean_baci_panel_rebuilt_legacy/current, beta_robustness_summary, beta_common_hs6}.csv + diagnose_{mrl_panel_mismatch, baci_panel_mismatch, beta_robustness_concordance}.md. Cập nhật reproducibility_package_report.md §A/§H/§I.

## Round 011 — Reproducibility hardening (GPT @35dd44f)
- Date: 2026-06-30 | Actor: GPT round-011 memo → cowork
- P0 wording: tách rõ 3 panel — asean_baci_panel(legacy)=REPRODUCIBLE EXACT; asean_mrl_panel(legacy frozen)=SUPERSEDED/NOT exact-reproduced; asean_mrl_panel_rebuilt_current=REPRODUCIBLE current build. Sửa §A + §I reproducibility_package_report.
- P0 manifest: rebuild_check/generated_outputs_manifest.csv (sha256 đầy đủ cho 3 output: BACI legacy 292500/sha ddbaa6e3, BACI current 395460/sha 11f0f1e0, MRL current 1404/sha be1106ab). 2 BACI lớn committed=false (.gitignore), MRL current committed=true.
- P0 portable: build_asean_mrl_panel.py + build_asean_baci_panel.py nhận CLI args (--mode/--concordance/--binding-panel/--baci-dir/--frozen-panel/--release-long/--year-min/--year-max/--out) + in "USING ...". ĐÃ TEST: MRL current=1404; BACI legacy=292500 (compare vs frozen: value max|diff|=0, Σvalue khớp, only_old=only_new=0).
- P1 compare nâng cấp: compare_rebuilt_panel.py 10 checks (schema/rowcount/key-uniqueness/dup-sample/coverage/numeric max-abs+rel+mean+count-tol/categorical/NA/sorted-norm sha256/value-sum) + xuất md+csv+json.
- P1 CI wording: "CI workflow added; run status unverified" (bỏ "CI chạy" — chưa có run ID).
- P1 raw scripts: copy download_baci.py + download_eu_mrl_api.py + filter_baci.py → scripts/raw_data_collection/; + reviews/raw_download_manual_steps.md (source/URL/version/sha256/size/placement/verify cho BACI zip 2dd0dd61 1.27GB + MRL snapshot bc3643ec 367MB).
- P1 estimation diagnostics: bỏ absolute /sessions/ path khỏi samesample_diag*.py + measure_distortion*.py → resolve từ __file__ + env STUDY_ROOT (portable-to-layout). Verify: 0 absolute path còn lại, all parse OK.
- Housekeeping: round_011 + dọn 4 round md trùng ngoài study root → reviews/.
- Acceptance criteria GPT §11: 8/8 done.
