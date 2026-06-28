# Nhật ký lỗi & phát hiện audit (append-only, ghi ngày bên trong mỗi mục)

## YYYY-MM-DD — [Giai đoạn N] — <tiêu đề ngắn>
- File liên quan: <đường dẫn>
- Mô tả: <...>
- Mức nghiêm trọng: CAO / TRUNG BÌNH / THẤP
- Hành động: <...>
- Trạng thái: ĐANG XỬ LÝ / ĐÃ XỬ LÝ

## 2026-06-26 — [Tổ chức thư mục] — Gom 14 thư mục 00_–13_ vào thư mục chứa
- File liên quan: eu_maximum_residue_level_asean_export_study/ (toàn bộ 14 thư mục 00_–13_)
- Mô tả: Đã di chuyển (move, không copy) 14 thư mục đánh số 00_–13_ kèm toàn bộ nội dung vào một thư mục chứa duy nhất eu_maximum_residue_level_asean_export_study/ ngay trong thư mục gốc lớn. Thực hiện khi các thư mục còn rỗng dữ liệu (44 thư mục con, 18 file tài liệu), chưa có script/đường dẫn hard-code. Đối chiếu đếm trước/sau khớp: 00_=0 subdir/6 file, 07_=3/1, 11_=5/2; tổng 44 subdir/18 file không đổi.
- Lý do: Tách khung dự án hiện hành khỏi các thư mục thử nghiệm cũ (Reading, Version 1, Version 2, Xây dựng biến, Ý tưởng ban đầu) cho gọn và khớp cấu trúc Phần 1 cẩm nang.
- Cấu trúc trước → sau: [gốc]/00_…13_ nằm rời rạc, lẫn thư mục cũ  →  [gốc]/eu_maximum_residue_level_asean_export_study/00_…13_ gom một chỗ; 5 thư mục cũ giữ nguyên tại gốc.
- Mức nghiêm trọng: THẤP
- Hành động: Tạo container → move 14 thư mục → xác minh đếm trước/sau → cập nhật readme_project_overview.md và Phần 1 cẩm nang.
- Trạng thái: ĐÃ XỬ LÝ

## 2026-06-26 — [Giai đoạn 0] — BACI vintage diff: không có bản cũ để đối chiếu
- File liên quan: 02_data_collection_and_api_scripts/validation_reports/baci_validation_2026-06-26.md
- Mô tả: Bước 3 (diff vintage cũ↔mới) KHÔNG thực hiện được vì chỉ có một vintage BACI trên máy (HS12 V202601, tại Version 1 & Version 2); không có release cũ hơn (vd 202401/202501) để định lượng độ nhạy theo vintage. Bản gốc đã dùng cũng chính là 202601.
- Mức nghiêm trọng: THẤP
- Hành động: Nếu cần đánh giá độ nhạy vintage, cung cấp một release BACI cũ hơn để so trên phạm vi HS 07–10; nếu không, ghi giới hạn này vào mục Hạn chế.
- Trạng thái: ĐANG XỬ LÝ

## 2026-06-26 — [Giai đoạn 0] — Ràng buộc HS revision: BACI HS12 ↔ concordance EU (folder 03)
- File liên quan: 03_concordance_product_code_to_harmonized_system_six_digit/ (chưa dựng); 00_project_documentation/analytical_decisions_log.md
- Mô tả: BACI đóng băng theo HS12 (HS2012). Concordance product_code→HS6 phía EU phải dùng HS6 revision 2012 để khớp. Folder 03 chưa dựng trong khung mới; revision phía EU chưa xác nhận. Nếu EU dùng HS2017/HS2022 → cần bắc cầu revision, nếu không sẽ lệch mã khi merge (folder 06).
- Mức nghiêm trọng: TRUNG BÌNH
- Hành động: Khi dựng folder 03, xác nhận & ghi rõ HS revision; nếu lệch HS12 thì thêm bước concordance HS2012↔HS20xx. Cần người dùng xác nhận (Bước 6).
- Trạng thái: ĐANG XỬ LÝ

## 2026-06-26 — [Giai đoạn 0] — EU MRL: khóa (chất×sản phẩm×ngày áp dụng) KHÔNG duy nhất
- File liên quan: 02_data_collection_and_api_scripts/validation_reports/eu_mrl_validation_2026-06-26.md
- Mô tả: Trên snapshot 2026-05-27 (519.650 record), khóa (pesticide_residue_id, product_code, application_date) có 88.337 dòng trùng — cùng tổ hợp xuất hiện dưới nhiều regulation/Annex với applicability khác nhau (vd vừa "Applicable" Annex III vừa "No longer applicable" Annex II). KHÔNG phải hỏng dữ liệu.
- Mức nghiêm trọng: TRUNG BÌNH
- Hành động: Khi dựng EU MRL panel (folder 04), dùng khóa đầy đủ (thêm regulation_number + included_in_annex) và logic chọn dòng "đang áp dụng" theo thời điểm; không dedup ngây thơ.
- Trạng thái: ĐANG XỬ LÝ

## 2026-06-26 — [Giai đoạn 0] — EU MRL: 30.343 dòng MRL null
- File liên quan: 02_data_collection_and_api_scripts/validation_reports/eu_mrl_validation_2026-06-26.md
- Mô tả: 30.343 dòng có mrl_value/mrl_value_only = null (đa phần Annex II/III, applicability "Applicable"). Khác với 73.030 dòng "No MRL required" (=Annex IV, hợp lệ). Null cần quyết cách xử lý khi dựng biến treatment.
- Mức nghiêm trọng: THẤP
- Hành động: Ở bước dựng treatment (04), quyết định: loại / impute / coi là thiếu; ghi rõ.
- Trạng thái: ĐANG XỬ LÝ

## 2026-06-26 — [Giai đoạn 0] — EU MRL: chẩn đoán tie & null (in-scope) + đề xuất quy tắc
- File liên quan: 04_maximum_residue_level_panel/eu_mrl_key_null_resolution_proposal_2026-06-26.md
- Mô tả: Scoping HS07–10×A_k: tie in-scope 22.195 khóa, null in-scope 579. Sau lọc Applicable+latest-date: tie dư 11.726 cặp nhưng **0 xung đột giá trị MRL** (chỉ trùng across-annex cùng giá trị). Null ràng buộc thật = **40 (chất×sp)** có Applicable mới nhất null (TRỐNG THẬT trong API, không parse-error; giá trị ở CELEX). CELEX live không trích được ở môi trường này (EUR-Lex JS, không có Chrome).
- Mức nghiêm trọng: cập nhật — tie hạ THẤP (không xung đột giá trị); null 40 ca TRUNG BÌNH.
- Hành động: đã đề xuất 3 quy tắc (a)(b)(c) trong proposal; CHỜ chốt trước khi dựng panel.
- Trạng thái: ĐANG XỬ LÝ (chờ chốt quy tắc)

## 2026-06-26 — [Apply] EU MRL: panel ràng buộc dựng xong (cập nhật cờ tie/null)
- File liên quan: 04_maximum_residue_level_panel/eu_mrl_apply_report_2026-06-26.md
- Mô tả: Áp rule a (bậc thang toàn-bộ-bản-ghi) + b + c. Khóa (chất,sp,năm) DUY NHẤT (trùng=0). Kiểm chứng: bậc thang đổi đúng năm, không mất lịch sử (vd Fenamidone rớt 60→0.01). Cập nhật: tie-break (b) xử 909 cell (93 ngày xung đột across-annex) — đã giải quyết. Null pending = 420 bản ghi (43 current ≈ ước lượng 40 cũ, 377 historical) — phương pháp toàn-bộ-bản-ghi lộ thêm null lịch sử.
- PHÁT HIỆN MỚI: not_yet_set = 24,2% cell (139.699) — tổ hợp chưa liệt kê → cần fill default 0,01 (Art 18 Reg 396/2005) ở bước treatment. Không phải lỗi panel.
- Mức nghiêm trọng: tie THẤP (đã xử); null pending TRUNG BÌNH (worklist 420, ưu tiên 43 current); default-0.01 fill = cờ cho bước treatment.
- Hành động: tra CELEX 420 ca (ưu tiên 43 current) → ledger; bước treatment fill default 0,01 cho not_yet_set.
- Trạng thái: ĐANG XỬ LÝ (panel ship được; pending 420 + default-fill chờ bước sau)

## 2026-06-26 — [Concordance] HS revision MEDIUM flag → ĐANG GỠ
- File liên quan: 03_concordance_product_code_to_harmonized_system_six_digit/concordance_rebuild_phase1_report_2026-06-26.md
- Mô tả: Rebuild concordance EU→HS6 neo HS2012 qua metadata BACI HS12 đóng băng; referential 0 lỗi (mọi HS6 ứng viên ∈ BACI). Cờ MEDIUM "HS revision concordance" (mở từ task BACI) ĐANG GỠ. Phase 1: auto_accept 59, needs_review 96 (21 OLD_DISAGREE), nhóm 62, n.e.c. 47, ngoài-scope 88, không-khớp 29.
- Mức nghiêm trọng: HẠ TRUNG BÌNH → THẤP (đã neo HS2012).
- Hành động: duyệt decision_table (Phase 2) → chốt concordance + ĐÓNG cờ.
- Trạng thái: ĐANG XỬ LÝ (Phase 1 xong, chờ duyệt)

## 2026-06-26 — [Concordance Phase 2] HS revision flag ĐANG GỠ (neo Codex + tên khoa học)
- File liên quan: 03_concordance_product_code_to_harmonized_system_six_digit/concordance_rebuild_phase2_report_2026-06-26.md
- Mô tả: Neo concordance vào tên khoa học + nhóm Codex CCPR → heading HS2012 (mỏ neo 60 dòng, verify 60/60) + đa-phiếu hội tụ. verified_high 84 (có trích dẫn), needs_confirm 30, arbitration 60, nhóm 85, ngoài-neo 75, n.e.c. 47. SỬA đúng lỗi fuzzy Phase 1 (wheat→1001, cassava→0714, spinaches→070970, melons→0807). Referential 0 lỗi; coverage in-scope 95%. Nguồn ngoài (Codex PDF/HS-EN/Fiankor) không kéo được → neo bằng loài + text heading HS2012 local.
- Mức nghiêm trọng: THẤP (đã neo HS2012 chắc; chờ duyệt residual + finalize).
- Hành động: duyệt residual + quyết phạm vi tươi/chế biến → finalize concordance → ĐÓNG cờ HS revision.
- Trạng thái: ĐANG XỬ LÝ (Phase 2 xong, chờ duyệt)

## 2026-06-26 — [RASFF] Mật độ VN crop-pesticide ĐỦ (gộp) + 2 phát hiện thiết kế
- File liên quan: 02_data_collection_and_api_scripts/rasff_feasibility_scan/rasff_vietnam_density_scan_2026-06-26.md
- Mô tả: Reproduce KHỚP 328 vụ / 180 border (Route B, 2 file user). Verdict ĐỦ (gộp): chạy được mô hình đếm GỘP (product FE + year FE + offset enhanced-control); KHÔNG đủ product×year chi tiết (chỉ 1 ô ≥20). 2 phát hiện: (a) carbendazim DẪN ĐẦU hoạt chất gây rejection của VN (≠ bộ 5 chất nghiên cứu khác) → A_k & chỉ số MRL phải neo theo hoạt chất thực tế VN; (b) nội sinh cường-độ-kiểm-tra hiện rõ (ớt 2024, sầu riêng 2023–24 vọt trùng enhanced-control Reg 2019/1793) → bắt buộc offset.
- Mức nghiêm trọng: TRUNG BÌNH (ảnh hưởng thiết kế A_k + ước lượng).
- Hành động: khi thiết kế chỉ số/panel — neo A_k theo hoạt chất VN; đưa cờ enhanced-control làm offset; RASFF = trụ bổ trợ (không phải minh hoạ suông).
- Trạng thái: ĐANG XỬ LÝ (chờ Claude xác nhận trước khi thiết kế panel)

## 2026-06-26 — [Concordance/Index] CỜ VÀNG: 6 mã VN có MRL nhưng chưa vào A_k/panel
- File liên quan: 03_/outputs/vn_product_x_mrl_coverage_2026-06-26.csv; concordance_phase3b_resolve_2026-06-26.md
- Mô tả: Đối chiếu panel MRL (04_): 6 mã EU lát VN — thanh long 0162040, vải/nhãn 0162020, chanh leo 0162030, đậu bắp 0231040, parsley 0256040, basil 0256080 — CÓ MRL trong snapshot đóng băng (~691 chất) NHƯNG KHÔNG nằm trong A_k/panel (04_). Index sẽ rỗng MRL ở các sản phẩm này (gồm thanh long #2 RASFF) cho tới khi A_k mở rộng. Ớt cay 0231020 (#1) đầy đủ — KHÔNG đỏ.
- Mức nghiêm trọng: TRUNG BÌNH (ảnh hưởng độ phủ chỉ số ở sản phẩm VN nóng).
- Hành động: Bước thiết kế chỉ số/dựng panel — MỞ RỘNG A_k để gồm 6 mã VN này. KHÔNG đụng 05_/04_ ở task concordance.
- Trạng thái: ĐANG XỬ LÝ (chờ bước A_k/index)

## 2026-06-26 — [Concordance/Annex I] Rambutan XÉT LẠI: 0163060 (Cherimoyas) không 0162020
- File liên quan: 03_/annex1_verification_2026-06-26.md; outputs/annex1_verify/grep_hits.txt
- Mô tả: Verify Annex I (catalogue taxonomy): grep "rambutan" cho thấy rambutan là synonym của **0163060 'Cherimoyas'** (nhóm 0163 lớn-vỏ-không-ăn), KHÔNG phải 0162020 (litchi/longan). Phase 3b từng gộp longan+rambutan vào 0162020. HS6 cả hai = 081090 nhưng nguồn MRL khác (longan=0162020, rambutan=0163060). Thanh long (0162040), longan (0162020), ớt cay (0231020) XÁC NHẬN theo catalogue. Legal Annex I (EUR-Lex) CHƯA kiểm (bị chặn).
- Mức nghiêm trọng: THẤP (rambutan không top-3 VN; HS6 081090 không đổi; chỉ khác nguồn MRL).
- Hành động: Claude quyết rambutan → 0163060; legal text user mở tay nếu cần.
- Trạng thái: ĐANG XỬ LÝ (chờ Claude)

## 2026-06-26 — [RESOLVED Bước 0] Rambutan tách 0162020 → 0163060 (đã sửa concordance)
- File liên quan: 03_/outputs/concordance_final_vn_2026-06-26.csv (+ .bak_before_rambutan_2026-06-27)
- Mô tả: Theo verify Annex I, đã SỬA: thêm dòng 0163060 'Cherimoyas' (chôm chôm/rambutan, synonym nguyên văn 'Rambutans/hairy litchis') → HS6 081090; note 0162020 chỉ còn longan/litchi. Lát VN nay 16 mã/27 dòng.
- Mức nghiêm trọng: THẤP → ĐÃ ĐÓNG.
- Trạng thái: ĐÃ XỬ LÝ (Bước 0 task panel-extend).

## 2026-06-26 — [RESOLVED Phần A] 6 mã VN cờ VÀNG đã vào panel (mở rộng A_k 515 chất)
- File liên quan: 04_/outputs/eu_mrl_binding_panel_vn_extended_{jan01,dec31}_2026-06-26.csv; vn_product_x_mrl_coverage (cập nhật)
- Mô tả: 7 mã (gồm 6 cờ vàng + 0163060 mới) đã build panel = 489 chất×10 năm, ngang 9 mã OK; thanh long #2 ĐỦ phủ. Builder kiểm chứng 50.750 ô khớp 0 sai. Khóa duy nhất, referential sạch.
- Mức nghiêm trọng: TRUNG BÌNH → cơ học ĐÃ ĐÓNG (độ phủ chất). A_k MEMBERSHIP vẫn chờ (xem dưới).
- Trạng thái: ĐÃ XỬ LÝ phần panel; A_k membership chờ Claude.

## 2026-06-26 — [PHÁT HIỆN Phần B] acetamiprid gây 21 rejection nhưng MISSING_FROM_A_k + không có MRL in-window
- File liên quan: 05_/ak_rasff_reconciliation_2026-06-26.csv
- Mô tả: acetamiprid (#6-7 RASFF, 21 vụ) KHÔNG trong A_k 515. Snapshot CHỈ có định nghĩa dư lượng REVISED 'Acetamiprid (R)' id=10, record sớm nhất 20/08/2025 (SAU cửa sổ 2015–2024) → 0 MRL ràng buộc in-window; định nghĩa CŨ không còn trong snapshot product records. dinotefuran trong A_k nhưng MRL null (pending_celex). 17/18 chất T5 trong A_k; 498/515 chất A_k không gây rejection VN.
- Mức nghiêm trọng: CAO (ảnh hưởng định nghĩa A_k → chỉ số treatment cho VN).
- Hành động: Claude quyết — (1) thêm acetamiprid vào A_k? (2) khôi phục MRL acetamiprid in-window từ định nghĩa cũ/CELEX. KHÔNG tự sửa A_k.
- Trạng thái: CHỜ CLAUDE (đầu vào quyết định nghĩa A_k).

## 2026-06-29 — [Concordance] — HS revision EU↔BACI HS2012: ĐÃ XÁC MINH KHỚP (giải cờ Giai đoạn 0)
- File liên quan: 03_/outputs/concordance_final_asean.csv; 01_raw_data_frozen/trade_data_baci/.../product_codes_HS12_V202601.csv (5.202 mã); 12_audit/concordance_hs_revision_fixes_2026-06-29.csv
- Mô tả: Đối chiếu TOÀN BỘ HS6 concordance với universe BACI HS2012 (5.202 mã). Kết quả: **136/137 mã atomic là HS2012 hợp lệ**; **panel ước lượng 125/125 KHỚP** (theo cấu trúc từ BACI). Quét semantic nhóm Annex I↔chương HS: melon/dưa hấu/cucurbit (nhóm 02) → chương 08 là ĐÚNG taxonomy HS, không phải lỗi.
- Mức nghiêm trọng: hạ từ TRUNG BÌNH → **THẤP** (revision khớp; merge BACI căn đúng).
- Hành động: cờ HS-revision GIẢI. Hai lỗi map còn lại tách sang mục dưới.
- Trạng thái: ĐÃ XỬ LÝ (HS-revision); 2 lỗi map → mục kế.

## 2026-06-29 — [Concordance] — 2 lỗi ánh xạ EU→HS6 (đều từ auto_sci_name/needs_review_noanchor)
- File liên quan: 03_/outputs/concordance_final_asean.csv; 04_/outputs/asean_mrl_panel.csv; 07_/asean_baci_panel.csv; 12_audit/concordance_hs_revision_fixes_2026-06-29.csv
- Mô tả:
  1. **0402020 "Oil palm kernels" → 151010 SAI**: 151010 không tồn tại trong HS2012 (heading 1510 chỉ có 151000 dầu ô liu n.e.c.). Đúng = **120710** (palm nuts and kernels). Tác động: MRL panel 13 dòng, **analysis panel 0** (rớt vì BACI không có 151010) → vô hại estimation, nhưng concordance sai.
  2. **0401090 "Cotton seeds" → 520100 SAI**: 520100 = **xơ bông** (chương 52, NGOÀI phạm vi 07–12), trong khi hạt bông là oilseed. Đúng = **120721** (cotton seeds). Tác động: **analysis panel 2.340 dòng = 0,12% kim ngạch (0,031% đi-EU)** → **nhiễm panel ước lượng bằng mã ngoài phạm vi**. Nhỏ về trọng số (PPML value-weighted) nhưng sai bản chất + reviewer dễ bắt "vì sao HS52 trong panel nông sản".
- PHÁT HIỆN HỆ THỐNG: cả 2 lỗi đều do **auto_sci_name (khớp tên khoa học, không neo)** → 22 mã auto_sci_name + ~95 mã needs_review là rổ rủi ro nhất, cần soi semantic từng mã (chưa làm).
- Mức nghiêm trọng: palm THẤP (rớt); cotton **TRUNG BÌNH** (nhiễm panel + ngoài phạm vi).
- Hành động: (a) sửa concordance 151010→120710, 520100→120721; (b) **loại 520100 khỏi panel** (hoặc thay 120721 nếu cotton seed trong phạm vi) → cần rebuild panel từ BACI; (c) soi 22 auto_sci_name + needs_review. CHỜ user chốt phạm vi (oilseed bông/cọ có thuộc bài nông-sản-rau-quả không) trước khi rebuild.
- Trạng thái: ĐANG XỬ LÝ (bản vá sẵn; chờ quyết phạm vi + rebuild)

## 2026-06-29 — [Concordance] — ESCALATION: rổ flagged sai hệ thống (≥12 lỗi, có mã giá trị lớn)
- File liên quan: 03_/outputs/concordance_final_asean.csv; 12_audit/concordance_confirmed_errors_2026-06-29.csv
- Mô tả: Soi 2 rổ flagged → tỉ lệ lỗi CAO:
  - **auto_sci_name (22 mã): 8 lỗi (36%)** — hạt dầu gán lộn HS6 (mè→thầu dầu 120730, cải dầu→mè 120740, rum→bông 120721, anh túc→cải dầu 120510, kapok→ÓC CHÓ 080232, quả cọ→Ô LIU 071120, borage/camelina→sai). Tất cả chương 12 oilseed, kim ngạch ~0,08% panel → ảnh hưởng β không đáng kể.
  - **needs_arbitration (mẫu): ≥4 lỗi, 2 GIÁ TRỊ LỚN** — lựu+mãng cầu → 080390 (CHUỐI, 8% panel); su hào → 071410 (SẮN, 6% panel); hạt thông → 080112 (DỪA). Lưu ý: chuối (0163020 verified_high) và sắn (0212010) VẪN map đúng vào chính mã đó → lỗi **làm bẩn rổ weakest-link stringency** của mã chuối/sắn (thêm chất của lựu/mãng cầu/su hào), KHÔNG bịa mã. Mức méo stringency chưa lượng hóa (cần rebuild để đo).
- Trái lại: phần lớn "nghi vấn" giá trị lớn của heuristic là **umbrella HỢP LỆ** (081090 trái cây lạ, 121190 dược thảo, 0902 trà) — không phải lỗi, chỉ thô.
- Gradient tin cậy: verified_high / vn_finalized (tốt) > auto_hs6_present (phần lớn ổn) > **auto_sci_name / needs_arbitration (nhiều lỗi)**.
- Mức nghiêm trọng: **TRUNG BÌNH–CAO** (concordance chưa đáng tin ở rổ flagged; ảnh hưởng estimation: nhỏ về giá trị nhưng méo stringency mã lớn chưa rõ).
- Hành động: (a) đã lưu 12 lỗi xác nhận; đã vá 2 (cotton/palm kernel); (b) cần **tái-giải hệ thống rổ flagged** (auto_sci_name 22 + needs_arbitration 60 + needs_review ~95) bằng map Annex-I-species→HS2012 có bằng chứng nguyên văn; (c) rebuild panel + đo lại stringency chuối/sắn. CHỜ user chốt mức làm.
- Trạng thái: ĐANG XỬ LÝ (đã lập danh sách lỗi; chờ user chốt tái-giải hệ thống + rebuild)

## 2026-06-29 — [Concordance] — Soi 100% 381 mã: phân loại cuối + đính chính số thổi phồng
- File: 12_audit/CONCORDANCE_AUDIT_SUMMARY_2026-06-29.md + concordance_full_review_classified_2026-06-29.csv
- Kết quả cuối: OK 168 | NO_HS6 97 | UMBRELLA/multi 38 | LUMPING 53 | catchall 20 | ERROR ~12–15.
- ĐÍNH CHÍNH: số "130 flag" trung gian do detector thô; 44 là FALSE-FLAG (thực ra ĐÚNG). Lỗi thật ~12–15 (đã liệt kê), + vấn đề phương pháp lumping 53 ca (19 mã panel) chọn mã đại diện cụ thể thay vì n.e.c.
- Mức nghiêm trọng: lỗi map TRUNG BÌNH (đa số rìa; banana/cassava stringency cần đo); lumping = quyết định thiết kế (user).
- Trạng thái: ĐANG XỬ LÝ — chờ user quyết tái-neo lumping + cho rebuild để đo méo.

## 2026-06-29 — [Concordance] — ĐO MÉO: lỗi+lumping VÔ HẠI với β; đã vá 14 lỗi
- File: 12_audit/concordance_distortion_betatest_2026-06-29.txt; measure_distortion_2026-06-29.py
- Đo: chạy M1 trên panel hiện có (KHÔNG rebuild BACI). Baseline tái lập khớp (S1 −1,4685; S2 +0,1488). Loại 31 mã ERROR+LUMPING (24,8% dòng) → S1 −1,3811 (lệch ~6%, cùng dấu/ý nghĩa), S2 +0,1410 (≈không đổi).
- KẾT LUẬN: lỗi concordance + lumping **không làm đổi kết quả** (PPML weighted theo kim ngạch; lỗi ở mã trọng số nhỏ / chỉ trộn stringency). β chính đứng vững.
- Hành động: đã VÁ 14 lỗi vào concordance (2 HS-rev + 12 thay-thế: oilseeds, lựu/mãng cầu→081090, su hào→071490, hạt thông→080290, cải ngựa→070690...). 2 ca borderline (quả cọ, nguyệt quế) gắn cờ REVIEW. Tái-neo 53 lumping = KHÔNG đáng cho kết quả → ghi Limitations thay vì sửa. Panel CHƯA rebuild (theo user).
- Mức nghiêm trọng: hạ THẤP (kết quả robust; concordance đã dọn phần lõi lỗi).
- Trạng thái: ĐÃ XỬ LÝ phần đo + vá; rebuild panel để áp 14 sửa = chờ user (khi nào muốn bản panel sạch tuyệt đối).

## 2026-06-29 — [Concordance] — Re-xem lumped: +4 mis-lump (sản phẩm CÓ mã riêng) + xác minh literature
- File: 12_audit/concordance_certification_inpanel_2026-06-29.csv
- Phát hiện: phân biệt LUMP HỢP LỆ (không có mã riêng → gộp, CHUẨN theo Ferro2015/Shingal2024) vs MIS-LUMP (có mã riêng nhưng gộp nhầm dưới mã sản phẩm khác = LỖI). Sửa 4: nutmeg 090921→090811; vanilla 090821→090510; anise 090921→090961; liquorice 091030→121190. Cờ REVIEW 2: celery-seed (810030), palm-hearts (270090).
- Bằng chứng literature (đọc trực tiếp): Ferro(2015) "matched 243 agricultural products to HS6... aggregate to match trade data"; Shingal(2024) "each product mapped to HS6". → product→HS6 aggregation CHUẨN; nhưng lump-dưới-mã-sai KHÔNG chuẩn (đã sửa).
- ĐÍNH CHÍNH: phán "lumping = chuẩn, vô hại" của Cowork quá lỏng — đúng cho lump-không-có-mã-riêng, SAI cho 4 ca mis-lump trên.
- Tổng đã sửa session: 20 mã. β vẫn vô hại (mã trọng số nhỏ).
- Trạng thái: ĐANG XỬ LÝ (còn 2 borderline + 158 mã ngoài-panel + lump hợp lệ ghi Limitations).
