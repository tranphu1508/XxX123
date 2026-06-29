# Diagnosis — MRL panel rebuild (current) vs frozen — 2026-06-30

Rebuild: `build_asean_mrl_panel.py --mode current` → 1404 dòng / 156 HS6 / 2015–2023.
Frozen: `asean_mrl_panel.csv` → 1781 dòng / 137 HS6 / 2011–2023.
Common keys (hs6,year)=1062; only-old=719; only-new=342.

| cause | affected_rows | chi tiết | verdict | action |
|---|---|---|---|---|
| Year window 2011–2014 | 548 (only-old) | frozen back-fill 2011–2014 = LOD 0.01; current bắt đầu 2015 (cửa sổ dữ liệu MRL thật, API 2015–2024) | intentional_change | current dùng 2015–2023 (mẫu chính); 2011–2014 không có MRL thật → bỏ back-fill |
| HS6 set đổi (concordance fixes) | 171 only-old (19 HS6 bỏ) + 342 only-new (38 HS6 thêm) | concordance đã sửa 80+ mã (round 1–8): bỏ mã sai (vd 151010, 520100), thêm coverage (shelled nuts, crushed spices), cứu commodity (durian/strawberry) → bộ HS6 map đổi | intentional_change | current = bản đúng; frozen SUPERSEDED |
| Stringency lệch trên key chung | 72/1062 (6.8%) | rổ EU→HS6 đổi (mã sửa) → weakest-link min MRL đổi; 93.2% key chung GIỐNG | intentional_change | đúng theo concordance đã sửa |

**Kết luận:** mọi khác biệt truy được về (a) cửa-sổ-năm và (b) concordance đã sửa. Không có lỗi bug build. Current MRL panel là bản đúng (theo concordance cuối); frozen superseded. → status: **REPRODUCIBLE (current) — intentional differences documented.**
