# Reproducibility Package Report — end-to-end (trả lời GPT round-009)

**Dự án:** EU MRL stringency → ASEAN-5 agri-food exports (gravity-PPML). **Repo:** tranphu1508/XxX123 @70f6ff4.
**Phạm vi:** raw → frozen → concordance → MRL panel → BACI panel → estimation. **Trung thực:** phần nào tái lập được / phần nào còn manual/missing đều ghi thẳng ở §I.

---
## A. INVENTORY ARTIFACT
| artifact | type | purpose | created_by | source/origin | rows/size | checksum (sha256, prefix) | status |
|---|---|---|---|---|---|---|---|
| BACI_HS12_V202601.zip | raw frozen | thương mại song phương HS2012 | CEPII (tải tay) | cepii.fr BACI_HS12_V202601 | 1,267,950,839 B | 2dd0dd61… | frozen ✓ |
| product_codes_HS12_V202601.csv | raw | universe HS2012 (5.202 mã) | trong BACI zip | CEPII | 5,202 | (trong zip) | frozen ✓ |
| eu_mrl_bulkdownload_snapshot_2026-05-27.json | raw frozen | MRL EU (API) | EU Pesticides DB API v3.0 | datalake.sante…mrls | 519,650 rec | bc3643ec… | frozen ✓ |
| L_2018018EN…xml.html (Annex I Reg 2018/62) | raw frozen | ground-truth pháp lý sản phẩm | EUR-Lex CELEX 32018R0062 | EUR-Lex | 1,430,139 B | c4cb8987… | frozen ✓ |
| annex1_species_to_code.csv | parsed | mã EU → loài Latin | parse Annex I | derived | 1,305 | — | ✓ |
| MASTER_pesticide_crop_parsed.csv | raw frozen | rổ ω MARD (VN) | TT 03/2016 Công báo | parse | 26,877 | 7361eb9f… | frozen ✓ |
| concordance_final_asean.csv | master | EU→HS6 + release_policy | cowork (vá tay + script) | derived | 381 | — | ✓ |
| concordance_release_long.csv | output (main) | coverage, 1 HS6/dòng | build_release_long.py | derived | 268 | — | ✓ validated |
| concordance_release_core_rac.csv | output (robustness) | strict-RAC, 1 HS6/commodity | build_release_core_rac.py | derived | 220 | — | ✓ validated |
| asean_mrl_panel.csv | intermediate | stringency weakest-link/HS6×năm | build_asean_mrl_panel.py (R010) | derived | 1,781 (137 HS6) | — | ✓ REPRODUCIBLE (R010) |
| asean_baci_panel.csv | estimation input | panel 5×125×52×9 balanced | build_asean_baci_panel.py (R010) | derived | 292,500 | — | ✓ REPRODUCIBLE — exact 0-diff (R010) |
| scripts/*.py | scripts | build/validate/diagnostics | cowork | repo | 9 file | — | ✓ |
| reviews/*, ROUND_LOG, agent_rounds_log, adjudication | logs | provenance review 8 vòng | cowork+GPT+Opus | repo | — | — | ✓ |

## B. DATA DOWNLOAD / FREEZE
- **BACI (trade):** CEPII release 202601, HS revision HS12 (HS2012), phủ 2012–2024. Tải tay (1.27GB) → đóng băng `01_raw_data_frozen/trade_data_baci/`, verify SHA-256 `2dd0dd61…b75bf9`. Script lọc ASEAN-5: `Version 2/.../filter_baci.py` (KHÔNG trong repo handoff). **Re-download = manual** từ cepii.fr.
- **EU MRL:** API Pesticides DB v3.0, snapshot **2026-05-27** (519.650 record), SHA-256 `bc3643ec…a798bb`. Script: `Version 2/.../download_eu_mrl.py`. Lưu ý: API "không pháp lý" → dùng Annex I (CELEX 32018R0062) làm ground-truth.
- **Annex I pháp lý:** Reg (EU) 2018/62 thay Annex I Reg 396/2005; đóng băng 2026-06-27, SHA `c4cb8987…`.
- **MARD (ω VN):** TT 03/2016 + 03/2015 + 09/2023, Công báo CP; SHA `7361eb9f…`.
- Cửa sổ mẫu: **2015–2023 chính**, 2024 robustness (BACI 2024 provisional). Mọi raw GIỮ đủ, chỉ gắn cờ.

## C. CLEANING PIPELINE
- **Concordance (03_/scripts/):** `build_concordance_candidates.py`, `build_concordance_phase2.py` + vá tay đa vòng (xem ROUND_LOG). Output `concordance_final_asean.csv`.
- **Filters/scope:** exporter = ASEAN-5 (IDN/MYS/PHL/THA/VNM); đích = 52 (EU-27 + đối tác lớn); năm 2015–2023; HS revision = HS2012 (khớp BACI); product scope = thực vật chương 07–12 (+ một số 09/12/18/20 theo concordance); LOẠI: animal/nonfood (77), NEC "Others" (31), group-heading (children-only, 52).
- **HS-revision check:** 136/137 mã atomic concordance ∈ HS2012 universe (đã sửa 151010); merge BACI căn HS2012 đúng.
- **Dedup:** release_long khử trùng cặp (eu_code, hs6).

## D. MRL IMPUTATION & AGGREGATION
| biến | điều kiện | giá trị | cơ sở | ảnh hưởng |
|---|---|---|---|---|
| MRL not_yet_set | tổ hợp (chất×sp×năm) chưa liệt kê | **default 0.01 mg/kg** | Art 18 Reg 396/2005 (+ Drogue 2012 precedent) | ~24.2% cell panel ràng buộc (139.699) |
| MRL null in-scope | Applicable mới nhất = null | tra CELEX / pending | Reg 396/2005 | 40 ca current |
| MRL fallback | thiếu EU | **Codex CXL** | Xiong2014/Otsuki2001/Li2014 | rổ ω VN |
| aggregate độ-ngặt | nhiều chất/HS6 | **weakest-link** = −ln(min MRL) | (chọn vs mean; lump_divergent flag) | asean_mrl_panel: min_mrl_weakest→stringency |
| lumped HS6 | nhiều mã EU→1 HS6 | gộp (cờ lumped/lump_divergent) | HS6 thô hơn EU | 60/137 HS6 lumped |
- **treatment** = stringency × eu_dummy; merge vào BACI theo (hs6,year) = **MATCH 100%** (292.500/292.500).

## E. MERGE KEYS
| merge | left | right | keys | type | post-merge rows | match |
|---|---|---|---|---|---|---|
| 1 EU→HS6 | Annex I product | concordance | eu_code | 1:1/1:m | 381 | 136/137 HS6 ∈ HS2012 |
| 2 stringency→trade | asean_baci_panel | asean_mrl_panel | (hs6, year) | m:1 | 292,500 | **100%** |
| 3 treatment | panel | — | stringency×eu_dummy | — | 292,500 | — |
| (release) explode | concordance_final (EXPORT_PRODUCT) | — | eu_code→hs6 (tách ';') | 1:m | 268 | mọi hs6 ∈ HS2012 ✓ |

## F. CONCORDANCE POLICY (chốt, link log)
- **Main = TRADE_COVERAGE_PRIMARY**, robustness = **CORE_RAC_ONLY** (strict-raw).
- nuts in-shell+shelled (cashew 080131;080132); spices whole+crushed (pepper 090411;090412; allspice 090421;090422); **coffee green-only** 090111;090112; **rice** coverage gồm paddy/husked/milled/broken (CORE_RAC = paddy 100610); hops 121010 only; cherry 080929 parent-only; cotton CORE_RAC 120729; wheat CORE_RAC 100199.
- exclusions: NEC/animal/nonfood/out-of-study. group-heading = EXPORT_CHILDREN_ONLY (validator kiểm có-con-thật).
- Link: `adjudication_decisions.csv`, `ROUND_LOG.md`, `literature_policy_matrix.csv`, `round_006_cowork_literature_synthesis.md`.

## G. LITERATURE & LEGAL (chi tiết: literature_policy_matrix.csv)
- **EU Reg 396/2005 Art 18/20:** MRL đặt trên RAC (Annex II/III), áp processed qua **processing factor** → cơ sở pháp lý cho coverage. Default 0.01 (Art 18).
- **Nguyen 2026 (đối thủ VN):** green coffee 090111 = 97.6%; milled/broken rice 100630/640 = 97.9% → xác nhận coffee-green + rice-milled.
- **Drogue 2012:** apples/pears fresh+processed, HS6, default 0.01. **Hejazi 2022:** fresh-FFV. **Ferro2015/Shingal2024/Fiankor2021/Curzi2020:** HS6 chuẩn. **Otsuki2001:** processed+unprocessed.

## H. REBUILD COMMANDS
```bash
# Concordance releases (REPRODUCIBLE — script trong repo):
python concordance_review_package/scripts/build_release_long.py
python concordance_review_package/scripts/validate_release_long.py
python concordance_review_package/scripts/build_release_core_rac.py
python concordance_review_package/scripts/validate_release_core_rac.py
# Diagnostics (trong scripts/): samesample_diag.py, measure_distortion.py
# Panel (R010 — script ĐÃ có trong repo, đã test compare):
python concordance_review_package/scripts/build_asean_mrl_panel.py  --mode current
python concordance_review_package/scripts/build_asean_baci_panel.py            # legacy = exact 0-diff vs frozen
python concordance_review_package/scripts/compare_rebuilt_panel.py --old <frozen> --new <rebuilt> --keys exp hs6 dest year
# Diagnoses: rebuild_check/diagnose_baci_panel_mismatch.md, diagnose_mrl_panel_mismatch.md, diagnose_beta_robustness_concordance.md
```

## I. REPRODUCIBILITY STATUS (trung thực)
| block | status | lý do / next action |
|---|---|---|
| Concordance master + 2 release | **REPRODUCIBLE** | build+validate script trong repo; CI chạy |
| Trade download/freeze (BACI) | **MANUAL** | frozen+checksum ✓; re-download 1.27GB tay từ CEPII; filter_baci.py ở Version 2 (chưa đưa repo) |
| MRL download/freeze (EU API) | **MANUAL** | frozen+checksum ✓; download_eu_mrl.py ở Version 2 |
| Data cleaning (concordance) | **REPRODUCIBLE** | 03_/scripts + vá tay log đầy đủ |
| MRL imputation + asean_mrl_panel | **REPRODUCIBLE (R010)** | build_asean_mrl_panel.py trong repo; current rebuild = 1,404/156 HS6; diff vs frozen = intentional (year-window + concordance fixes), diagnose_mrl_panel_mismatch.md |
| Merge panel asean_baci_panel | **REPRODUCIBLE — exact (R010)** | build_asean_baci_panel.py: legacy mode tái lập frozen **bit-for-bit** (292,500 dòng, max\|diff\|=0.0, Σvalue khớp); diagnose_baci_panel_mismatch.md |
| Estimation input | **REPRODUCIBLE (R010)** | asean_baci_panel.csv tái dựng được; β replicates exactly (S1=−1.4685 vs công bố −1.47) |
| Estimation scripts | **REPRODUCIBLE** | pyfixest (samesample_diag/measure_distortion) trong repo; ppmlhdfe `.do` (estimation/) cho SE trọng tài |

### LỖ HỔNG CHÍNH — cập nhật Round 010
1. ~~Re-implement + lưu 2 script build panel~~ → **ĐÓNG (R010)**: `build_asean_mrl_panel.py` + `build_asean_baci_panel.py` + `compare_rebuilt_panel.py` đã trong repo, đã chạy compare vs frozen + log diagnosis. BACI legacy = **exact 0-diff**; β công bố **replicates exactly** (−1.4685).
2. (CÒN) Đưa filter_baci.py + download_eu_mrl.py từ Version 2 vào repo (đang ngoài repo handoff).

**Tóm tắt (R010):** concordance + releases + **cả 2 panel build** = reproducible (BACI exact, MRL intentional-diff documented) + CI; raw = frozen+checksum (re-download manual). **Bonus R010:** robustness của β với concordance đã sửa — trên mẫu common-107-HS6, stringency cũ vs mới cho β **GIỐNG HỆT (−1.52*** = −1.52***)** → concordance fixes KHÔNG lật kết quả lõi; magnitude nhạy với mức gộp HS6 (xem diagnose_beta_robustness_concordance.md).
