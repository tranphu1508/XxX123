# ASEAN Chặng 2: Panel MRL EU + chẩn đoán gộp + CỔNG hình-dạng-cong — 2026-06-26

> Dựng panel độ-ngặt MRL EU cho tập ASEAN rộng (HS6×năm, KHÔNG có chiều nước — MRL EU như nhau mọi nước XK; chiều nước ở BACI chặng 3). KHÔNG ω-theo-nước (bất khả) → chỉ số = MRL EU/weakest-link, equal-weight. Tái dùng máy móc VN (bậc thang, not_yet_set→0.01, baseline 2009). Hai chẩn đoán CỔNG TRƯỚC ước lượng. DỪNG sau chẩn đoán.

## Bước 0-1 — Tập + panel
- Bỏ 20 umbrella + 70 động vật + 7 nec → **284 mã EU → 137 HS6**. **HS6 SẠCH (1 EU→1 HS6): 77 | HS6 GỘP (>1 EU): 60.**
- Panel `asean_mrl_panel.csv`: 137 HS6 × 13 năm (2011–2023) = 1.781 dòng. Độ-ngặt = −ln(min MRL), weakest-link (min MRL across A_k 515 chất trong mã EU; HS6 gộp → min across mã EU). Builder kiểm chứng (VN) 0 sai.

## Bước 2 — CHẨN ĐOÁN A: độ tán trong 59/60 HS6-gộp (năm 2020)
- **49 vô hại** (CV<10%, range<1.0) | **11 `lump_divergent`**: `070920, 070940, 070951, 070960, 070970, 070999, 081010, 081020, 081030, 081040, 090421`.
- Chi tiết HS6 chú ý (n_EU, min, max độ-ngặt, CV):

| HS6 | #mã EU | min–max độ-ngặt | CV | phán |
|---|---|---|---|---|
| 081090 (trái nhiệt đới) | 6 | 4,61–5,30 | 0,05 | vô hại* |
| 121190 (thảo mộc pha trà) | 13 | 4,61–4,61 | 0,00 | vô hại* |
| 070940 (rau lá khác) | 11 | 4,61–6,21 | 0,13 | **lump_divergent** |
| 081040 (berries khác) | 8 | 4,61–5,81 | 0,10 | **lump_divergent** |
| 090921 (hạt gia vị) | 7 | 4,61–4,61 | 0,00 | vô hại |
| 070410 (bắp cải) | 8 | 6,21–6,21 | 0,00 | vô hại |

> **\* Cảnh báo nhận thức:** 081090/121190 "vô hại" CHỈ vì **weakest-link nén** (mọi mã đều có 1 chất gần LOD → min MRL sát nhau). Ở mức MRL-điển-hình (mean), 081090 (vải MRL cao vs chôm chôm sàn) vẫn phân kỳ. Weakest-link **che** dị biệt sản phẩm — ghi rõ giới hạn.

## Bước 3 — CHẨN ĐOÁN B (CỔNG): phân bố độ-ngặt across 137 HS6 (2020)
| bin (theo min MRL weakest-link) | #HS6 | % |
|---|---|---|
| lỏng (MRL>0,5) | 0 | 0% |
| vừa (0,05<MRL≤0,5) | 0 | 0% |
| ngặt (0,01<MRL≤0,05) | 56 | 41% |
| **sàn (MRL≤0,01)** | **81** | **59%** |

- **%gần-sàn (MRL≤0,05) = 100%.** Độ-ngặt: min 4,61 — median 5,30 — max 6,91; IQR 4,61–6,21; **sd 0,87**. Toàn bộ bó trong dải 4,61–6,91 (mọi sản phẩm "rất ngặt" ở chất ngặt nhất).
- **Đối chứng aggregator:** MEAN-stringency CŨNG bó cụm (min 3,13–max 4,61, **sd 0,31 < weakest-link 0,87**, 100% trong MRL 0,01–0,044). → **Nén là CẤU TRÚC** (MRL EU phần lớn ở LOD 0,01 cho hầu hết chất×sản phẩm), KHÔNG do chọn toán tử.

### VERDICT CỔNG: **KHÔNG ĐẠT (bó cụm) — báo thẳng**
Độ-ngặt cross-section **bó cụm ở đầu ngặt** (100% gần-sàn; 0% lỏng/vừa; sd nhỏ ở cả weakest-link lẫn mean). **KHÔNG đủ trục trải để vẽ hình-dạng-cong** (thiếu khối ở vùng lỏng để bắt phi tuyến). Nguyên nhân cấu trúc: EU MRL gần như đồng loạt ở LOD cho rau-quả → biến thiên cross-section cạn.

### Khuyến nghị (chờ Claude, TRƯỚC chặng 3)
- **Bỏ trục cross-section-curvature** (bất khả với MRL bó-LOD). Chuyển sang **chiều THỜI GIAN** (cú siết within-product — như tricyclazole×gạo 2018; chặng-2-VN đã thấy 34% cặp có-bước-trong-cửa-sổ) làm nguồn nhận diện chính.
- Nếu vẫn muốn cross-section: chỉ phân biệt **nhị phân ngặt(sàn) vs vừa** (không vẽ cong liên tục); hoặc mở rộng sang sản phẩm có MRL lỏng thật (hiếm trong rau-quả).
- **`lump_divergent` (11 HS6):** dùng mẫu-sạch (loại 11 này) cho phân tích chính + robustness gồm chúng.

## DỪNG
Panel + 2 chẩn đoán xong. **CỔNG hình-dạng-cong KHÔNG ĐẠT** (độ-ngặt bó cụm gần-LOD, cấu trúc). Chờ Claude: gộp-phân-kỳ (11 HS6 mẫu sạch), cổng độ-ngặt (chuyển sang chiều thời gian?). Chặng 3 = merge BACI + phủ-sóng nước.
