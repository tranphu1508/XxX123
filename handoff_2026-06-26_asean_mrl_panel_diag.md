# Handoff — 2026-06-26 — ASEAN Chặng 2: Panel MRL EU + chẩn đoán + CỔNG hình-dạng-cong

## 1. Metadata
- Ngày: 2026-06-26 | Trạng thái: HOÀN TẤT — DỪNG (chưa ước lượng). Panel HS6×năm, KHÔNG chiều nước; equal-weight weakest-link.

## 2. Đã làm
- 284 mã EU → **137 HS6 (77 SẠCH + 60 GỘP)**. Panel `asean_mrl_panel.csv` 1.781 dòng (137 HS6 × 2011-2023), độ-ngặt=-ln(min MRL) weakest-link A_k, tái dùng builder VN (0 sai).

## 3. Chẩn đoán A — độ tán HS6-gộp
- 49 vô hại | **11 lump_divergent** (070920,070940,070951,070960,070970,070999,081010,081020,081030,081040,090421).
- ⚠ 081090/121190 "vô hại" CHỈ vì weakest-link NÉN (che dị biệt sản phẩm); mức mean vẫn phân kỳ — ghi rõ.

## 4. Chẩn đoán B (CỔNG) — KHÔNG ĐẠT
- Phân bố độ-ngặt: **100% gần-sàn** (59% LOD≤0,01 + 41% 0,01-0,05); **0% lỏng/vừa**; sd 0,87. MEAN cũng bó (sd 0,31). → **nén CẤU TRÚC** (MRL EU đồng loạt LOD).
- **VERDICT: bó cụm → KHÔNG đủ trục vẽ hình-dạng-cong** (báo thẳng). Khuyến nghị: chuyển sang chiều THỜI GIAN (cú siết within-product) làm nhận diện chính; hoặc nhị phân ngặt/vừa; KHÔNG vẽ cong cross-section.

## 5. Output
- 04_/outputs/asean_mrl_panel.csv (HS6×năm + lump_divergent) + 04_/asean_mrl_panel_diag_2026-06-26.md.

## 6. Cờ review (DỪNG)
- Claude: 11 lump_divergent (mẫu sạch?); CỔNG độ-ngặt bó cụm → đồng ý bỏ cross-section-curvature, chuyển chiều thời gian? Chặng 3 = merge BACI + phủ-sóng nước.
