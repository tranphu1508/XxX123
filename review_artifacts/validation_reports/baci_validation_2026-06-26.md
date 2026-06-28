> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/02_data_collection_and_api_scripts/validation_reports/baci_validation_2026-06-26.md, cập nhật 2026-06-26.

# Báo cáo kiểm định BACI — 2026-06-26

- Nguồn: CEPII BACI, **release 202601**, **HS revision = HS12** (phủ 2012–2024). Release date 2026-01-22 (theo `Readme.txt` trong gói).
- Artifact kiểm: bản đã tải sẵn trên máy (`Version 1/.../BACI_HS12_V202601/`), khớp release hiện hành của CEPII.
- Công cụ: DuckDB 1.5.4 (đọc trực tiếp CSV, `k` ép kiểu VARCHAR để giữ số 0 đầu).
- Cửa sổ kiểm: 2015–2024 (10 năm). Gói còn chứa 2012–2014 (không thuộc cửa sổ phân tích).
- Tham chiếu trích dẫn: Gaulier & Zignago (2010); Licence Etalab 2.0.

## A. Độ đầy đủ (completeness) — ĐẠT
- Đủ 10 năm 2015–2024, mỗi năm một file CSV, không năm nào thiếu.
- Số sản phẩm HS6: 5198–5199/năm (metadata `product_codes` có 5202 mã) — khớp kỳ vọng ~5000.
- Đủ 5 nước xuất khẩu ASEAN-5 (mã COMTRADE tra từ metadata, không gán tay): Viet Nam 704, Thailand 764, Indonesia 360, Philippines 608, Malaysia 458 — đều hiện diện với lượng dòng lớn (ví dụ 2024: VNM 116.778, THA 181.565, IDN 131.860, PHL 65.233, MYS 148.159).
- Đủ nhóm điểm đến cần cho tái phân bổ: EU-27 (27 mã hiện hành), USA 842, China 156, Japan 392, Rep. of Korea 410, India 699 — đều có trong metadata 238 nước.
- Dòng ASEAN-5 → EU-27 tồn tại và KHÔNG nhỏ bất thường: 115.720–147.096 dòng/năm (xem bảng).

## B. Tính toàn vẹn (integrity) — ĐẠT
- Schema đúng `t,i,j,k,v,q` ở mọi file.
- `k` đọc dạng CHUỖI, độ dài = 6 ký tự cho 100% mã (số 0 đầu được giữ; nếu đọc dạng số sẽ mất → bắt buộc đọc string ở các bước sau).
- `(t,i,j,k)` DUY NHẤT: số dòng trùng = 0 ở cả 10 năm.
- Tham chiếu (kiểm 2015 & 2024, đại diện): mọi `k` ∈ `product_codes` (bad_k=0); mọi `i`,`j` ∈ `country_codes` (bad_i=bad_j=0).
- Checksum SHA-256 metadata: `country_codes_V202601.csv` = 32102cbc…2999; `product_codes_HS12_V202601.csv` = f4805a12…6102; `Readme.txt` = 156c8fe9…4c66. Checksum zip + từng CSV: xem `01_raw_data_frozen/trade_data_baci/checksums_2026-06-26.txt` (sinh khi đóng băng).

## C. Chất lượng (quality) — ĐẠT (kèm 2 cờ)
- `v` > 0 với 100% dòng ở mọi năm (BACI chỉ lưu dòng dương). **Dữ liệu KHÔNG chứa số 0** → zeros phải được dựng riêng ở bước lập panel cho PPML (không thuộc bước này).
- `q` (lượng, tấn) có thể thiếu (mã hóa = ô trống): **2,3%–3,5%/năm** (xem bảng). Không cản trở (ước lượng dựa trên `v`).
- Khoảng hợp lý: không có `v` ≤ 0; `q` không âm.
- **CỜ 1 — năm 2024 provisional:** đánh dấu ở mọi nơi (quyết định: chỉ dùng robustness, mẫu chính 2015–2023 — xem `00_project_documentation/analytical_decisions_log.md`). Lưu ý: ở mức tổng ASEAN→EU, giá trị 2024 (≈165,8 tỷ kUSD) KHÔNG bị hụt rõ so với 2022–2023, nhưng rủi ro provisional nằm ở mức chi tiết (sản phẩm×đối tác: thiếu reporter → "số 0 giả"), đúng vùng nhạy cho phân tích MRL.
- **CỜ 2 — mã EU "cũ":** map EU-27 theo iso3 ra 29 mã vì BACI giữ 2 mã COMTRADE cũ chia sẻ iso3 — 58 (Belgium-Luxembourg) và 280 (CHLB Đức cũ). Cả hai có **0 dòng** ở 2015–2024 → EU-27 dùng đúng 27 mã hiện hành, an toàn.

## Bảng tổng hợp theo năm (2015–2024)

| Năm | Số dòng | HS6 | Dòng trùng (t,i,j,k) | q thiếu | q thiếu % | v≤0 | ASEAN-5→EU-27 (dòng) |
|---|---|---|---|---|---|---|---|
| 2015 | 10.782.381 | 5199 | 0 | 302.136 | 2,8% | 0 | 117.762 |
| 2016 | 10.868.820 | 5199 | 0 | 273.045 | 2,5% | 0 | 115.720 |
| 2017 | 11.213.140 | 5199 | 0 | 261.162 | 2,3% | 0 | 119.684 |
| 2018 | 11.370.143 | 5199 | 0 | 275.914 | 2,4% | 0 | 121.261 |
| 2019 | 11.506.556 | 5199 | 0 | 282.817 | 2,5% | 0 | 123.815 |
| 2020 | 11.150.663 | 5199 | 0 | 288.008 | 2,6% | 0 | 122.582 |
| 2021 | 11.673.491 | 5199 | 0 | 314.378 | 2,7% | 0 | 134.607 |
| 2022 | 11.677.171 | 5198 | 0 | 344.342 | 2,9% | 0 | 139.840 |
| 2023 | 11.755.559 | 5199 | 0 | 416.492 | 3,5% | 0 | 147.096 |
| 2024 ⚠ provisional | 11.109.411 | 5198 | 0 | 361.162 | 3,3% | 0 | 147.096 |

Giá trị ASEAN-5→EU-27 (nghìn USD), tham khảo: 2021 = 147.467.239; 2022 = 165.823.057; 2023 = 157.966.012; 2024 = 165.821.149.
(Ghi chú: số dòng ASEAN→EU 2023 và 2024 trùng nhau 147.096 chỉ là ngẫu nhiên — tổng giá trị khác nhau, các chỉ số khác cũng khác → không phải lỗi đọc dữ liệu.)

## Kết luận
Bản BACI HS12 V202601 ĐẠT cả 3 nhóm kiểm định, đủ điều kiện đóng băng làm dữ liệu thương mại gốc cho cửa sổ 2015–2024. Hai cờ cần mang theo downstream: (1) năm 2024 provisional → robustness-only; (2) năm cuối có % q thiếu nhỉnh hơn (3,3–3,5%) nhưng không ảnh hưởng ước lượng theo `v`.
