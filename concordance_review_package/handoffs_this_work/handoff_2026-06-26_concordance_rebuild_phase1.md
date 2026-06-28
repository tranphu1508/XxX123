# Handoff — 2026-06-26 — Rebuild concordance EU→HS6 (HS2012) — Phase 1 (đã DỪNG)

## 1. Metadata
- Ngày: 2026-06-26. Trạng thái: HOÀN TẤT Phase 1; **ĐÃ DỪNG** chờ duyệt decision_table.
- Task: "Rebuild concordance EU product_code → HS6 (HS2012), Phase 1".

## 2. Đã làm gì + SỐ CHÍNH
- 2 tập tham chiếu: EU **381 sản phẩm** (`Pesticide-residues-products-All.csv`, có tên khoa học, snapshot 2026-05-27) + HS2012 **198 HS6 (07–10)** từ BACI đóng băng. **Referential 0 lỗi**.
- Matcher tái lập (`scripts/build_concordance_candidates.py`, rapidfuzz: tên khoa học + fuzzy mô tả + gợi ý bản cũ) → draft + decision_table.
- Status (381): **auto_accept 59**, needs_review 96 (**21 OLD_DISAGREE**), nhóm một-nhiều 62, n.e.c. 47, ngoài-07-10 88, không-khớp 29. Lá in-scope 184: aa 59 / nr 96 / ex 29; ≥medium 62%.
- Đối chiếu bản cũ: **~76% đồng thuận**; 21 ca bản-cũ-bất-đồng lộ lỗi auto-match dạng (vd Wheat→buckwheat, Beans-with-pods→đậu khô) → cờ đỏ.
- Độ phủ HS07–10: **96/198 có EU map; 102 chưa** (HS chế biến-gộp). many-one 32.

## 3. Cấu trúc — thay đổi
- THÊM: `03_/scripts/build_concordance_candidates.py`; `03_/outputs/concordance_draft_2026-06-26.csv` + `concordance_decision_table_2026-06-26.csv`; `03_/concordance_rebuild_phase1_report_2026-06-26.md`.
- SỬA: `00_/data_sources_and_provenance.md` (+EU product catalogue); `11_/issues_log.md` (HS revision flag ĐANG GỠ).
- review_artifacts: +phase1 report; refresh provenance + issues_log.

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Build lại từ đầu (script tái lập + decision table) vì bản cũ không log quyết định → không audit được.
- Auto-accept SIẾT (bản cũ đồng thuận HOẶC tên khoa học); auto-match dễ sai dạng (tươi/khô) → ca bản-cũ-bất-đồng hạ về needs_review (cờ OLD_DISAGREE).
- HS neo HS2012 qua BACI metadata → gỡ cờ MEDIUM HS revision (referential 0 lỗi).
- DỪNG — chưa chốt concordance (chờ duyệt).

## 6. Cờ cần review (Phase 2)
- Duyệt `concordance_decision_table`: 96 needs_review (ưu tiên 21 OLD_DISAGREE) + 62 nhóm một-nhiều + 47 n.e.c. + 88 ngoài-scope + 29 không-khớp.
- issues_log: HS revision ĐANG GỠ (đóng khi Phase 2 chốt concordance).

## 7. Con trỏ bằng chứng
- `03_/concordance_rebuild_phase1_report_2026-06-26.md`; `03_/outputs/*.csv`; `03_/scripts/build_concordance_candidates.py`.
