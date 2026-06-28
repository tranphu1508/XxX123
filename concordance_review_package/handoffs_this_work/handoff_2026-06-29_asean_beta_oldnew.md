# Handoff — 2026-06-29 — ASEAN: kiểm ổn định β panel CŨ↔MỚI (M1)

## 1. Metadata
- Ngày: 2026-06-29 | Người giao: Claude (web) | Thực thi: Cowork
- Engine: **pyfixest fepois (PPML)** — Stata KHÔNG có trong Cowork sandbox; β-coef tương đương ppmlhdfe (đã verify ở task audit: coef trùng tuyệt đối, chỉ SE-cluster impl khác). `.do` cho user chạy ppmlhdfe để có SE trọng tài.
- Trạng thái: **HOÀN TẤT — STOP-RULE KÍCH HOẠT → DỪNG chờ người dùng.**

## 2. Schema panel mới (NGUYÊN VĂN — describe)
`07_main_estimation_stata/asean_baci_panel.csv` | **N=292.500**
| cột thật | kiểu | ý nghĩa |
|---|---|---|
| exp | int | nước XK (5: 360 Indo, 458 Malay, 608 Phil, 704 VN, 764 Thái) |
| hs6 | int | mã HS6 (125; **INT → mất số 0 đầu, pad 6 số khi merge**) |
| dest | int | nước đích (52) |
| year | int | 2015–2023 (9 năm) |
| eu | int 0/1 | = **eu_dummy** (CÓ SẴN) |
| value | float | giá trị XK (level) |
| cohort/treated/post/etime/did | — | event-study (KHÔNG dùng cho M1) |

- **eu_dummy = eu** (có sẵn). **EU_MRL_M1 thiếu** → merge `stringency` từ `asean_mrl_panel.csv` theo (hs6,year): **MATCH 292.500/292.500 = 100,00%**.
- `treatment = EU_MRL_M1 × eu_dummy`: mean 2,869, sd 2,833, min 0, max 6,908; #treatment>0 = 151.875 (đích EU).

## 3. Số nhóm FE (mới | cũ)
| FE | mới | cũ |
|---|---|---|
| fe_ikt (exp×hs6×year) | 5.625 | 9.250 |
| fe_jt (dest×year) | 468 | 430 |
| fe_ijk (exp×dest×hs6) | 32.500 | 38.850 |
| fe_j (dest)=52 ; cl_ij (exp×dest)=260 (cluster) | | |
*(fe_ikt/fe_ijk mới NHỎ hơn vì 125 HS6×9 năm vs cũ 185×10; đây là khác biệt panel.)*

## 4. β `treatment` — PPML (cluster cl_ij) — NGUYÊN VĂN
| spec | absorb | β | SE | z | p | N |
|---|---|---|---|---|---|---|
| **S1 Preferred** | fe_ikt fe_jt | **−1,4685** | 0,3898 | −3,767 | 0,0002 | 241.250 |
| **S2 Conservative (3 chiều, mô hình chính)** | fe_ikt fe_jt fe_ijk | **+0,1488** | 0,0760 | 1,958 | 0,0502 | 100.006 |
| **S3 Minimum** | fe_ikt fe_j year | **−0,8844** | 0,1981 | −4,464 | 0,0000 | 241.250 |

### Bảng đối chiếu cuối
| | β_CŨ (Đợt1 M1) | S1 mới | S2 mới | S3 mới |
|---|---|---|---|---|
| β `treatment` | **−2,0770 \*\*\*** | −1,4685 \*\*\* | **+0,1488 (≈0, ĐỔI DẤU)** | −0,8844 \*\*\* |

## 5. VERDICT — STOP-RULE KÍCH HOẠT
- **S2 (mô hình chính 3 chiều) ĐỔI DẤU** (−2,08 → +0,15) **+ S1 co ~30%** (−2,08 → −1,47). β **KHÔNG ổn định** khi chuyển panel.
- Theo STOP-RULE: **KHÔNG viết lại bài, KHÔNG vứt panel cũ, KHÔNG thêm đặc tả ép β về −2.** Báo số + nêu nghi vấn + CHỜ.
- **Nghi vấn (chính):** loại mã **185→126** (concordance pháp-lý-hóa bỏ ~59 HS6 khớp-mờ cũ) có thể đang lái kết quả −2,077 cũ. Phụ: panel mới 9-vs-10 năm, 52-vs-42 đích.
- **Caveat S2:** N tụt 241k→**100k** (fe_ijk 3 chiều drop nhiều cell all-zero/singleton) → S2 nhận diện trên mẫu con KHÁC HẲN; dấu +0,15 trên mẫu nhỏ này.

## 6. Cờ review (Claude tự xác nhận)
- **Số khớp do-file?** Có — đã `describe` trước, dùng tên cột THẬT (exp/hs6/dest/year/eu/value), không giả định; merge 100%; FE đếm thật. (Block [2] do-file: `eu_dummy`→dùng `eu`; `EU_MRL_M1`→merge stringency; pad hs6 6 số.)
- **Kết luận hợp lệ theo STOP-RULE?** Có — S2 đổi dấu = đúng điều kiện DỪNG; KHÔNG tự chốt panel, KHÔNG ép β.
- **Đề xuất (CHỜ DUYỆT, chưa chạy):** diagnostic same-sample để tách nguyên nhân — chạy lại **panel CŨ giới hạn 126 HS6 sạch** (`regression_panel_FINAL.csv` đã thấy ở `Version 2/Model Run/`); nếu β cũ cũng về ~0 → chính 59 mã loại lái kết quả; nếu vẫn −2 → khác biệt cách dựng panel. Chờ người dùng OK.

## 7. Con trỏ
- 12_audit/beta_stability_log.txt (log nguyên văn) | m1_results.json
