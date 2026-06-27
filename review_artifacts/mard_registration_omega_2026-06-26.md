# Rổ trọng số ω từ thông tư MARD (Danh mục thuốc BVTV) — 2026-06-26

> Dựng rổ đăng ký VN làm trọng số ω_ia cho chỉ số stringency — đầu vào tới hạn, **ngoại sinh** với MRL EU & kiểm tra. Nguồn = Công báo Chính phủ VN (thông tư MARD), người dùng tải sẵn. Quy tắc bằng chứng nguyên văn áp dụng. DỪNG sau khi ra rổ ω.

## BƯỚC 1 — Thông tư đã lấy được + chọn kỳ-gốc
Thư mục `…/Việt Nam/Các thông tư` có đủ các kỳ 2013–2024. Đã có **bản parse chất lượng cao, kiểm-chứng-số-lượng** (README ghi: số hoạt chất KHỚP công bố từng nhóm; cross-check vision) → `MASTER_pesticide_crop_parsed.csv` (26.878 dòng, 14 thông tư) + bản 2015/Parse.
- **ω CHÍNH (kỳ-gốc) = Thông tư 03/2016/TT-BNNPTNT** ("MARD 2016" Nguyen dùng; Công báo 14049–14063; hiệu lực 06/2016).
- **Sớm nhất (alt) = TT 03/2015** (Công báo 245–256; hiệu lực 15/03/2015) — khớp đầu cửa sổ mẫu 2015.
- **Robustness = TT 09/2023** (Công báo 1099–1108).
- **Lý do kỳ-gốc làm chính:** ω cố-định 2016 = trọng số TIỀN-ĐỊNH, không phản ứng MRL EU. Bằng chứng nội sinh của bản mới: **carbendazim, chlorpyrifos, acephate, fipronil ĐĂNG KÝ 2015/2016 nhưng = 0 (bị loại) ở 2023** → VN siết DM theo áp lực xuất khẩu/lệnh cấm quốc tế → bản 2023 NỘI SINH, chỉ dùng robustness.
- Đã đóng băng: `01_/vn_mard_circulars/` (MASTER parsed SHA-256 `7361eb9f…585c79` + source 03/2016 6 PDF + 09/2023 5 doc + 03/2015 6 PDF), read-only. Provenance đã ghi.

## BƯỚC 2 — Granularity: **THEO CÂY (crop-level)** ✅ (lý tưởng)
Danh mục CÓ cột cây/đối tượng cho từng hoạt chất → rổ ω-theo-cây (hoạt chất × cây). Bằng chứng nguyên văn (MASTER):
```
Carbendazim | crop=bông vải | category=fungicide | 03/2016/TT-BNNPTNT | hiệu lực 2016-06-06
Carbendazim 03/2016 đăng ký trên: cam, cà phê, lúa, sầu riêng, thanh long, vải, xoài, ớt, nho, … (29 cây)
```
- Intensity = **số tên-thương-phẩm** (ten_thuong_pham) /(hoạt chất × cây) + binary đăng-ký + share trong cây.
- **GAP granularity:** 6/17 mã VN KHÔNG có ω crop-level cho chất RASFF (bưởi, chanh, đậu bắp, chanh leo, parsley, basil = 0 chất) → dùng **ω quốc-gia fallback** (`omega_vn_national_fallback.csv`). Mã có ω-cây tốt: gạo (16 chất), cà phê (15), vải/nhãn (13), cam/xoài (5), ớt/sầu riêng (2).

## BƯỚC 3 — Map hoạt chất → RASFF-18 (NGUYÊN VĂN) — 16/18 thấy, 2 thiếu
| RASFF-18 | tên Danh mục (nguyên văn) | #cây (2016) | #cây (2023) |
|---|---|---|---|
| carbendazim | `Carbendazim` | 29 | **0 (loại)** |
| permethrin | `Permethrin` (≠ Cypermethrin) | 11 | 7 |
| chlorpyrifos | `Chlorpyrifos`, `Chlorpyrifos Ethyl` (≠ `Chlorpyrifos Methyl`) | 17 | **0 (loại)** |
| tricyclazole | `Tricyclazole` | 8 | 8 |
| chlorfenapyr | `Chlorfenapyr` | 6 | 6 |
| hexaconazole | `Hexaconazole` | 22 | 21 |
| acetamiprid | `Acetamiprid` | 9 | 9 |
| propiconazole | `Propiconazole` | 11 | 9 |
| imidacloprid | `Imidacloprid` | 18 | 18 |
| **carbofuran** | **— KHÔNG có trong Danh mục —** | **0** | **0** |
| dinotefuran | `Dinotefuran` | 14 | 14 |
| profenofos | `Profenofos` | 7 | 7 |
| cypermethrin | `Cypermethrin`, `Alpha-/Beta-cypermethrin` | 19 | 19 |
| acephate | `Acephate` | 13 | **0 (loại)** |
| **methamidophos** | **— KHÔNG có trong Danh mục —** | **0** | **0** |
| dimethoate | `Dimethoate` | 15 | 13 |
| fipronil | `Fipronil` | 18 | **0 (loại)** |
| dithiocarbamates | `Mancozeb`,`Metiram`,`Propineb`,`Thiram`,`Ziram` (gộp; maneb không đăng ký) | 37 | 37 |

*(#cây = ω quốc-gia, số cây đăng ký toàn quốc; loại false-positive permethrin⊄cypermethrin, chlorpyrifos⊄methyl.)*

## BƯỚC 4 — ĐIỂM MÙ: cấm-nhưng-vẫn-bị-từ-chối (de jure vs de facto)
| chất | RASFF vụ | ω đăng ký | trạng thái VN |
|---|---|---|---|
| **carbofuran** | **15** | **0 (mọi kỳ)** | KHÔNG trong DM được phép (cấm/loại) |
| **methamidophos** | **10** | **0 (mọi kỳ)** | KHÔNG trong DM (cấm từ lâu) |
→ 2 chất này gây **25 vụ từ chối EU** nhưng ω=0 → sẽ **rớt khỏi chỉ số có-trọng-số** dù thực tế chặn hàng. Cờ `banned_but_rejected=1`. **Đây vừa là điểm mù của ω, vừa là phát hiện** (đăng ký hợp pháp lệch sử dụng thực — nông dân dùng chất cấm). Ngoài ra **carbendazim/chlorpyrifos/acephate/fipronil**: đăng ký 2016 nhưng loại 2023 → ω-2016 GIỮ (đúng tinh thần tiền-định); ω-2023 = 0 (đừng dùng 2023 cho các chất này).

## BƯỚC 5 — Xuất rổ ω
- `omega_vn_registration_basket.csv` (918 dòng = 18 chất × 17 mã VN × 3 kỳ): `registered`, `n_tradenames`, `n_rows`, `omega_share_within_crop`, `banned_but_rejected`, `omega_source_period`.
- `omega_vn_national_fallback.csv` (54 dòng = 18 chất × 3 kỳ): ω quốc-gia (#cây, #tên-thương-phẩm) — cho 6 mã gap + robustness.
- **ω chính = 03/2016**; alt sớm = 03/2015; robustness = 09/2023.

## DỪNG — chờ Claude/người dùng
- (a) Xác nhận **granularity ω = crop-level** (gap 6 mã → national fallback): OK chưa?
- (b) Quyết xử **banned_but_rejected** (carbofuran/methamidophos): giữ biến chỉ-số phụ KHÔNG-trọng-số cho nhóm này, hay gán ω tối thiểu? — TRƯỚC khi cắm ω vào chỉ số.
- CHƯA cắm ω vào chỉ số, CHƯA chạy hồi quy.
