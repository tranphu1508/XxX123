# Handoff — 2026-06-26 — Thiết kế bộ máy chỉ số stringency + validate RASFF

## 1. Metadata
- Ngày: 2026-06-26 | Task: thiết kế chỉ số (level/change kép) + validate RASFF | Trạng thái: HOÀN TẤT — DỪNG trước BACI
- CHỈ ĐỌC panel/diagnostic/RASFF; KHÔNG chạy hồi quy thương mại.

## 2. Đã làm
- **Phần 1:** s_akt = g-level `−ln(MRL_EU)`, 2 rổ (RASFF-18, A_k). not_yet_set→0,01; loại pending. g-gap-Codex = PENDING.
- **Phần 2:** gộp MEAN + weakest-link (max g = min MRL). Cột ω param =1 đều (KHÔNG dùng RASFF làm trọng số).
- **Phần 3:** tách LEVEL `S_lvl` (mọi chất) vs CHANGE `dS_tighten` (chỉ step_in_window). Danh mục 62 thí nghiệm tự nhiên.
- **Phần 4:** validate Poisson `count~S_lvl+nhóm FE+năm FE` (80 obs, 200 rejection).

## 3. BIẾN THỂ THẮNG: S_lvl_max_rasff (weakest-link × RASFF-18 × level)
- coef +0,904, p=0,004, AIC 386,1 (thấp nhất), pseudo-R² 0,364.
- 2 phát hiện: **weakest-link >> MEAN** (mean p≈0,9); **rổ RASFF-18 > A_k** (A_k-mean sai dấu).
- Caveat: nội sinh cường-độ-kiểm-tra (enhanced-control) — validate đo lường, KHÔNG nhân quả. offset Reg 2019/1793 PENDING.

## 4. Bản đồ đã-xây/chờ
- ĐÃ: s_akt, g-level, mean/weakest-link, level/change, chỉ số đều, validate RASFF.
- CHỜ: **ω rổ đăng ký MARD (CRITICAL)**; g-gap-Codex (tùy chọn); offset enhanced-control.
- ⛔ CHƯA chạy hồi quy thương mại BACI (DỪNG đúng phạm vi).

## 5. Output
- 07_/index/vn_stringency_index_variants.csv (272 product×year × biến thể).
- 07_/index/vn_change_natural_experiments.csv (62 cú siết sạch).
- 07_/index/index_design_2026-06-26.md (báo cáo + bảng validate + bản đồ).

## 6. Cờ review
- Claude/người dùng: (a) xác nhận biến thể thắng S_lvl_max_rasff, (b) chốt trước khi cắm ω (MARD) + chạy BACI.
