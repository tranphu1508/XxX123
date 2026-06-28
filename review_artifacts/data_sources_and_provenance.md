# Nguồn dữ liệu và xuất xứ (data sources and provenance)

| Nguồn | Phiên bản | Ngày | URL | Checksum | Ghi chú |
|---|---|---|---|---|---|
| BACI (CEPII) | release 202601, HS12 | 2026-06-26 | cepii.fr BACI_HS12_V202601 | zip SHA-256 `2dd0dd61…b75bf9` | Mẫu chính 2015–2023; 2024 provisional. |
| EU MRL (Pesticides DB) | API v3.0 | snapshot 2026-05-27 | datalake.sante…pesticide-residues-mrls | JSON SHA-256 `bc3643ec…a798bb` | 519.650 record. DB không pháp lý. |
| EU product catalogue | products endpoint v3.0 | 2026-05-27 | datalake.sante…pesticide-residues-products | (trong gói snapshot) | 381 sản phẩm + tên khoa học. |
| Concordance anchor | — | 2026-06-26 | Codex/HS-EN | — | Neo loài + heading HS2012 + Codex CCPR. |
| EU Annex I PHÁP LÝ (Reg 2018/62) | thay Annex I Reg 396/2005 | đóng băng 2026-06-27 | EUR-Lex CELEX 32018R0062 | HTML SHA-256 `c4cb8987…de578f` | GROUND-TRUTH pháp lý mã sản phẩm. 381 nhóm+924 sub. 17/17 mã VN khớp. |
| VN MARD Danh mục BVTV | TT 03/2016 (ω chính); 03/2015; 09/2023 | đóng băng 2026-06-27 | Công báo CP VN (TT-BNNPTNT) | MASTER parsed SHA-256 `7361eb9f…585c79` | Rổ ω (ngoại sinh MRL). Crop-level. 16/18 RASFF có; carbofuran+methamidophos banned_but_rejected. 05_/omega_vn_registration_basket.csv. |
