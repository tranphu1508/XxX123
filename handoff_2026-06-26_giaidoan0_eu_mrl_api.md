# Handoff — 2026-06-26 — Giai đoạn 0: EU MRL API (tải → kiểm → đóng băng → diff → log)

## 1. Metadata
- Ngày: 2026-06-26. NGÀY SNAPSHOT dữ liệu: 2026-05-27.
- Task: "Giai đoạn 0, nguồn API MRL của EU (phía treatment)".
- Trạng thái: HOÀN TẤT.

## 2. Đã làm gì + SỐ KIỂM ĐỊNH CHÍNH
- Endpoint (Bước 0): `https://api.datalake.sante.service.ec.europa.eu/sante/pesticides/pesticide-residues-mrls-download?language_code=EN&format=json&api-version=v3.0` (API v3.0; DB UI v3.3). NDJSON. **Độ phủ application_date 2008–2026** (phủ trọn 2015–2024 — API CÓ lịch sử; EUR-Lex chỉ để xác thực pháp lý, không cần bù độ phủ).
- Snapshot đóng băng: `eu_mrl_bulkdownload_snapshot_2026-05-27.json`, SHA-256 `bc3643ec…a798bb`, 367.899.606 bytes.
- Kiểm định ĐẠT: **519.650 record; 704 hoạt chất; 381 sản phẩm; 229 regulation**; product_code 7 ký tự chuỗi (giữ 0 đầu); schema 0 lệch; **default/LOD 70,7%** (mrl_lod="*"); mrl_value_only: số 416.277 / "No MRL required" 73.030 (=Annex IV) / null 30.343; min 0,001–max 1500 mg/kg, 0 giá trị ≤0; Annex II/V/III/IV; applicability Applicable 299.655 / No longer 211.994 / Not yet 8.001.
- Diff (Bước 3): V1 22/05 → V2 27/05: **100% khóa chung khớp; 0 đổi hiện hành; 0 đổi lịch sử; +762 mục tương lai** (regulation mới). Không đính chính hồi tố.
- Đóng băng + checksum + provenance + **sổ điền tay 0%**.

## 3. Cấu trúc — thay đổi file
- THÊM: `02_/validation_reports/eu_mrl_validation_2026-06-26.md`; `02_/scripts/download_eu_mrl_api.py`; `01_/european_union_maximum_residue_level_snapshot/` (json snapshot + checksums_2026-05-27.txt + _snapshot_info + download_log).
- SỬA: `02_/readme_data_collection.md` (+mục EU MRL); `00_/data_sources_and_provenance.md` (+dòng EU MRL).
- THÊM (audit): `11_/issues_log.md` (+2 mục Giai đoạn 0 EU MRL).

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Dữ liệu API đã pull sẵn (V1 22/05, V2 27/05) → dùng V2 làm snapshot đóng băng; vẫn viết script tái lập + endpoint canonical.
- NDJSON → kiểm định streaming (~3s/368MB).
- Default/LOD biểu diễn TƯỜNG MINH ("*", "0.01*") — cốt lõi treatment.
- Độ phủ API 2008–2026 → EUR-Lex backfill KHÔNG cần cho độ phủ, chỉ cho xác thực pháp lý.
- Chỗ chưa chắc: khóa panel (88k trùng); 30k null; HS revision concordance (folder 03 — có sẵn concordance_EU_HS6_v3.csv ở Version 2 để kiểm revision khi dựng 03).

## 6. Cờ cần review
- issues_log (2 mục): khóa (chất×sp×ngày) không duy nhất [TRUNG BÌNH]; 30.343 MRL null [THẤP]. Xem `11_/issues_log.md`.
- Bước 6: (1) độ phủ API tới 2008 → EUR-Lex chỉ để xác thực pháp lý (KHÔNG cần bù độ phủ); (2) ràng buộc product_code EU → HS2012 (folder 03) — đã khóa do BACI=HS12.

## 7. Con trỏ bằng chứng
- Validation: `02_/validation_reports/eu_mrl_validation_2026-06-26.md`
- Snapshot đóng băng: `01_/european_union_maximum_residue_level_snapshot/`
- Script: `02_/scripts/download_eu_mrl_api.py`; readme `02_/readme_data_collection.md`
- Phát hiện: `11_/issues_log.md`
