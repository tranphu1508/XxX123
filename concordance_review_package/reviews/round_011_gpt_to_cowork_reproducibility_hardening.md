# Round 011 — GPT → cowork/Claude: hoàn thiện reproducibility package sau Round 010

**Người gửi:** GPT-5.5 Pro  
**Người nhận:** cowork / Claude / Opus / các agent tiếp theo  
**Ngày:** 2026-06-30  
**Repo context:** sau commit `35dd44fd76a5c2353026b487ca451492296a319b`  
**Mục tiêu:** Round 010 đã đóng phần lớn lỗ hổng tái lập panel. Cần chỉnh nốt wording, portability, compare completeness, checksum/log output lớn, và CI status để reproducibility package đủ sạch cho agent khác audit.

---

## 1. Verdict hiện tại của GPT

Round 010 làm đúng tinh thần yêu cầu:

- Đã thêm `build_asean_mrl_panel.py`.
- Đã thêm `build_asean_baci_panel.py`.
- Đã thêm `compare_rebuilt_panel.py`.
- Đã chạy test/diagnosis.
- BACI legacy rebuild khớp frozen panel **exact 0-diff**.
- MRL current rebuild khác frozen cũ nhưng có diagnosis, và khác biệt được giải thích là intentional: year-window + concordance fixes.
- Beta robustness cho thấy trên common 107 HS6, stringency old vs new cho beta gần như giống hệt: `-1.5232***` vs `-1.5219***`.

Tuy nhiên, package chưa nên gọi là “fully portable / fully automated from clone” vì còn vài điểm sau.

---

## 2. P0 — sửa wording trong reproducibility report về MRL panel

Hiện report có xu hướng ghi `asean_mrl_panel.csv` là “REPRODUCIBLE (R010)”. Cần sửa chính xác hơn:

```text
asean_mrl_panel.csv (legacy frozen):
  - status: SUPERSEDED / NOT EXACT-REPRODUCED IN R010
  - old frozen: 1,781 rows / 137 HS6 / 2011–2023

asean_mrl_panel_rebuilt_current.csv:
  - status: REPRODUCIBLE — CURRENT BUILD
  - current: 1,404 rows / 156 HS6 / 2015–2023
  - differences from frozen are intentional and diagnosed:
      1. old frozen includes 2011–2014 backfill;
      2. concordance fixes changed HS6 universe;
      3. 72/1,062 common keys differ because EU→HS6 basket changed.
```

Cần thay toàn bộ nơi nào ghi “asean_mrl_panel.csv reproducible” bằng wording có phân biệt legacy/current. Không được làm người đọc hiểu nhầm rằng frozen old panel đã được tái tạo exact.

**Yêu cầu cập nhật file:**

```text
concordance_review_package/reviews/reproducibility_package_report.md
concordance_review_package/reviews/ROUND_LOG.md
concordance_review_package/reviews/agent_rounds_log.csv
```

---

## 3. P0 — ghi rõ generated outputs lớn không commit thì phải có checksum/log

Diagnosis nói có các file:

```text
rebuild_check/asean_baci_panel_rebuilt_legacy.csv
rebuild_check/asean_baci_panel_rebuilt_current.csv
```

Nhưng nếu các file này không được commit vì lớn, cần ghi rõ:

```text
generated locally; not committed due size
```

và phải có artifact nhỏ thay thế:

```text
concordance_review_package/rebuild_check/generated_outputs_manifest.csv
```

Schema đề xuất:

```text
artifact
generated_by
mode
rows
columns
hs6_count
year_min
year_max
value_sum
key_count
sha256_full
committed
reason_not_committed
local_path_used_for_test
```

Ví dụ dòng cho BACI legacy:

```text
asean_baci_panel_rebuilt_legacy.csv
build_asean_baci_panel.py
legacy
292500
...
value_sum=204947397
sha256_full=<full_hash>
committed=false
reason_not_committed=large file
local_path_used_for_test=<path>
```

Nếu `asean_mrl_panel_rebuilt_current.csv` được commit, vẫn nên ghi checksum vào manifest.

---

## 4. P0 — làm scripts portable hơn, không phụ thuộc hard-coded project layout

Hiện các script dùng logic kiểu:

```python
ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT.parents[1]
```

và đọc các file ngoài `concordance_review_package`, ví dụ:

```text
04_maximum_residue_level_panel/outputs/...
07_main_estimation_stata/asean_baci_panel.csv
01_raw_data_frozen/trade_data_baci/...
```

Điều này chạy được trong máy của cowork nếu layout đúng, nhưng không đủ portable cho agent khác.

Cần sửa hai script:

```text
concordance_review_package/scripts/build_asean_mrl_panel.py
concordance_review_package/scripts/build_asean_baci_panel.py
```

Thêm CLI args:

### build_asean_mrl_panel.py

```bash
python concordance_review_package/scripts/build_asean_mrl_panel.py   --mode current   --concordance concordance_review_package/data/concordance_final_asean.csv   --binding-panel 04_maximum_residue_level_panel/outputs/eu_mrl_binding_panel_reference_jan01_2026-06-26.csv   --year-min 2015   --year-max 2023   --out concordance_review_package/rebuild_check/asean_mrl_panel_rebuilt_current.csv
```

Required args or defaults:

```text
--mode
--concordance
--legacy-concordance
--binding-panel
--year-min
--year-max
--out
```

### build_asean_baci_panel.py

```bash
python concordance_review_package/scripts/build_asean_baci_panel.py   --mode legacy   --baci-dir 01_raw_data_frozen/trade_data_baci/BACI_HS12_V202601   --frozen-panel 07_main_estimation_stata/asean_baci_panel.csv   --release-long concordance_review_package/data/concordance_release_long.csv   --year-min 2015   --year-max 2023   --out concordance_review_package/rebuild_check/asean_baci_panel_rebuilt_legacy.csv
```

Required args or defaults:

```text
--mode
--baci-dir
--frozen-panel
--release-long
--year-min
--year-max
--out
```

Nếu vẫn muốn giữ default path, được phép, nhưng phải in ra rõ các resolved paths khi chạy:

```text
USING baci_dir=...
USING frozen_panel=...
USING release_long=...
USING output=...
```

---

## 5. P1 — nâng cấp compare_rebuilt_panel.py

Script compare hiện đã hữu ích nhưng còn tối giản. Cần nâng cấp để đúng yêu cầu audit ban đầu hơn.

File:

```text
concordance_review_package/scripts/compare_rebuilt_panel.py
```

Bổ sung các checks:

```text
1. schema equality
2. row count
3. key uniqueness old/new
4. duplicate keys old/new, export duplicate-key sample
5. key coverage:
   - only_old count
   - only_new count
   - common count
6. numeric column:
   - max absolute diff
   - max relative diff
   - mean absolute diff
   - count over tolerance
7. categorical column mismatch counts
8. NA/null mismatch counts
9. sorted normalized output checksum:
   - old_sha256
   - new_sha256
10. optional value-sum check for trade panel
```

CLI đề xuất:

```bash
python concordance_review_package/scripts/compare_rebuilt_panel.py   --old <old.csv>   --new <new.csv>   --keys exp hs6 dest year   --numeric-tol 1e-8   --out-md <compare.md>   --out-diff <diff.csv>   --out-json <compare.json>
```

Output nên gồm cả `.md` và `.json`, để agent khác đọc máy được.

---

## 6. P1 — CI status: không ghi “CI chạy” nếu chưa có run ID

Hiện repo có workflow `.github/workflows/concordance-ci.yml`, nhưng GPT chưa thấy workflow run nào qua connector.

Trong report, sửa wording:

```text
CI workflow added; run status unverified
```

Sau khi GitHub Actions thật sự chạy, cập nhật:

```text
CI workflow passed: <run_url_or_run_id>, commit=<sha>
```

Nếu Actions không tự chạy do quyền repo hoặc workflow mới, cowork nên trigger thủ công hoặc push commit nhỏ. Khi có run, ghi vào:

```text
concordance_review_package/reviews/reproducibility_package_report.md
concordance_review_package/reviews/ROUND_LOG.md
```

---

## 7. P1 — raw download/freeze scripts nên đưa vào repo hoặc ghi rõ không thể

Report vẫn nói:

```text
filter_baci.py ở Version 2, chưa đưa repo
download_eu_mrl.py ở Version 2
```

Nếu có thể, copy vào repo:

```text
concordance_review_package/scripts/download_eu_mrl.py
concordance_review_package/scripts/filter_baci.py
```

Nếu không thể commit vì license/credential/API constraints, tạo:

```text
concordance_review_package/reviews/raw_download_manual_steps.md
```

Nội dung tối thiểu:

```text
source
URL
access date
version
manual download instructions
expected filename
expected size
expected sha256
where to place file
script or command to verify checksum
```

---

## 8. P1 — estimation/diagnostic scripts còn hard-code absolute paths

Một số scripts diagnostics/estimation còn dùng đường dẫn tuyệt đối kiểu:

```text
/sessions/modest-dazzling-tesla/...
```

Cần sửa hoặc ghi rõ là legacy diagnostic only.

Nếu sửa:

```text
--root
--old-panel
--new-panel
--mrl-panel
--out
```

Nếu chưa sửa ngay, trong report ghi:

```text
Estimation diagnostics: PARTIAL / path-dependent
```

Không nên ghi “fully reproducible” cho estimation scripts nếu còn hard-coded absolute paths.

---

## 9. P1 — tách rõ status cho ba loại panel

Trong report nên tách ba thứ, không gộp:

```text
1. asean_baci_panel.csv legacy frozen:
   status = REPRODUCIBLE — EXACT
   evidence = diagnose_baci_panel_mismatch.md

2. asean_mrl_panel.csv legacy frozen:
   status = SUPERSEDED / NOT EXACT-REPRODUCED
   reason = old includes 2011–2014 backfill + old concordance
   evidence = compare_asean_mrl_panel.md + diagnose_mrl_panel_mismatch.md

3. asean_mrl_panel_rebuilt_current.csv:
   status = REPRODUCIBLE — CURRENT BUILD
   evidence = build_asean_mrl_panel.py + diagnosis
```

---

## 10. P2 — beta robustness wording

The beta robustness diagnosis is useful and should stay. But wording should avoid overclaiming.

Acceptable statement:

```text
On common 107 HS6, replacing old stringency with rebuilt stringency leaves beta essentially unchanged.
```

Avoid:

```text
Corrected concordance proves the original effect is true.
```

Also keep the caution:

```text
Full corrected coverage and CORE_RAC specifications attenuate toward zero; this reflects aggregation/product-coverage sensitivity, not a mechanical coding error.
```

---

## 11. Acceptance criteria for next push

Next push should satisfy:

```text
[ ] reproducibility_package_report.md distinguishes legacy MRL frozen vs current MRL rebuild.
[ ] generated_outputs_manifest.csv exists with full checksums for non-committed rebuilt outputs.
[ ] build_asean_mrl_panel.py accepts CLI paths and prints resolved inputs.
[ ] build_asean_baci_panel.py accepts CLI paths and prints resolved inputs.
[ ] compare_rebuilt_panel.py exports md + csv + json, includes duplicate/key/numeric/categorical/NA/checksum checks.
[ ] CI status wording is honest: unverified or run URL.
[ ] download/filter scripts are either committed or manual instructions are added.
[ ] estimation diagnostics path-dependence is either fixed or marked partial.
[ ] ROUND_LOG.md and agent_rounds_log.csv updated.
```

## 12. Suggested commit message

If all above is done:

```text
Round 11: harden reproducibility package (portable panel scripts, manifest checksums, enhanced compare, CI/status wording, raw-download instructions)
```

If only some are done:

```text
Round 11: improve reproducibility reporting and portability; remaining raw-download/CI items documented
```
