# Nguồn dữ liệu và xuất xứ (data sources and provenance)

Bảng theo dõi mọi nguồn dữ liệu thô đưa vào dự án. Ghi đầy đủ phiên bản, ngày snapshot/tải, URL và checksum để bảo đảm khả năng tái lập. Mỗi lần thêm nguồn mới, thêm một dòng; không xóa dòng cũ.

| Nguồn dữ liệu | Phiên bản/Bản phát hành | Ngày snapshot/tải | URL | Checksum | Ghi chú |
|---|---|---|---|---|---|
| BACI (CEPII) | release 202601, HS12 (2012–2024) | tải sẵn; kiểm định + checksum 2026-06-26 | https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS12_V202601.zip | zip SHA-256 `2dd0dd61…b75bf9` | Etalab 2.0 + Gaulier & Zignago (2010). Mẫu chính 2015–2023; 2024 provisional. |
| EU MRL (EU Pesticides Database) | UI v3.3, API v3.0 | NGÀY SNAPSHOT 2026-05-27 | https://api.datalake.sante.service.ec.europa.eu/sante/pesticides/pesticide-residues-mrls-download?... | JSON SHA-256 `bc3643ec…a798bb` | DB không có giá trị pháp lý — đối chiếu EUR-Lex. 519.650 record. |
| EU product catalogue (Annex I máy-đọc) | products endpoint (API v3.0) | snapshot 2026-05-27 | https://api.datalake.sante.service.ec.europa.eu/sante/pesticides/pesticide-residues-products?... | (trong gói snapshot EU MRL) | 381 sản phẩm EU + tên khoa học + synonyms. |
| Concordance anchor (Codex/HS) | — | 2026-06-26 | Codex/HS-EN không kéo được | — | Neo: tên khoa học + heading HS2012 + Codex CCPR. |
| EU Annex I PHÁP LÝ (Reg (EU) 2018/62) | Reg (EU) 2018/62 thay Annex I của Reg 396/2005 | người dùng cung cấp; đóng băng 2026-06-27 | EUR-Lex CELEX 32018R0062 | HTML SHA-256 `c4cb8987…de578f` (01_/eu_annex1_legal/) | **GROUND-TRUTH PHÁP LÝ** mã sản phẩm EU. 381 nhóm + 924 sub-entry. Đối chiếu 17 mã VN: 17/17 khớp. Mạnh hơn catalogue máy-đọc. |
