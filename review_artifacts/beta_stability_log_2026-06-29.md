=== KIỂM ĐỊNH ỔN ĐỊNH β — PANEL CŨ ↔ MỚI (ASEAN M1) — 2026-06-29 ===
Engine: pyfixest fepois (PPML) — Stata KHÔNG có trong Cowork sandbox; .do cung cấp cho user chạy ppmlhdfe.

PANEL MỚI: asean_baci_panel.csv | N=292.500 dòng
  cột thật: exp(5 nước:360 Indo,458 Malay,608 Phil,704 VN,764 Thái) | hs6(125, INT→pad 6 số) | dest(52) | year(2015-2023,9) | eu(0/1 = eu_dummy) | value(level XK) | + cohort/treated/post/etime/did (event-study, không dùng M1)
  eu_dummy = eu (CÓ SẴN). EU_MRL_M1 = merge 'stringency' từ asean_mrl_panel.csv theo (hs6,year): MATCH 292.500/292.500 = 100,00%.
  treatment = EU_MRL_M1 × eu_dummy: N=292.500 mean=2,8694 sd=2,8334 min=0 max=6,908; #treatment>0=151.875 (đích EU).

SỐ NHÓM FE (mới | cũ):
  fe_ikt exp×hs6×year : 5.625  | 9.250
  fe_jt  dest×year    : 468    | 430
  fe_ijk exp×dest×hs6 : 32.500 | 38.850
  fe_j dest=52 | cl_ij exp×dest=260 (cluster)

KẾT QUẢ PPML (cluster cl_ij):
  S1 Preferred   absorb(fe_ikt fe_jt)        : β=-1.4685 SE=0.3898 z=-3.767 p=0.0002 N=241.250
  S2 Conservative absorb(fe_ikt fe_jt fe_ijk): β=+0.1488 SE=0.0760 z= 1.958 p=0.0502 N=100.006   <-- ĐỔI DẤU
  S3 Minimum     absorb(fe_ikt fe_j year)    : β=-0.8844 SE=0.1981 z=-4.464 p=0.0000 N=241.250

ĐỐI CHIẾU: β_CŨ (Đợt1 M1) = -2.0770 ***
  S1 -1.47 (cùng dấu, co ~30%) | S2 +0.15 (ĐỔI DẤU, mất ~-2) | S3 -0.88 (co mạnh)

VERDICT STOP-RULE: S2 (mô hình chính 3 chiều) ĐỔI DẤU + S1 co → β KHÔNG ổn định → **DỪNG**.
  KHÔNG chốt panel mới. KHÔNG vứt panel cũ. Nghi vấn: loại mã 185→126 (concordance pháp-lý) có thể đang lái kết quả cũ -2.077; HOẶC khác biệt 9-vs-10 năm / 52-vs-42 đích. Chờ người dùng.
