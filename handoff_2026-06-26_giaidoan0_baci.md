# Handoff — 2026-06-26 — Giai đoạn 0: BACI (tải → kiểm định → đóng băng → diff → log)

## 1. Metadata
- Ngày giờ: 2026-06-26
- Task / prompt tương ứng: "Giai đoạn 0, nguồn BACI: tải mới → kiểm định → đóng băng → diff bản cũ → log".
- Trạng thái: HOÀN TẤT phần khả thi; CHỜ: (a) copy binary lớn vào 01_ chạy native; (b) xác nhận HS revision concordance; (c) quyết định Bước 6.

## 2. Đã làm gì (tóm tắt)
- Bước 0: chốt **release 202601 + HS12** (phủ 2015–2024; khớp bản gốc Version 1/2). Ghi `analytical_decisions_log.md`.
- Bước 1: lấy URL canonical CEPII; viết `download_baci.py` (ghim version) + `readme_data_collection.md`. Dữ liệu đã có sẵn trên máy đúng release → không tải lại.
- Bước 2: kiểm định 3 nhóm bằng DuckDB trên CSV local 2015–2024 → `baci_validation_2026-06-26.md` (ĐẠT). Đủ 10 năm; HS6 ~5199; dup=0; v>0 100%; q thiếu 2,3–3,5%/năm; tham chiếu k/i/j sạch; ASEAN-5 & EU-27 đầy đủ.
- Bước 3 (diff): KHÔNG có vintage cũ để so (chỉ 202601) → ghi issues_log (THẤP).
- Bước 4 (đóng băng): tính SHA-256 **17 file** (zip + 13 CSV + 3 metadata) → `checksums_2026-06-26.txt`; chép metadata nhỏ vào 01_; binary lớn (~6 GB) để `freeze_baci_to_frozen.bat` chạy native (cầu nối WRITE chậm).
- Bước 5: provenance dòng BACI đầy đủ; **sổ điền tay = 0%**.

## 3. Cấu trúc thư mục sau cập nhật
- Cấu trúc KHÔNG đổi; thêm/đổi NỘI DUNG file:
  - THÊM: `02_/validation_reports/baci_validation_2026-06-26.md`, `02_/readme_data_collection.md`, `02_/scripts/download_baci.py`, `02_/scripts/freeze_baci_to_frozen.bat`
  - THÊM: `01_/trade_data_baci/checksums_2026-06-26.txt`, `_freeze_status_2026-06-26.md`, + metadata (country_codes, product_codes, Readme)
  - SỬA: `00_/analytical_decisions_log.md` (+mục BACI 202601/HS12), `00_/data_sources_and_provenance.md` (dòng BACI đầy đủ)
  - THÊM (audit): `11_/issues_log.md` (+2 mục Giai đoạn 0)

## 4. Agent / sub-agent
- Số agent đã gọi: 0.

## 5. Lập luận & quyết định của Cowork
- HS12 vì phủ TRỌN 2015–2024 (HS17 mất 2015–2016) và khớp bản gốc; release 202601 hiện hành.
- Dữ liệu đã tải sẵn đúng release → không tải lại; vẫn viết script tái lập + URL canonical cho provenance.
- Kiểm định bằng DuckDB (đọc CSV ~300 MB/s qua cầu nối — nhanh).
- Cầu nối sandbox: WRITE ~16 MB/s → copy ~6 GB vào 01_ vượt giới hạn call → giao freeze cho script native; checksum (READ) tính trực tiếp được.
- Chỗ chưa chắc: revision concordance EU (folder 03 trống); độ nhạy vintage (không có bản cũ để so).

## 6. Cờ cần review
- issues_log (2 mục Giai đoạn 0): (a) vintage diff không có bản cũ [THẤP]; (b) ràng buộc HS revision BACI HS12 ↔ concordance EU [TRUNG BÌNH]. Xem `11_audit_findings_and_issues_log/issues_log.md`.
- Bước 6 (người dùng quyết): (1) năm 2024 provisional — đã có quyết định trước (robustness-only), xác nhận giữ; (2) HS revision concordance EU phải khớp HS2012; (3) chạy `freeze_baci_to_frozen.bat` native để hoàn tất đóng băng 01_.

## 7. Con trỏ bằng chứng
- Validation: `02_/validation_reports/baci_validation_2026-06-26.md`
- Quyết định: `00_/analytical_decisions_log.md`
- Checksums/đóng băng: `01_/trade_data_baci/checksums_2026-06-26.txt`, `_freeze_status_2026-06-26.md`
- Script: `02_/scripts/download_baci.py`, `freeze_baci_to_frozen.bat`; `02_/readme_data_collection.md`
- Phát hiện: `11_/issues_log.md`

## 8. Cập nhật sau Bước 6 (2026-06-26, người dùng đã quyết)
- Năm 2024: GIỮ robustness-only (mẫu chính 2015–2023) + chạy thêm **sensitivity cả hai cách** (có/không 2024) ở bước 07/08.
- HS revision concordance EU: người dùng chọn **"tính sau"** → giữ cờ `11_/issues_log.md` (TRUNG BÌNH), quyết khi dựng folder 03.
- Đóng băng: người dùng chọn Cowork chép qua cầu nối → **ĐÃ copy zip canonical (1.27 GB) vào `01_/trade_data_baci/` và VERIFY SHA-256 KHỚP** (`2dd0dd61…b75bf9`). CSV theo năm nằm trong zip đã đóng băng (giải nén ra thư mục làm việc khi cần); bản validated vẫn ở Version 1. `01_` giờ là CHỈ ĐỌC.
