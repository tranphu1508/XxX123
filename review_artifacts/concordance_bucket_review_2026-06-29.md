# Handoff — 2026-06-29 — Soi rổ flagged concordance (auto_sci_name + needs_review)

## 1. Metadata
- Ngày: 2026-06-29 | Cowork (đọc trực tiếp). Tiếp nối audit HS-revision.
- Trạng thái: **HOÀN TẤT soi mẫu. Phát hiện rổ flagged SAI hệ thống (≥12 lỗi). Chờ user chốt mức tái-giải + rebuild.**

## 2. Đã làm
- Vá 2 mã (đã backup concordance): 0401090 cotton 520100→120721; 0402020 palm kernel 151010→120710. **Panel chưa đụng (theo user).**
- Soi rổ auto_sci_name (22) + needs_review/arbitration/confirm (228).

## 3. Kết quả — gradient tin cậy concordance
| Rổ | Cỡ | Đánh giá |
|---|---|---|
| verified_high + vn_finalized | ~100 | Tin cậy (spot-check banana/durian/dragonfruit ĐÚNG) |
| auto_hs6_present | 156 | Phần lớn ổn (umbrella 081090/121190/0902 HỢP LỆ, chỉ thô) |
| **auto_sci_name** | 22 | **8 LỖI (36%)** — hạt dầu lộn mã |
| **needs_arbitration** | 60 | **≥4 lỗi mẫu, 2 GIÁ TRỊ LỚN** |

## 4. Lỗi xác nhận (12) — `12_audit/concordance_confirmed_errors_2026-06-29.csv`
- **Hạt dầu (8, ~0,08% KN → β gần như không đổi):** mè→thầu dầu, cải dầu→mè, rum→bông, anh túc→cải dầu, kapok→**óc chó**, quả cọ→**ô liu**, borage/camelina→nec.
- **Giá trị lớn (4):** lựu + mãng cầu → 080390 (**CHUỐI**, 8% panel); su hào → 071410 (**SẮN**, 6%); hạt thông → 080112 (**DỪA**).
  - Sắc thái: chuối (0163020 verified_high) + sắn (0212010) map ĐÚNG vào chính mã đó → lỗi **làm bẩn rổ weakest-link stringency** (thêm chất của lựu/su hào…), KHÔNG bịa mã/không thêm kim ngạch sai. Mức méo stringency **chưa đo** (cần rebuild).
- Umbrella lớn (081090/121190/0902) = HỢP LỆ, không phải lỗi.

## 5. Trả lời câu "concordance chuẩn chưa"
**Chưa.** Rổ flagged (auto_sci_name + needs_arbitration) sai hệ thống — ≥12 lỗi, gồm 2 mã lớn. NHƯNG: lõi giá trị (sầu riêng/thanh long/cà phê/gạo/tiêu/chuối/sắn) nằm ở verified_high và VẪN có mặt đúng; lỗi chủ yếu (a) oilseed kim ngạch ~0 hoặc (b) bẩn stringency mã lớn (mức chưa rõ). → kết quả β lõi **có thể vẫn vững**, nhưng concordance **phải dọn rổ flagged + đo lại stringency** mới đủ tin để công bố.

## 6. Đề xuất (CHỜ user)
1. **Tái-giải hệ thống** rổ flagged (~177 mã: auto_sci_name 22 + needs_arbitration 60 + needs_review ~95) — map Annex-I-species→HS2012 đúng, bằng chứng nguyên văn, theo cổng từng lô.
2. **Rebuild MRL panel + đo lại** stringency chuối/sắn trước/sau sửa → lượng hóa méo.
3. Giữ panel hiện tại để chạy song song, so β trước/sau.

## 7. Con trỏ
- `12_audit/concordance_confirmed_errors_2026-06-29.csv` (12 lỗi)
- `12_audit/concordance_hs_revision_fixes_2026-06-29.csv` (2 đã vá)
- backup: `03_/outputs/concordance_final_asean_pre_hsfix_2026-06-29.csv`
