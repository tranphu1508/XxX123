# Handoff — 2026-06-26 — Annex I verify mã VN (bằng chứng thô) — đã DỪNG

## 1. Metadata
- Ngày: 2026-06-26. Trạng thái: verify xong (bằng chứng thô); ĐÃ DỪNG chờ Claude đọc + quyết rambutan.
- Task: "Verify phân loại Annex I cho mã VN — xuất bằng chứng nguyên văn, KHÔNG kết luận thay".

## 2. Đã làm gì + SỐ CHÍNH
- Nguồn Annex I: **A** (SANTE products taxonomy = frozen catalogue, đủ trường) ✓; **B** EUR-Lex pháp lý **BỊ CHẶN** (web_fetch CELEX:32018R0062 rỗng) → **C** URL cho user mở tay.
- Verbatim 15 mã VN (annex1_verify/) + grep TOÀN catalogue 3 cụm chuỗi (pitaya/dragon, longan/rambutan, chili) → mọi mã+dòng.
- **Phán định (theo catalogue):** 0162040 thanh long **XÁC NHẬN** (pitaya/dragon CHỈ ở 0162040; hit 0632010 là từ "dragon" thảo mộc); 0162020 longan **XÁC NHẬN**; **rambutan XÉT LẠI** (là synonym của **0163060 Cherimoyas**, KHÔNG phải 0162020 → MRL khác); 0231020 ớt cay **XÁC NHẬN** (không mã ớt-cay riêng).
- KHÔNG sửa concordance. Mọi XÁC NHẬN chỉ theo catalogue; **legal Annex I CHƯA KIỂM** (EUR-Lex chặn).

## 3. Cấu trúc — thay đổi
- THÊM: `03_/outputs/annex1_verify/` (annex1_taxonomy_vn JSON + verbatim_rows_vn_15.txt + grep_hits.txt); `03_/annex1_verification_2026-06-26.md`.
- SỬA: `11_/issues_log.md` (rambutan XÉT LẠI). review_artifacts: +annex1 report + verbatim + grep.

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Xuất bằng chứng THÔ (verbatim + grep) để Claude tự đọc/phán định, KHÔNG kết luận thay.
- EUR-Lex chặn → dùng A (catalogue = Annex I máy-đọc) + C (URL user cho legal text).
- Phát hiện rambutan khác mã (0163060) → XÉT LẠI, đề xuất, chờ Claude (không tự sửa).

## 6. Cờ cần review
- **Rambutan → 0163060** (Cherimoyas) thay vì 0162020 — Claude quyết (MRL khác; HS6 081090 không đổi).
- Legal Annex I (EUR-Lex) chưa kiểm — user mở tay nếu cần (URL trong report §C).

## 7. Con trỏ bằng chứng
- `03_/annex1_verification_2026-06-26.md`; `outputs/annex1_verify/` (annex1_taxonomy_vn JSON, verbatim_rows_vn_15.txt, grep_hits.txt).
