# Raw data download / freeze — manual reproduction steps (Round 011)

Trả lời GPT §7. Hai nguồn raw KHÔNG commit vào repo (license + dung lượng), nhưng:
(a) script tải đã copy vào `scripts/raw_data_collection/`, và
(b) hướng dẫn + checksum đầy đủ ở dưới để bất kỳ agent nào tái lập + verify.

> `01_raw_data_frozen/` là **CHỈ ĐỌC**. Giải nén/biến đổi ghi ra thư mục làm việc khác.

---

## 1. BACI (CEPII) — trade data

| field | value |
|---|---|
| source | CEPII — BACI |
| release / version | **V202601**, nomenclature **HS12** (phủ 2012–2024) |
| URL | https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS12_V202601.zip |
| license | Etalab 2.0 |
| access date | 2026-06-26 |
| script | `scripts/raw_data_collection/download_baci.py` ; lọc ASEAN-5: `filter_baci.py` |
| expected filename | `BACI_HS12_V202601.zip` |
| expected size | **1,267,950,839 bytes** |
| expected sha256 | `2dd0dd6174f11e9fc33b9bacf001d50c1913dbfeed9cba30876a1668b2b75bf9` |
| place at | `01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601.zip` |

**Per-year CSV sha256 (sau giải nén)** — đối chiếu `01_raw_data_frozen/trade_data_baci/checksums_2026-06-26.txt`:
```
a7e6c024...39e5  BACI_HS12_Y2015_V202601.csv
9446ad8a...a3bd  BACI_HS12_Y2016_V202601.csv
42494f4f...fe06  BACI_HS12_Y2017_V202601.csv
9ec607f7...0e80  BACI_HS12_Y2018_V202601.csv
b51c9565...17e3  BACI_HS12_Y2019_V202601.csv
7916d6ed...c68d  BACI_HS12_Y2020_V202601.csv
9ddcc73b...573e  BACI_HS12_Y2021_V202601.csv
4d5c4fdc...754f  BACI_HS12_Y2022_V202601.csv
205d74de...532e  BACI_HS12_Y2023_V202601.csv
f4805a12...6102  product_codes_HS12_V202601.csv
32102cbc...2999  country_codes_V202601.csv
```

**Steps:**
```bash
# 1. tải zip (hoặc python scripts/raw_data_collection/download_baci.py)
curl -L -o BACI_HS12_V202601.zip "https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS12_V202601.zip"
# 2. verify zip
sha256sum BACI_HS12_V202601.zip   # == 2dd0dd61...75bf9
# 3. giải nén ra THƯ MỤC LÀM VIỆC (không phải 01_)
unzip BACI_HS12_V202601.zip -d <work_dir>/BACI_HS12_V202601
# 4. verify từng CSV
cd 01_raw_data_frozen/trade_data_baci && sha256sum -c checksums_2026-06-26.txt
# 5. build panel: trỏ --baci-dir vào <work_dir>/BACI_HS12_V202601
python concordance_review_package/scripts/build_asean_baci_panel.py --mode legacy --baci-dir <work_dir>/BACI_HS12_V202601
```

---

## 2. EU MRL — EU Pesticides Database snapshot

| field | value |
|---|---|
| source | EU Pesticides Database (UI v3.3), API v3.0 — datalake SANTE |
| version | **KHÔNG có mã version** → NGÀY SNAPSHOT = phiên bản |
| snapshot date | **2026-05-27** (tải lại sẽ KHÁC; đây là mốc tái lập duy nhất) |
| bulk endpoint | https://api.datalake.sante.service.ec.europa.eu/sante/pesticides/pesticide-residues-mrls-download?language_code=EN&format=json&api-version=v3.0 |
| script | `scripts/raw_data_collection/download_eu_mrl_api.py` |
| expected filename | `eu_mrl_bulkdownload_snapshot_2026-05-27.json` (NDJSON) |
| expected size | **367,899,606 bytes** (519,650 record) |
| expected sha256 | `bc3643ec8a995539bf8419b8284cb7cffeadf9e24e3b35d83c1f53cd77a798bb` |
| place at | `01_raw_data_frozen/european_union_maximum_residue_level_snapshot/` |

⚠ DB SANTE "KHÔNG có giá trị pháp lý" → căn cứ pháp lý đối chiếu EUR-Lex Annex I (mục 3). DB cập nhật liên tục: **không fetch lại y hệt được** → dùng đúng file snapshot 2026-05-27 đã đóng băng.

```bash
python concordance_review_package/scripts/raw_data_collection/download_eu_mrl_api.py
sha256sum eu_mrl_bulkdownload_snapshot_2026-05-27.json   # == bc3643ec...98bb
```

---

## 3. EU Annex I (legal ground-truth) & 4. VN MARD circulars
- **Annex I**: Reg (EU) 2018/62, EUR-Lex `L_2018018EN`. Đóng băng: `01_raw_data_frozen/eu_annex1_legal/` (`annex1_species_to_code.csv`, html nguồn). Dùng cho căn cứ pháp lý concordance.
- **VN MARD**: TT 03/2016 (Công báo). Parsed: `01_raw_data_frozen/vn_mard_circulars/MASTER_pesticide_crop_parsed.csv` (26,877 dòng). sha trong `12_audit/inventory_audit.csv`.

Cả hai đã commit dạng parsed CSV trong repo nguồn; chi tiết checksum ở `audit_evidence/inventory_audit.csv`.
