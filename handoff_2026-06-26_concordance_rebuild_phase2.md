# Handoff — 2026-06-26 — Concordance EU→HS6 (HS2012) Phase 2 (neo Codex + tên khoa học) — đã DỪNG

## 1. Metadata
- Ngày: 2026-06-26. Trạng thái: HOÀN TẤT Phase 2; **ĐÃ DỪNG** chờ duyệt residual + quyết phạm vi.
- Task: "Concordance rebuild Phase 2 — neo Codex + tên khoa học + đa-phiếu hội tụ".

## 2. Đã làm gì + SỐ CHÍNH
- **Mỏ neo lõi:** nhóm Codex/EU → heading HS2012, **60 dòng, verify 60/60** (text heading BACI).
- **Đa-phiếu hội tụ** (A loài→heading→HS6 / B fuzzy / C bản cũ / D auto): **verified_high 84** (auto-accept, có trích dẫn), needs_confirm 30, needs_arbitration 60, nhóm một-nhiều 85, ngoài-neo (chế biến/động vật) 75, n.e.c. 47.
- **SỬA đúng lỗi fuzzy Phase 1:** Wheat→100111 (không buckwheat), Cassava→071410 (không Mate), Spinaches→070970 (không spices), Melons→0807 (không vỏ 0814).
- **Referential 0 lỗi**; coverage in-scope **174/184 (95%)**; HS07–10 unmapped 94.
- Nguồn ngoài (Codex PDF/HS-EN/Fiankor) KHÔNG kéo được (FAO timeout/paywall) → neo bằng tên khoa học + text heading HS2012 local (đều kiểm chứng).

## 3. Cấu trúc — thay đổi
- THÊM: `03_/scripts/build_concordance_phase2.py`; `03_/outputs/` (codex_group_to_hs_heading + concordance_decision_table_phase2 + concordance_final_candidate, CSV); `03_/concordance_rebuild_phase2_report_2026-06-26.md` + `codex_group_to_hs_heading_2026-06-26.md` + `concordance_manual_arbitration_ledger_2026-06-26.md`.
- SỬA: `00_/data_sources_and_provenance.md` (anchor row); `11_/issues_log.md` (HS revision ĐANG GỠ).
- review_artifacts: +phase2 report + codex anchor; refresh provenance + issues_log.

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Đổi nền: neo **loài + Codex + HS2012** (độc lập AI) thay vì fuzzy tên thường (Phase 1 sai wheat→buckwheat…). Constrain match TRONG heading → tin cậy cao.
- verified_high = A trong heading + (≥1 phiếu trùng HOẶC heading duy-nhất-HS6) → có trích dẫn, auto-accept không cần duyệt từng cái.
- Nguồn ngoài không kéo được → neo bằng local có thẩm quyền (text heading HS2012 + tên khoa học).
- Phạm vi tươi/chế biến: ĐỀ XUẤT (mặc định tươi/thô vào mẫu chính; chế biến gắn cờ form) — ghi analytical_decisions_log KHI finalize, chưa ghi.
- DỪNG — chưa finalize.

## 6. Cờ cần review (finalize)
- Duyệt residual: needs_confirm 30 + needs_arbitration 60 + nhóm 85 + ngoài-neo 75 + n.e.c. 47 (mỗi ca có vote_A + trích dẫn). Quyết phạm vi tươi/chế biến.
- issues_log: HS revision ĐANG GỠ (ĐÓNG khi finalize).

## 7. Con trỏ bằng chứng
- `03_/concordance_rebuild_phase2_report_2026-06-26.md`; `outputs/concordance_decision_table_phase2_2026-06-26.csv` + `concordance_final_candidate_2026-06-26.csv` + `codex_group_to_hs_heading_2026-06-26.csv`; `scripts/build_concordance_phase2.py`; ledger.
