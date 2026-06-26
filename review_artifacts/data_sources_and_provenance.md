> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/00_project_documentation/data_sources_and_provenance.md, cập nhật 2026-06-26.

# Nguồn dữ liệu và xuất xứ (data sources and provenance)

Bảng theo dõi mọi nguồn dữ liệu thô đưa vào dự án. Ghi đầy đủ phiên bản, ngày snapshot/tải, URL và checksum để bảo đảm khả năng tái lập. Mỗi lần thêm nguồn mới, thêm một dòng; không xóa dòng cũ.

| Nguồn dữ liệu | Phiên bản/Bản phát hành | Ngày snapshot/tải | URL | Checksum | Ghi chú |
|---|---|---|---|---|---|
| BACI (CEPII) | release 202601, HS12 (2012–2024) | tải sẵn; kiểm định + checksum 2026-06-26 | https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS12_V202601.zip | zip SHA-256 `2dd0dd61…b75bf9` — đầy đủ: 01_raw_data_frozen/trade_data_baci/checksums_2026-06-26.txt | Etalab 2.0 + trích Gaulier & Zignago (2010). Mẫu chính 2015–2023; 2024 provisional (robustness). 0% điền tay. Đã kiểm định ĐẠT: 02_/validation_reports/baci_validation_2026-06-26.md |
| EU MRL (EU Pesticides Database) | UI v3.3, API v3.0 (DB không có mã version) | NGÀY SNAPSHOT 2026-05-27 | https://api.datalake.sante.service.ec.europa.eu/sante/pesticides/pesticide-residues-mrls-download?language_code=EN&format=json&api-version=v3.0 | JSON SHA-256 `bc3643ec…a798bb` (01_/european_union_maximum_residue_level_snapshot/checksums_2026-05-27.txt) | DB KHÔNG có giá trị pháp lý — đối chiếu EUR-Lex. Độ phủ API: 2008–2026. 519.650 record. 0% điền tay. Kiểm định: 02_/validation_reports/eu_mrl_validation_2026-06-26.md |
| EU product catalogue (Annex I máy-đọc) | EU Pesticides DB products endpoint (API v3.0) | snapshot 2026-05-27 | https://api.datalake.sante.service.ec.europa.eu/sante/pesticides/pesticide-residues-products?language_code=EN&format=json&api-version=v3.0 | (trong gói snapshot EU MRL) | 381 sản phẩm EU + tên khoa học Latin + synonyms + phân cấp. Dùng dựng concordance EU→HS6 (folder 03, vế nguồn). |
| Concordance anchor (Codex/HS) | — | 2026-06-26 | Codex CXA-4 / HS-EN / Fiankor A1 KHÔNG kéo được (FAO timeout; paywall) | — | Neo concordance EU→HS6: tên khoa học (EU catalogue) + text heading HS2012 (BACI) + cấu trúc Codex CCPR. Mỏ neo: 03_/outputs/codex_group_to_hs_heading_2026-06-26.csv (verify 60/60). |
