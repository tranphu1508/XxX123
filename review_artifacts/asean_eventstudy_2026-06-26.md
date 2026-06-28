# ASEAN Chặng 3: Panel BACI đa phương + CỔNG pre-trends — 2026-06-26

> Thử thiết kế nhân quả ĐA PHƯƠNG (cross-section-cong đã chết chặng 2). Lợi thế: FE nước×năm nuốt EVFTA; FE sản phẩm×năm nuốt durian; cohort gạo đa phương (Thái/Cam/Myanmar lớn). **pre-trends = CỔNG + STOP-RULE.** Mẫu sạch (loại 11 lump_divergent). ASEAN-5 chính. **KẾT QUẢ: CỔNG GÃY → STOP-RULE kích hoạt → KHÔNG chạy cả gói.**

## Bước 1 — Panel BACI đa phương
- Đơn vị: XK(ASEAN-5: VN/Thái/Indo/Phil/Malay) × HS6(126 sạch) × đích(EU27+25 RoW=52) × 2015–2023. **292.500 dòng**, zero 81% (PPML), **khóa (xk,k,đích,t) duy nhất ✓**. Gạo (1006xx)→EU bởi cả 5 ASEAN-5.

## Bước 2 — Bảng phủ-sóng nước (→EU27, 2015–2023; user chốt ngưỡng)
| nước | tổng→EU ($k) | #cặp(HS6×năm)>0 | #HS6 | năm phủ |
|---|---|---|---|---|
| Việt Nam | 8.795.459 | 914 | 123 | 9 |
| Indonesia | 2.129.735 | 715 | 121 | 9 |
| Thái Lan | 2.127.370 | 1.020 | 131 | 9 |
| Cambodia | 1.407.381 | 471 | 95 | 9 |
| Myanmar | 1.151.654 | 275 | 70 | 9 |
| Philippines | 685.922 | 410 | 104 | 9 |
| Laos | 144.796 | 387 | 85 | 9 |
| Malaysia | 102.910 | 643 | 123 | 9 |
| Singapore | 66.791 | 524 | 112 | 9 |
| Brunei | 2.322 | 38 | 20 | 9 |
→ **ASEAN-5 = mẫu chính**; Cambodia/Myanmar (gạo, →EU lớn) = ứng viên robustness mở rộng (user duyệt ngưỡng, KHÔNG tự thêm).

## Bước 3 — Cohort siết (từ asean_mrl_panel, Δ độ-ngặt≥1, loại 2016 omnibus)
**42 HS6 treated**: **2018 = 15 HS6** (ngũ cốc: gạo 1006xx, lúa mì 1001, lúa mạch 1003, ngô 1005, yến mạch 1004…); **2022 = 27 HS6** (trái cây/rau: durian 081060, chanh 080550, berries 081040…). Gạo 2018 = cohort SẠCH NHẤT + ĐA PHƯƠNG (Thái/Cam/Myanmar/VN/Indo/Phil cùng xuất gạo→EU).

## Bước 4 — CỔNG pre-trends (cohort sạch nhất: gạo 2018) — **GÃY**
Event-study τ×EU PPML (FE exp×năm + hs6×năm + dest×năm + exp×hs6, cluster hs6):
| τ | coef | SE | p |
|---|---|---|---|
| **−3** | **−1,554** | 0,515 | **0,003** ⚠ |
| **−2** | **−1,513** | 0,456 | **0,001** ⚠ |
| 0 | −1,759 | 0,426 | <0,001 |
| +1…+5 | −1,1 … −1,8 | | <0,01 |

**PRE-TRENDS joint F-test (τ=−3,−2 = 0): F=13,97, p=0,0009 → BÁC BỎ MẠNH.** Gạo ASEAN→EU đã GIẢM (so control) TRƯỚC 2018 → song song KHÔNG thỏa. Hệ số post (~−1,3) KHÔNG tách được khỏi xu hướng-trước.

### Cohort #2 (2022 fruits/veg) — CŨNG GÃY
τ=−3 = −2,96 (p<0,001), τ=−2 = −2,95 (p<0,001) → pre-trends gãy decisively.

## VERDICT CỔNG: **GÃY ở CẢ HAI cohort sạch nhất → STOP-RULE KÍCH HOẠT**
- **KHÔNG chạy Bước 5** (event-study đầy đủ) — đúng quy tắc dừng.
- Đối chiếu xuyên dự án: VN-only gãy (gạo τ=−2 = **+1,04**, EVFTA đẩy LÊN); ASEAN đa phương gãy (gạo τ=−2 = **−1,51**, thị phần EU GIẢM). **Dấu ngược nhau nhưng ĐỀU không-phẳng** → thiết kế nhân quả chế độ 2 KHÔNG nhận diện được ở MỌI khung (VN-only LẪN đa phương).
- **Lý do:** EU là thị trường NHỎ + xu-hướng-riêng (idiosyncratic) cho nông sản ASEAN; cú siết MRL KHÔNG tạo gãy sạch — xu hướng thế tục (EVFTA, thị phần gạo giảm, durian boom) chi phối.

### Khuyến nghị (stop-rule): **CẢ HAI bài chuyển ĐO-LƯỜNG**
Bỏ tuyên bố nhân quả chế độ 2. Trụ bài = **đo-lường/mô-tả** (đúng định hướng cẩm nang "tương quan có điều kiện, KHÔNG nhân quả"):
1. Tài liệu hoá **tiến hoá độ-ngặt MRL EU** (panel — đã có): regime siết mạnh, bó-LOD.
2. **Mẫu hình từ chối RASFF** (đã validate: weakest-link×RASFF-18, coef +0,90) — đo lường ràng buộc thực.
3. Tương quan có điều kiện MRL×thương mại (KHÔNG event-study nhân quả).

## DỪNG
**CỔNG pre-trends GÃY (cả 2 cohort) → STOP-RULE → KHÔNG chạy gói nhân quả.** Chờ Claude: xác nhận stop-rule + chuyển hướng đo-lường. (Bảng phủ-sóng để user chốt mở rộng nước nếu cần cho phần đo-lường.)
