# 📋 PLAN — Đưa concordance EU→HS6 về ĐÚNG 100% (mở đầu 2026-06-29)

> **KỶ LUẬT:** File này là kim chỉ nam. Cho tới khi MỌI mã 381 được chứng nhận + panel rebuild khớp + β bản sạch xác nhận, **KHÔNG trôi sang việc khác** (viết bài / tách thước đo / việc mới) — nếu user không chỉ đạo khác. Mỗi lần làm xong 1 mục, cập nhật mục "TIẾN ĐỘ" cuối file.

## 🎯 MỤC TIÊU
Toàn bộ **381 mã EU** (Annex I Reg (EU) 2018/62) → **HS6 revision HS2012** (khớp BACI) được **kiểm chứng từng mã** bằng bằng chứng nguyên văn từ ≥2 nguồn; panel rebuild khớp concordance đã sửa; chạy lại β xác nhận.

## 🔬 PIPELINE KIỂM CHỨNG TỪNG MÃ (bắt buộc — đa nguồn, có bằng chứng)
Với mỗi mã EU, kết hợp 3 nguồn:
1. **Pháp lý EU (sản phẩm LÀ GÌ + loài Latin):** Annex I Reg (EU) 2018/62.
   - Gốc: `01_raw_data_frozen/eu_annex1_legal/L_2018018EN.01000101.xml.html`
   - Parsed (tra nhanh theo mã/loài): `01_raw_data_frozen/eu_annex1_legal/annex1_species_to_code.csv` (1.305 dòng; khóa parent_code+sub_code)
2. **Nomenclature đích (HS2012):** `01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601/product_codes_HS12_V202601.csv` (5.202 mã; cột `code`,`description`).
3. **Nguồn ngoài đã xác thực (bắc cầu loài→HS khi không hiển nhiên):** web search CHỈ nguồn chính thống — WCO HS Explanatory Notes/Nomenclature; FAO/FAOSTAT; Codex Alimentarius (CCPR classification of food); EU TARIC / EUR-Lex. Ghi URL.
- **Bằng chứng mỗi mã (1 dòng):** eu_code | tên+loài (nguồn 1, dòng) | HS6 chọn + mô tả HS2012 (nguồn 2) | URL nguồn 3 xác nhận | verdict (OK/SỬA: cũ→mới).

## 🙋 KHI CẦN USER ĐỐI CHIẾU — phải nói RÕ
User không chắc tên khoa học → Cowork **search hộ**, user chỉ đối chiếu. Khi cần user xem, ghi đủ: **(a) tên file, (b) đường dẫn đầy đủ, (c) hàng/dòng số mấy, (d) cách so khớp, (e) nguồn để khớp**.

## 🗂️ CÁC NHÓM VIỆC
### Nhóm A — đóng lỗi đã biết
- **A1** Chốt 2 borderline: `402030` quả cọ tươi, `256090` nguyệt quế/bay leaves (đang dính mã ô liu sai).
- **A2** Rebuild panel áp 14 sửa (giải nén BACI) → chạy lại β bản sạch + tính lại stringency chuối/sắn.
### Nhóm B — chứng nhận từng mã
- **B3** Soi tay 125 mã "OK" in-panel tới 6 số (rồi 43 mã OK ngoài panel).
- **B4** Xác nhận 97 mã NO_HS6 loại đúng (động vật/nec, không bỏ sót cây).
- **B5** Kiểm 20 catch-all "Others(2)" + 38 umbrella/đa-mã (cà phê 0901xx, gạo 1006xx tách đúng; 081090/121190 gộp chủ đích).
### Nhóm C — phương pháp + minh bạch
- **C6** Quyết 53 lumping: tái-neo về mã n.e.c. (vd 070999) HAY giữ + ghi Limitations (đã đo vô hại).
- **C7** Chạy ppmlhdfe `.do` lấy SE trọng tài.
- **C8** Phụ lục concordance 381 mã + bằng chứng cho replication.

## ✅ ĐÃ XONG (2026-06-29)
- Soi 100% phân loại: 168 OK / 97 NO_HS6 / 38 umbrella+multi / 53 lumping / 20 catchall / ~12–15 lỗi. (`12_audit/concordance_full_review_classified_2026-06-29.csv`)
- Vá **14 lỗi** vào file concordance (panel CHƯA rebuild). (`12_audit/concordance_confirmed_errors_2026-06-29.csv`)
- Đo méo: lỗi+lumping **vô hại với β** (loại 24,8% dòng → S1 −1,47→−1,38, S2 ≈không đổi). (`12_audit/concordance_distortion_betatest_2026-06-29.txt`)
- Backup: `03_/outputs/concordance_final_asean_pre_hsfix_2026-06-29.csv`.

## 📍 TIẾN ĐỘ (cập nhật mỗi bước)
- [2026-06-29] A1 XONG: chốt 402030→120799, 256090→091099 (bằng chứng đa-nguồn, 16 mã tổng đã sửa). Đang ở **A2 (rebuild)**.
- [2026-06-29] A2 CHẶN: script build gốc của asean_baci_panel + asean_mrl_panel KHÔNG có trong file (phiên trước không lưu). File BACI lọc sẵn chỉ EU (25 đích) — KHÔNG đủ dựng panel đa phương 52 đích. Rebuild faithful cần: (a) script gốc HOẶC (b) giải nén BACI 1.27GB + tái lập logic (52-đích/balance/weakest-link) + VALIDATE tái tạo đúng panel cũ trước khi áp sửa. β đã đo là robust → rebuild chỉ để dữ-liệu-sạch, không đổi kết quả. CHỜ user quyết (a/b/defer).
- [2026-06-29] CHỐT THỨ TỰ (user): concordance ĐÚNG 100% TRƯỚC, panel rebuild CUỐI CÙNG (panel phái sinh từ concordance). A2 HOÃN tới sau Nhóm B+C. Đang làm **Nhóm B — chứng nhận từng mã** (pipeline đa-nguồn).
- [2026-06-29] B (in-panel) XONG soi: 223 EU→panel. CHỨNG NHẬN ĐÚNG ~145 (122 strong + 19 umbrella + 4 false-flag) + 16 đã sửa; còn lại = gộp/nhóm-cha/catch-all (thô, KHÔNG lỗi, đã đo vô hại). KHÔNG lỗi map mới. Bằng chứng: 12_audit/concordance_certification_inpanel_2026-06-29.csv. CÒN: (B) 158 mã ngoài-panel; (C6) quyết lumping; (C7) arbiter SE; (C8) phụ lục. Panel rebuild = CUỐI.
- [2026-06-29] Re-xem lumped: +4 mis-lump SỬA (nutmeg/vanilla/anise/liquorice — có mã riêng, gộp nhầm). Đính chính: lump-không-có-mã-riêng=CHUẨN (Ferro2015/Shingal2024 đã đọc xác minh); mis-lump=LỖI. Tổng 20 mã sửa. Còn: 2 borderline (celery-seed/palm-hearts), 158 mã ngoài-panel (user muốn chứng nhận đủ 381), lump hợp lệ→Limitations.
- [2026-06-29] B XONG soi 100% 381 mã: sửa ~26 lỗi + tái-neo ~26 lump ngoài-panel. KIỂM CUỐI: 0 lỗi map còn lại; chỉ 10 lumping in-panel gộp-cùng-họ HỢP LỆ (chuẩn Ferro/Shingal→Limitations). Cert: 12_audit/CONCORDANCE_CERTIFICATION_FINAL_2026-06-29.md. CÒN: C6 (chốt 10 lump), C7 (arbiter SE), C8 (phụ lục), A2 rebuild CUỐI.
