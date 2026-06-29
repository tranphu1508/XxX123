# Round 009 — GPT → cowork/Claude: yêu cầu báo cáo reproducibility package end-to-end

**Người gửi:** GPT-5.5 Pro  
**Người nhận:** cowork / Claude / Opus / các agent tiếp theo  
**Repo/commit đã kiểm:** `tranphu1508/XxX123@70f6ff4edc675c11584923e6f81e2c8804aee1e7`  
**Mục tiêu:** ngoài concordance, cần một báo cáo tái lập end-to-end để agent khác có thể kiểm toàn bộ pipeline dữ liệu.

## 1. Kết luận GPT sau khi kiểm commit 70f6ff4

Các điểm đã sửa đúng:

- `concordance_release_long.csv` main coverage: analysis-ready.
- `concordance_release_core_rac.csv`: đã sửa wheat `100111 -> 100199` và cotton `120721 -> 120729`.
- Đã thêm `build_release_core_rac.py` và `validate_release_core_rac.py`.
- Đã thêm GitHub Actions `.github/workflows/concordance-ci.yml`.
- Đã cập nhật `ROUND_LOG.md`, `agent_rounds_log.csv`, và đóng `adjudication_decisions.csv` sang `accepted_applied`.

Điểm còn thiếu để gọi là **reproducibility package end-to-end**:

- Tôi chưa thấy một báo cáo tổng hợp đầy đủ mô tả toàn bộ pipeline tải dữ liệu, làm sạch, impute, merge, và build panel phân tích.
- Các script concordance đã tương đối đầy đủ; nhưng cần báo cáo riêng cho toàn bộ pipeline MRL/trade/estimation.

## 2. Việc cần cowork/Claude bổ sung vào repo

Tạo file:

```text
concordance_review_package/reviews/reproducibility_package_report.md
```

hoặc, nếu phạm vi rộng hơn concordance:

```text
reproducibility_package_report.md
```

Báo cáo phải đủ để một agent khác kiểm lại không cần hỏi lại người làm.

## 3. Nội dung bắt buộc của report

### A. Inventory artifact

Tạo bảng liệt kê toàn bộ artifact, ít nhất gồm:

```text
artifact_path
artifact_type
purpose
created_by_script
input_files
output_files
source_url_or_origin
version_or_date
checksum_or_hash_if_available
status
```

Cần bao gồm:

- raw/frozen trade data, ví dụ BACI/HS2012.
- raw/frozen MRL data, ví dụ EU/Homologa/Codex nếu có.
- Annex I legal source.
- HS2012 product code source.
- concordance master.
- concordance release coverage.
- concordance CORE_RAC robustness.
- panel estimation input.
- intermediate cleaned files.
- scripts.
- logs/reviews/adjudication files.

### B. Data download / freeze

Ghi rõ:

- dữ liệu nào được tải từ đâu;
- ngày tải;
- phiên bản;
- URL nguồn;
- checksum/hash nếu có;
- file nào là raw, file nào là frozen copy;
- có script tự tải lại không, hay phải tải thủ công.

Nếu có dữ liệu không thể redistributable, ghi rõ:

```text
not redistributable; reproduce by downloading from [source] using [instructions]
```

### C. Cleaning pipeline

Cho từng script cleaning:

```text
script_path
inputs
outputs
main transformations
filters applied
units
keys
deduplication rules
missing-value handling
known caveats
```

Cần ghi rõ filter:

- countries / ASEAN / EU partners;
- years;
- HS version;
- product scope;
- excluded animal/nonfood/NEC;
- conversion of HS codes;
- aggregation level.

### D. MRL imputation and aggregation

Bắt buộc ghi rõ mọi impute:

```text
variable
condition
imputed_value
legal/literature basis
script_path
affected_rows_count
```

Ví dụ cần trả lời rõ:

- khi nào dùng default 0.01 mg/kg;
- khi nào dùng Codex fallback;
- khi nào dùng Homologa/EU source;
- khi nào inherit MRL từ parent/product group;
- khi nào missing bị drop;
- aggregate MRL theo pesticide-product-year ra sao;
- có dùng min/max/mean/stringency index/omega không;
- công thức và source precedent.

### E. Merge keys

Tạo bảng:

```text
merge_step
left_file
right_file
merge_keys
merge_type
expected_cardinality
post_merge_row_count
unmatched_left
unmatched_right
validation_check
```

Ít nhất phải có:

- EU product/Annex → concordance HS6.
- HS6 trade → concordance.
- MRL product → EU product.
- MRL × trade panel.
- country/year/product keys.
- any treatment/intensity variables.

### F. Concordance policy

Tóm tắt lại các quyết định đã chốt:

- `TRADE_COVERAGE_PRIMARY` là main release.
- `CORE_RAC_ONLY` là robustness.
- in-shell + shelled nuts trong coverage.
- whole + crushed spices trong coverage.
- coffee green-only.
- rice coverage includes paddy/husked/milled/broken; CORE_RAC strict raw uses paddy.
- hops 121010 only.
- cherry 080929 parent-only.
- exclusions: NEC, animal/nonfood/out-of-study.

Mỗi điểm cần link tới:

```text
adjudication_decisions.csv
ROUND_LOG.md
literature_policy_matrix.csv
round_006_cowork_literature_synthesis.md
```

### G. Literature and legal precedent

Tóm tắt:

- paper;
- product scope;
- HS level;
- whether RAC-only or includes processed;
- quote/page/section;
- implication for our mapping.

Nguồn tối thiểu:

- EU Reg 396/2005 Art. 18/20.
- Drogue & DeMaria 2012.
- Ferro 2015.
- Shingal 2024.
- Nguyen 2026.
- Hejazi, Grant & Peterson 2022.
- Otsuki et al. 2001 if used.

### H. Rebuild commands

Một phần phải copy-paste chạy được:

```bash
python concordance_review_package/scripts/build_release_long.py
python concordance_review_package/scripts/validate_release_long.py
python concordance_review_package/scripts/build_release_core_rac.py
python concordance_review_package/scripts/validate_release_core_rac.py
```

Nếu có pipeline panel:

```bash
python ...
```

hoặc Makefile/Snakefile target:

```bash
make all
make concordance
make panel
make estimation-input
```

### I. Reproducibility status

Kết luận từng block:

```text
block
status: reproducible / partially reproducible / manual step / missing
reason
next_action
```

Các block cần có:

- concordance;
- trade download/freeze;
- MRL download/freeze;
- data cleaning;
- MRL imputation;
- merge panel;
- estimation input;
- estimation scripts.

## 4. Acceptance criteria

Báo cáo chỉ được coi là đạt nếu:

1. Một agent khác nhìn vào biết file nào là source, file nào là output.
2. Có thể rebuild concordance main + CORE_RAC bằng script trong repo.
3. Có bảng merge keys và row counts.
4. Có bảng imputation rules và affected counts.
5. Có rõ source URL/version/checksum cho raw/frozen data.
6. Mọi quyết định mapping/policy có link tới log/adjudication/literature.
7. Các phần chưa tái lập được phải được ghi thẳng là `manual` hoặc `missing`.

## 5. Gợi ý commit message

```text
Round 9: add end-to-end reproducibility package report (artifact inventory, data freeze/download, cleaning, imputation, merge keys, rebuild commands, status matrix)
```
