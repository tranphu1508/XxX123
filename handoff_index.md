# Handoff Index — mục lục sống (mới nhất trên cùng)

>>> 🆕 CHAT MỚI? Đọc CỔNG CONTEXT trước: `_DOC_TRUOC_TIEN.md` → https://raw.githubusercontent.com/tranphu1508/XxX123/main/_DOC_TRUOC_TIEN.md (dẫn tới 6 file context_knowledge 00–05).


Định dạng: `YYYY-MM-DD | <task> | <raw URL> | <tóm tắt 1 câu>`

2026-06-29 | Đo méo concordance + vá 14 lỗi (β VỮNG) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-29_concordance_distortion_fix.md | ĐO: loại 31 mã lỗi+lumping (24,8% dòng) → S1 −1,47→−1,38, S2 +0,149→+0,141 (cùng dấu/ý nghĩa) → lỗi concordance VÔ HẠI với β. Soi 100% 381 mã: 168 OK + loại-đúng 97 + umbrella 38 + lumping 53 + ~12-15 lỗi. Đã vá 14 (oilseeds, lựu/mãng cầu→fruit-nec, su hào→071490...), 2 borderline cờ REVIEW. Lõi vững → công bố được; lumping ghi Limitations. Panel chưa rebuild — chờ user.

2026-06-29 | Soi rổ flagged concordance (auto_sci_name+needs_review) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-29_concordance_bucket_review.md | ESCALATION: rổ flagged SAI hệ thống — auto_sci_name 8/22 lỗi (hạt dầu lộn mã, ~0,08%KN), needs_arbitration ≥4 lỗi gồm 2 GIÁ TRỊ LỚN (lựu+mãng cầu→080390 CHUỐI 8%, su hào→071410 SẮN 6%, làm bẩn weakest-link stringency chứ không bịa mã). Umbrella 081090/121190/0902 HỢP LỆ. Đã vá 2 (cotton/palm), lập 12 lỗi xác nhận. Lõi verified_high vẫn đúng → β lõi có thể vững, nhưng phải dọn rổ flagged+rebuild — chờ user.

2026-06-29 | Audit HS-revision EU↔BACI + tính đúng concordance | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-29_hs_revision_audit.md | HS-revision KHỚP (136/137 mã HS2012 hợp lệ, panel 125/125); GIẢI cờ Giai đoạn 0. Phát hiện 2 lỗi map (đều auto_sci_name): 0402020 palm→151010(không có HS2012, đúng 120710, rớt vô hại) + 0401090 cotton seed→520100(=xơ bông ch52 NGOÀI 07-12, đúng 120721, NHIỄM panel 2.340 dòng=0,12%KN). Rổ auto_sci_name(22)+needs_review(95) cần soi — chờ user chốt phạm vi+rebuild.

2026-06-29 | ASEAN: diagnostic SAME-SAMPLE (mã loại có lái β=−2,077?) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-29_samesample_diag.md | TÁI LẬP full-185 khớp tuyệt đối; mã SẠCH(112) β=−2,88*** MẠNH HƠN, mã LOẠI(73) null −0,32(ns) → BÁC BỎ nghi vấn 'mã loại lái −2,077' (ngược lại: pháp-lý-hóa gia cố H1, mã loại là nhiễu đo); β mới yếu do thước đo+cấu trúc, KHÔNG do loại mã; S2 3-chiều đổi dấu ở MỌI mẫu = artifact incidental-parameter — chờ user.

2026-06-29 | ASEAN: kiểm ổn định β panel cũ↔mới (M1) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-29_asean_beta_oldnew.md | β_mới S2(3 chiều)=+0,15 (ĐỔI DẤU từ −2,077), S1=−1,47, S3=−0,88 → STOP-RULE: β KHÔNG ổn định → DỪNG, chưa chốt panel, nghi loại mã 185→126 lái kết quả — chờ user.

2026-06-26 | ASEAN Chặng 3: panel BACI đa phương + CỔNG pre-trends | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_asean_eventstudy.md | Panel 292.500 (ASEAN-5×126HS6×52đích); bảng phủ-sóng nước; cohort gạo2018+fruits2022; CỔNG pre-trends GÃY CẢ HAI (gạo F p=0,0009; fruits τ<0 p<0,001) → STOP-RULE → KHÔNG chạy gói nhân quả → cả 2 bài chuyển ĐO-LƯỜNG — DỪNG.

2026-06-26 | ASEAN Chặng 2: panel MRL EU + chẩn đoán gộp + CỔNG hình-dạng-cong | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_asean_mrl_panel_diag.md | 137 HS6 (77 sạch/60 gộp); 11 lump_divergent; CỔNG B KHÔNG ĐẠT — độ-ngặt bó cụm 100% gần-sàn (cấu trúc, weakest-link+mean đều bó) → bỏ cross-section-curvature, chuyển chiều thời gian — DỪNG.

2026-06-26 | ASEAN Chặng 1: un-park + finalize concordance EU→HS6 | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_concordance_asean_finalize.md | 304 mã thực-vật (loại 70 động vật+7 nec); 284 có HS6 + annex1_legal_ref 304/304; ca khả nghi verbatim (thanh long 081040→081090, dâu-tây LÁ 0632010≠quả 0152000); 59 HS6-lumped; 20 umbrella needs_review — DỪNG.

2026-06-26 | Kiểm toán tái lập (inventory + reproduce chéo) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_reproduce_audit.md | CỔNG inventory SẠCH (2 lệch=header off-by-1, null=cờ not_yet_set); 4 checkpoint KHỚP qua engine độc lập (DuckDB 328/180; coef +0,904 trùng tuyệt đối; ω gạo16/ớt2; pre-trends gạo τ=-2 +1,04); Stata vắng→.do cho user — DỪNG.

2026-06-26 | Event-study BACI (chế độ 2: MRL→thương mại) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_eventstudy_baci.md | Tam-sai β=+23% (p=0,12, dấu ngược); PRE-TRENDS FAIL (gạo τ=-2 p=0,003) → KHÔNG nhận diện nhân quả; confounder EVFTA 2020 + durian boom 8× (control nhiễm); TWFE-ATT~0 nhạy đặc tả → đề xuất chuyển chế độ 1 — DỪNG (báo thẳng).

2026-06-26 | Cắm ω vào chỉ số (weakest-link membership) + re-validate | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_index_weighted.md | Bước0: bưởi/chanh lỗi-khớp-tên (thu hồi qua 'cây có múi'), đậu bắp/chanh leo/herbs gap-thật; carbendazim/acephate rớt ~2019, chlorpyrifos/fipronil ~2021; banned-but-used 0 suốt; ω-filter fit RASFF KÉM hơn đều (caveat double-dip, ω vẫn ngoại sinh sạch cho BACI) — DỪNG.

2026-06-26 | Rổ trọng số ω từ thông tư MARD (Danh mục BVTV) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_mard_omega.md | ω chính=03/2016 (Nguyen); granularity CROP-LEVEL; 16/18 RASFF có trong DM; carbofuran+methamidophos banned_but_rejected (25 vụ, ω=0); carbendazim/chlorpyrifos loại 2023; gap 6 mã→national fallback — DỪNG chờ quyết banned + granularity.

2026-06-26 | Thiết kế chỉ số stringency (level/change) + validate RASFF | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_index_design.md | Biến thể THẮNG = S_lvl_max_rasff (weakest-link×RASFF-18, coef+0,90 p=0,004); weakest-link>>mean, RASFF-18>A_k; level/change tách; ω(MARD)+Codex PENDING; CHƯA chạy BACI — DỪNG.

2026-06-26 | Chẩn đoán sức nhận diện MRL (time-variation) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_mrl_identifying_power.md | 34% cặp có-bước-trong-cửa-sổ, 41% phẳng-ở-sàn; top-3 chất (carbendazim/permethrin/chlorfenapyr) KHÔNG biến thiên trong cửa sổ; cụm 2016 omnibus (FE hấp thụ); verdict giữ 2015-2023 + robustness 2011-2023 + cắt-ngang — DỪNG.

2026-06-26 | Annex I PHÁP LÝ đóng băng + đối chiếu 15 mã VN | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_annex1_groundtruth_crosscheck.md | Reg (EU) 2018/62 frozen; parse 381 nhóm+924 sub; 17/17 mã VN KHỚP ground truth (thanh long 0162040-001, rambutan 0163060-006, longan 0162020-001, ớt 0231020-001); +cột annex1_legal_ref — DỪNG.

2026-06-26 | Mở rộng panel MRL lát VN + đối chiếu A_k×RASFF | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_panel_extend_vn_ak_reconcile.md | 7 mã VN vào panel (489 chất×năm, thanh long ĐỦ); acetamiprid MISSING_FROM_A_k; rambutan→0163060; +quy tắc bằng chứng nguyên văn — DỪNG.

2026-06-26 | Annex I verify mã VN (bằng chứng thô) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_annex1_verify.md | Verbatim + grep catalogue: thanh long 0162040 + longan 0162020 + ớt cay 0231020 XÁC NHẬN; RAMBUTAN XÉT LẠI (0163060 Cherimoyas, không 0162020); EUR-Lex pháp lý bị chặn (URL cho user) — DỪNG chờ Claude.
2026-06-26 | Concordance Phase 3b RESOLVE + FINAL lát VN | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_concordance_phase3b_resolve.md | Giải 2 cờ qua synonyms; cà phê rang→processed; MRL-coverage 0 đỏ → FINAL lát VN; cờ VÀNG 6 mã — DỪNG.
2026-06-26 | Concordance Phase 3 FINALIZE lát VN | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_concordance_phase3_vn.md | Sửa lỗi phổ quát; lát VN finalized_vn; parked_asean 363 — DỪNG.
2026-06-26 | RASFF VN density CONFIRMED (ĐỦ-gộp) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_rasff_density_confirmed.md | 328/180; ĐỦ(gộp); carbendazim #1 — DỪNG.
2026-06-26 | RASFF VN density scan (sơ bộ) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_rasff_vietnam_density_scan.md | Path A chặn → Route B (thay bằng CONFIRMED).
2026-06-26 | Concordance EU→HS6 (Phase 2) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_concordance_rebuild_phase2.md | Mỏ neo 60/60; verified_high 84; coverage 95% — DỪNG.
2026-06-26 | Concordance EU→HS6 (Phase 1) | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_concordance_rebuild_phase1.md | auto_accept 59 (fuzzy có lỗi) — thay bằng Phase 2.
2026-06-26 | EU MRL apply: panel ràng buộc | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_eu_mrl_apply.md | Panel bậc thang; pending 420; not_yet_set 24%.
2026-06-26 | EU MRL: phân giải khóa trùng & null | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_eu_mrl_phangiai_khoa_null.md | Tie 22.195, null 579 — DỪNG.
2026-06-26 | Đẩy review_artifacts cho Claude rà | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_push_review_artifacts.md | Copy 5 file .md + ARTIFACTS.
2026-06-26 | Giai đoạn 0 — EU MRL API | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_giaidoan0_eu_mrl_api.md | Snapshot 2026-05-27; ĐẠT 3 nhóm.
2026-06-26 | Giai đoạn 0 — BACI | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_giaidoan0_baci.md | Chốt 202601+HS12; ĐẠT 3 nhóm.
2026-06-26 | Quyết định cửa sổ mẫu | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_quyetdinh_cuaso_mau.md | Mẫu chính 2015–2023, 2024 robustness.
2026-06-26 | Thiết lập repo nhật ký bàn giao | https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_2026-06-26_thiet_lap_repo_log.md | Dựng git repo log chỉ-md.

---

## ARTIFACTS ĐỂ RÀ (review_artifacts/) — bản sao chỉ-đọc, refresh sau mỗi task
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/issues_log.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/analytical_decisions_log.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/data_sources_and_provenance.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/validation_reports/baci_validation_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/validation_reports/eu_mrl_validation_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/eu_mrl_key_null_resolution_proposal_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/eu_mrl_apply_report_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/eu_mrl_null_worklist_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/manual_entry_ledger_eu_mrl_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/concordance_rebuild_phase1_report_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/concordance_rebuild_phase2_report_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/codex_group_to_hs_heading_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/concordance_phase3_finalize_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/concordance_phase3b_resolve_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/concordance_final_vn_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/vn_product_x_mrl_coverage_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/annex1_verification_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/annex1_verbatim_rows_vn_15_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/annex1_grep_hits_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/rasff_vietnam_density_scan_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/rasff_T4_product_x_year_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/rasff_T5_active_substances_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/panel_extend_vn_ak_reconcile_report_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/ak_rasff_reconciliation_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/Cam_Nang_Quan_Tri_Du_An_Va_Checklist_Audit.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/annex1_groundtruth_crosscheck_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/mrl_identifying_power_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/mrl_time_variation_diagnostic_RASFF_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/index_design_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/vn_stringency_index_variants_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/vn_change_natural_experiments_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/mard_registration_omega_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/omega_vn_registration_basket_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/omega_vn_national_fallback_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/index_weighted_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/vn_stringency_index_weighted_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/eventstudy_baci_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/baci_eventstudy_coefs_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/reproduce_audit_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/inventory_audit_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/reproduce_crosscheck_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/raw_evidence_crosstool_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/concordance_asean_finalize_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/concordance_final_asean_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/asean_mrl_panel_diag_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/asean_mrl_panel_2026-06-26.md
https://raw.githubusercontent.com/tranphu1508/XxX123/main/review_artifacts/asean_eventstudy_2026-06-26.md
