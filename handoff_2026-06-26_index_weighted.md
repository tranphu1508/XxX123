# Handoff — 2026-06-26 — Cắm ω vào chỉ số (weakest-link membership) + banned-but-used + re-validate

## 1. Metadata
- Ngày: 2026-06-26 | Trạng thái: HOÀN TẤT — DỪNG trước BACI | CHỈ ĐỌC panel/MARD/RASFF.

## 2. Bước 0 — đối chiếu xuyên chuỗi 14 thông tư
- **6 mã gap:** bưởi/chanh = **lỗi-khớp-tên** → thu hồi crop-level qua nhóm 'cây có múi' (dithiocarbamates, imidacloprid); đậu bắp/chanh leo/parsley/basil = **GAP-THẬT** → broad 'rau'/'cây ăn quả' fallback.
- **Chất rớt (mốc chính xác):** carbendazim & acephate LOẠI sau 03/2018 (~2019); chlorpyrifos & fipronil sau 10/2020 (~2021). KHÔNG phải "rớt 2023" đồng loạt.
- **banned-but-used:** carbofuran=0, methamidophos=0 dòng trong CẢ 14 thông tư (cấm suốt) ✓.

## 3. Chỉ số
- `S_lvl_max_omega2016` = weakest-link CHỈ trên chất ω-2016>0 (membership filter). omega_source per mã (crop/broad).
- banned_used[k,t] kênh RIÊNG (carbofuran+methamidophos RASFF: ớt 7, thanh long 3, other 10). + S_lvl_max_omega_plusbanned robustness.
- S_lvl_max_omega2023 (membership phản ứng: fipronil/chlorpyrifos/carbendazim rớt khỏi gạo/cà phê…).

## 4. RE-VALIDATE (Poisson RASFF)
- S_equal: coef +0,90 p=0,004 AIC 386,1. **S_omega2016: +0,28 p=0,076 AIC 391,9 → ω-filter fit RASFF KÉM hơn.**
- Lý do: ω loại phantom + banned-but-used (mất tín hiệu). CAVEAT CỨNG: RASFF = chọn+đo, double-dip, KHÔNG nhân quả; ω2016 ngoại sinh sạch hơn → vẫn = chính cho BACI. Outcome nhân quả = BACI, không lặp RASFF.

## 5. Output
- 07_/index/vn_stringency_index_weighted.csv (272 dòng: omega2016/omega2023/plusbanned/equal + banned_used + omega_source).
- 07_/index/index_weighted_2026-06-26.md.

## 6. Cờ review (DỪNG)
- (a) ω-filter giữ (chính BACI) hay đổi? (b) 6 mã gap: bưởi/chanh thu-hồi + 4 gap-thật fallback — OK chưa? TRƯỚC event-study BACI.
