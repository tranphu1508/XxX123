# Handoff — 2026-06-26 — Event-study BACI (chế độ 2: cú siết MRL → thương mại)

## 1. Metadata
- Ngày: 2026-06-26 | Trạng thái: HOÀN TẤT — DỪNG | Kết quả NHÂN QUẢ CHÍNH (chế độ 2).

## 2. Đã làm
- Panel BACI: 7.488 dòng (12 sp HS6 × 52 đích EU27+RoW × 2012–2023), giữ zero 46%, khóa (k,d,t) duy nhất. VN-xuất $6,4–11,3 tỷ/năm (validate OK).
- Treatment ω2016-filter: 4 cohort (gạo 2018 tricyclazole; cam/cà phê/fruits081090 2021). Ớt/chè never (phantom đã lọc).
- PPML tam-sai + event-study + Sun-Abraham/TWFE + pre-trends + RoW reallocation + robustness.

## 3. KẾT QUẢ (báo thẳng)
- **Tam-sai β = +0,207 (p=0,12, +23%)** — DƯƠNG, không ý nghĩa, dấu NGƯỢC kỳ vọng.
- **Pre-trends KHÔNG phẳng:** gạo (cohort sạch nhất, 2018) τ=−2 = +1,04 (p=0,003) → VI PHẠM song song → **không kết luận nhân quả**.
- TWFE-unit ATT ≈ 0 (p=0,91) vs tam-sai +23% → NHẠY đặc tả. (Sun-Abraham/CS PPML không fit — pyfixest fepois sập FE thưa; nhưng pre-trends fail là ID threat cốt lõi.)
- RoW reallocation: EU −18% (p=0,008), RoW −29% — không thấy dịch EU→RoW (control nhiễm).

## 4. Confounder (vì sao fail)
- **EVFTA 01/08/2020** cắt thuế nông sản VN→EU đúng lúc 3/4 cohort 2021 (all17→EU +65% hậu-EVFTA).
- **Durian (control never-treated) bùng nổ 8×** (2018 $268M→2023 $2.14B) → control NHIỄM.
- gạo→EU bé ($10–77M) → thí nghiệm yếu lực.

## 5. Output
- 07_/baci_eventstudy_panel.csv (7.488 dòng) + baci_eventstudy_coefs.csv + baci_did_coef.csv.
- 07_/eventstudy_baci_2026-06-26.md.

## 6. Cờ review (DỪNG)
- Pre-trends FAIL → đề xuất: (a) kiểm soát EVFTA tariff-line; (b) loại durian khỏi control; (c) chuyển trọng tâm CHẾ ĐỘ 1 (biên mở rộng + RASFF, đã có tín hiệu). Chờ Claude quyết hướng.
