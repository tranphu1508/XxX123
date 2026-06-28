# Handoff — 2026-06-26 — ASEAN Chặng 3: Panel BACI đa phương + CỔNG pre-trends

## 1. Metadata
- Ngày: 2026-06-26 | Trạng thái: HOÀN TẤT — **DỪNG (STOP-RULE kích hoạt)**. KHÔNG chạy Bước 5.

## 2. Đã làm
- Panel BACI đa phương: ASEAN-5 × 126 HS6 sạch × 52 đích × 2015-2023 = **292.500 dòng**, zero 81%, khóa duy nhất.
- Bảng phủ-sóng nước→EU: VN $8,8B > Indo/Thái $2,1B > Cambodia $1,4B > Myanmar $1,15B… (user chốt ngưỡng mở rộng).
- Cohort từ asean_mrl_panel: 42 HS6 (2018: 15 ngũ cốc gồm gạo; 2022: 27 trái cây/rau).

## 3. CỔNG pre-trends — **GÃY ở CẢ HAI cohort sạch nhất**
- **Gạo 2018 (đa phương):** τ=-3 = -1,55 (p=0,003), τ=-2 = -1,51 (p=0,001); **joint F-test p=0,0009 → bác bỏ mạnh**.
- **Fruits/veg 2022:** τ=-3 = -2,96, τ=-2 = -2,95 (p<0,001).
- Đối chiếu: VN-only gãy dấu DƯƠNG (+1,04 EVFTA); ASEAN gãy dấu ÂM (-1,51 thị phần EU giảm) → ĐỀU không-phẳng ở mọi khung.

## 4. STOP-RULE → cả hai bài chuyển ĐO-LƯỜNG
- KHÔNG chạy event-study đầy đủ. Trụ = đo-lường/mô-tả ("tương quan có điều kiện, KHÔNG nhân quả"): (1) tiến hoá độ-ngặt MRL (panel); (2) mẫu hình RASFF (validate weakest-link×RASFF-18 +0,90); (3) tương quan MRL×thương mại có điều kiện.

## 5. Output
- 07_/asean_baci_panel.csv (292.500 dòng) + asean_eventstudy_2026-06-26.md (bảng phủ-sóng + cohort + verdict cổng).

## 6. Cờ review (DỪNG)
- Claude: xác nhận stop-rule (pre-trends gãy cả 2 cohort) + chuyển hướng đo-lường cho cả VN & ASEAN. Bảng phủ-sóng để user chốt mở rộng nước (cho phần đo-lường).
