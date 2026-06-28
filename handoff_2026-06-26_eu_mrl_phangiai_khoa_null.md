# Handoff — 2026-06-26 — EU MRL: phân giải khóa trùng (88k) & null (30k) — ĐỀ XUẤT (đã DỪNG)

## 1. Metadata
- Ngày: 2026-06-26
- Task: "EU MRL: phân giải khóa trùng & null — chẩn đoán + đề xuất + soi CELEX, DỪNG chờ xác nhận".
- Trạng thái: HOÀN TẤT chẩn đoán + đề xuất; **ĐÃ DỪNG — chưa dựng panel resolved**, chờ chốt 3 quy tắc.

## 2. Đã làm gì + SỐ CHÍNH
- Đọc từ frozen snapshot (KHÔNG sửa 01_); output ở 04_.
- Scoping HS07–10×A_k (concordance_EU_HS6_v3 + A_k_members): in-scope **57.957 cặp; 515 hoạt chất; 96 sản phẩm**.
- **TIE:** 80.406 khóa trùng (= 88.337 dòng dư); in-scope 22.195. Sau lọc Applicable+latest-date: **11.726 cặp dư nhưng 0 xung đột giá trị MRL** (trùng across-annex CÙNG giá trị) → tie-break vô hại.
- **NULL:** 30.343 tổng; in-scope 579; **ràng buộc thật 40 (chất×sp)** (Applicable mới nhất null). Record thô: TRỐNG THẬT (mọi trường value null), KHÔNG parse-error; giá trị nằm ở CELEX (reg 2018–2024).
- **CELEX:** URL trỏ regulation thật; trích trực tiếp KHÔNG được ở môi trường này (EUR-Lex JS, không có Chrome) → tra 40 ca thủ công / EUR-Lex backfill.
- **Đề xuất 3 quy tắc:** (a) Applicable + latest ≤ 1/1/t; (b) dedup giá trị → ưu tiên Annex II>III>V (vô hại vì 0 xung đột); (c) null: CELEX/carry 40 ca, drop+cờ chỉ khi không khôi phục (≈0,07%).

## 3. Cấu trúc — thay đổi
- THÊM: `04_/eu_mrl_key_null_resolution_proposal_2026-06-26.md` (+ bản sao `review_artifacts/`).
- SỬA: `11_/issues_log.md` (+1 mục chẩn đoán).
- KHÔNG đụng 01_; KHÔNG dựng panel.

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Scoping TRƯỚC → thu nhỏ vấn đề (null 30k → 579 → 40 ràng buộc).
- Không tự áp quy tắc consequential → chỉ đề xuất, DỪNG.
- CELEX không trích được trong môi trường → ghi nhận trung thực; đề xuất tra 40 ca có chọn lọc.

## 6. Cờ cần review (chờ người dùng/Claude chốt)
- (a) mốc-năm-t = 1/1/t hay 31/12/t.
- (b) phá hòa: Annex II>III>V + dedup (khuyến nghị) vs min-MRL (bảo thủ) — vô hại vì 0 xung đột.
- (c) 40 null: CELEX/carry (khuyến nghị) vs drop+cờ vs impute 0,01.
- issues_log: mục chẩn đoán 2026-06-26.

## 7. Con trỏ bằng chứng
- Proposal: `04_/eu_mrl_key_null_resolution_proposal_2026-06-26.md` (+ `review_artifacts/`).
- Phát hiện: `11_/issues_log.md`.
