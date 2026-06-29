# Round 006 — GPT → cowork: kiểm commit `03bc4a6`, sửa validator policy, và bắt buộc đọc literature fulltext

**Người gửi:** GPT-5.5 Pro  
**Người nhận:** cowork / Opus / các agent tiếp theo  
**Ngày:** 2026-06-29  
**Repo/commit được kiểm:** `tranphu1508/XxX123@03bc4a6`  
**Phạm vi kiểm:**

- `concordance_review_package/data/concordance_release_long.csv`
- `concordance_review_package/data/concordance_final_asean.csv`
- `concordance_review_package/sources/product_codes_HS12_V202601.csv`
- `concordance_review_package/sources/annex1_species_to_code.csv`
- `concordance_review_package/reviews/ROUND_LOG.md`
- `concordance_review_package/reviews/adjudication_decisions.csv`
- `concordance_review_package/reviews/round_005_opus_independent_review.md`

---

## 1. Verdict ngắn

Commit `03bc4a6` **tốt hơn vòng trước nhưng chưa final**.

Các điểm tốt:

1. `release_policy` và `release_reason` đã được đưa vào `data/concordance_final_asean.csv`.
2. `build_release_long.py` và `validate_release_long.py` đã self-contained trong `concordance_review_package`, không còn trỏ sang `outputs/` hay `01_raw_data_frozen/`.
3. `concordance_release_long.csv` đã tăng lên 262 dòng, đã thêm nhiều split trade-coverage: nuts in-shell+shelled, spices whole+crushed, cereal seed+grain, coffee green-only, tea full split, cocoa/carob/hops/algae restored.
4. Opus round 005 đã được đưa vào adjudication log.

Nhưng còn **blocker logic**: validator hiện vẫn không bắt được trường hợp một commodity hợp lệ bị gắn nhầm `EXPORT_CHILDREN_ONLY`. Tôi thấy ít nhất hai ca rõ ràng:

```csv
163100,Durians,081060,...,EXPORT_CHILDREN_ONLY,commodity có HS6 hợp lệ
401100,Pumpkin seeds,120799,...,EXPORT_CHILDREN_ONLY,commodity có HS6 hợp lệ
```

Hai dòng này tự mâu thuẫn: `release_reason` nói là commodity có HS6 hợp lệ, nhưng `release_policy` lại loại khỏi release. Với gravity-MRL, đây là false negative nguy hiểm.

---

## 2. P0 — sửa validator: không chỉ kiểm EXPORT_PRODUCT

Validator hiện kiểm “known-commodity-presence” theo logic:

```python
for row in cc[cc['release_policy'] == 'EXPORT_PRODUCT']:
    ensure row hs6 appears in release_long
```

Logic này không thể bắt lỗi nếu `release_policy` đã sai ngay từ đầu. Cần thêm validator độc lập với policy hiện tại.

Đề xuất thêm check mới vào `validate_release_long.py` hoặc file riêng `validate_terminal_policy.py`:

### 2.1. Rule bắt buộc

Một dòng trong `concordance_final_asean.csv` phải là `EXPORT_PRODUCT` nếu đồng thời thỏa:

```text
- hs6 nonblank
- không phải excluded_nec / Others (2)
- không phải EXCLUDE_NONFOOD / animal-origin out-of-study
- không phải group heading thật trong master
- không có mã con trong master được export thay cho nó
```

Không đủ để xem `eu_code.endswith("0000")` hoặc tên bắt đầu bằng `(a)/(b)/(d)`.

### 2.2. Phân biệt “has Annex subitems” với “has exported children in master”

Nhiều parent trong Annex có subitems, nhưng nếu các subitems không tồn tại trong `concordance_final_asean.csv` như dòng riêng, thì parent vẫn là đơn vị release của master.

Ví dụ `0152000 Strawberries` có subitems trong Annex, nhưng nếu master chỉ có `0152000`, thì `0152000 -> 081010` phải export. Tương tự với nhiều commodity khác.

Do đó điều kiện `EXPORT_CHILDREN_ONLY` phải dựa trên:

```text
Có child rows thực sự trong concordance_final_asean.csv và các child rows đó được export.
```

Không dựa trên việc `annex1_species_to_code.csv` có sub_code phụ.

### 2.3. Pseudocode validator

```python
import re
import pandas as pd

cc = pd.read_csv("concordance_review_package/data/concordance_final_asean.csv", dtype=str).fillna("")
rel = pd.read_csv("concordance_review_package/data/concordance_release_long.csv", dtype=str).fillna("")

rel_pairs = set(zip(rel.eu_code.astype(str), rel.hs6.astype(str).str.zfill(6)))
master_codes = set(cc.eu_code.astype(str))

# infer parent-child by code prefix only where child appears as a real eu_code in master
# EU codes are variable length in file; use zero-padded string convention already present.
def real_children(eu_code: str) -> list[str]:
    prefix = eu_code[:-3]   # adapt if needed; better: use annex parent/subcode table explicitly
    return [c for c in master_codes if c != eu_code and c.startswith(prefix)]

def has_hs(row):
    return bool(str(row.hs6).strip()) and str(row.hs6).lower().strip() != "nan"

def is_excluded(row):
    txt = " ".join(str(row.get(k, "")) for k in ["phase2_status", "needs_review", "excluded_nonfood", "release_policy", "eu_desc"])
    return ("excluded_nec" in txt or "EXCLUDE_NEC" in txt or "EXCLUDE_NONFOOD" in txt or "Others (2)" in row.eu_desc)

errors = []
for _, row in cc.iterrows():
    if not has_hs(row) or is_excluded(row):
        continue

    if row.release_policy == "EXPORT_CHILDREN_ONLY":
        children = real_children(row.eu_code)
        exported_children = [c for c in children if c in set(rel.eu_code.astype(str))]
        if not exported_children:
            errors.append(f"{row.eu_code} {row.eu_desc}: policy=EXPORT_CHILDREN_ONLY but no exported child; likely dropped terminal commodity")

    if "commodity có HS6 hợp lệ" in row.release_reason and row.release_policy != "EXPORT_PRODUCT":
        errors.append(f"{row.eu_code} {row.eu_desc}: release_reason says commodity valid but policy={row.release_policy}")
```

Pseudocode trên cần cowork chỉnh lại parent-child logic cho chắc, tốt nhất join qua `annex1_species_to_code.csv` và master `eu_code` thay vì chỉ prefix string.

---

## 3. P0 — những dòng cần kiểm ngay trước khi rebuild

Tôi không khẳng định danh sách này là exhaustive; đây là các ca tôi thấy rõ từ commit `03bc4a6`.

```csv
eu_code,eu_desc,current_hs6,current_release_policy,recommended_policy,issue
163100,Durians,081060,EXPORT_CHILDREN_ONLY,EXPORT_PRODUCT,Durian là commodity terminal trong master; đang rơi khỏi release_long
401100,Pumpkin seeds,120799,EXPORT_CHILDREN_ONLY,EXPORT_PRODUCT,Pumpkin seeds là commodity master; nếu không export child rows thì parent phải export
```

Ngoài ra cần chạy validator mới để tìm mọi dòng tương tự:

```text
release_policy == EXPORT_CHILDREN_ONLY
AND hs6 nonblank
AND release_reason contains "commodity có HS6 hợp lệ"
```

Dòng có pattern này gần như chắc chắn là lỗi metadata/policy.

---

## 4. Đánh giá nhanh policy current release

Hiện tại `03bc4a6` đã áp một phần policy `TRADE_COVERAGE_PRIMARY`:

- Nuts đã bắt đầu có in-shell + shelled: coconut, walnut, Brazil nut, macadamia, chestnut, cashew, hazelnut, almond.
- Spices đã bắt đầu có whole + crushed/ground: cloves, mace, cinnamon, coriander, nutmeg, cumin, pepper, anise, vanilla, cardamom, ginger, juniper.
- Coffee vẫn green-only: `090111;090112`.
- Hops vẫn `121010`.
- Cherry sweet vẫn `080929`.

Tôi đồng ý đây là hướng hợp lý cho **main trade-coverage**, nhưng hiện cần literature check trước khi chốt vì user nói folder cowork có fulltext học thuật liên quan.

---

## 5. Yêu cầu mới: cowork phải đọc literature fulltext trước khi chốt policy

User cho biết folder làm việc của cowork có các văn liệu học thuật fulltext liên quan đến vấn đề concordance/MRL/gravity. Trước vòng tiếp theo, cowork cần đọc và phân tích các fulltext đó để xác định các bài trước xử lý **RAC vs trade coverage**, **processed form**, và **HS concordance** như thế nào.

Không được chỉ nói “the literature usually does X”. Cần trích xuất bằng chứng cụ thể từ từng paper.

### 5.1. Tạo inventory literature

Tạo file:

```text
concordance_review_package/reviews/literature_inventory.csv
```

Schema đề xuất:

```csv
file_path,citation_short,title,authors,year,journal_or_source,study_region,standard_type,trade_data_source,product_code_level,hs_revision,uses_mrl_data,unit_of_analysis,notes
```

Cowork phải scan toàn bộ folder làm việc và đưa vào tất cả fulltext liên quan, kể cả PDF, DOCX, TXT, markdown notes, replication docs.

### 5.2. Tạo matrix policy extraction

Tạo file:

```text
concordance_review_package/reviews/literature_policy_matrix.csv
```

Schema bắt buộc:

```csv
citation_short,year,question,addressed_or_not,evidence_quote,page_or_section,interpretation_for_this_project,confidence
```

Các `question` bắt buộc:

```text
Q1_unit_of_analysis_hs6_or_other
Q2_trade_data_source_baci_comtrade_other
Q3_hs_revision_and_concordance_method
Q4_standard_or_mrl_product_level
Q5_raw_agricultural_only_or_processed_included
Q6_how_many_to_many_concordance_handled
Q7_how_hs_form_splits_handled_in_shell_shelled_whole_crushed_seed_grain
Q8_whether_processed_forms_excluded_or_included
Q9_how_missing_or_lumped_codes_handled
Q10_robustness_checks_for_product_scope
```

Với mỗi paper, phải có quote ngắn hoặc page/section. Nếu paper không nói, ghi `not stated`; không suy diễn quá mức.

### 5.3. Tạo synthesis memo

Tạo file:

```text
concordance_review_package/reviews/round_006_cowork_literature_synthesis.md
```

Cấu trúc bắt buộc:

```markdown
# Round 006 — Literature synthesis for RAC vs trade coverage

## 1. Corpus reviewed
- Table of fulltext files and citations

## 2. What prior papers actually do
- Product unit
- Trade data coding
- Standards/MRL coding
- Concordance method
- Raw vs processed scope
- Handling of HS form splits

## 3. Direct implications for our concordance
- Nuts
- Spices
- Coffee
- Hops
- Coconut
- Cinnamon
- Sweet peppers
- Rice/cereals
- Cherry/subitems

## 4. Recommended policy after literature review
- Main release policy
- Robustness release policy
- Exclusion policy

## 5. Decisions to append to adjudication_decisions.csv
``` 

### 5.4. Không được bỏ qua các câu hỏi này

Cowork cần trả lời rõ bằng literature:

1. Các paper gravity-MRL/SPS thường map treatment sang HS6 như thế nào?
2. Họ có chỉ dùng raw agricultural commodities, hay dùng trade HS6 rộng hơn?
3. Nếu HS6 có cặp in-shell/shelled, họ lấy một mã hay cả hai?
4. Nếu spices có whole/crushed, họ lấy một mã hay cả hai?
5. Nếu coffee có green/roasted, họ loại roasted hay giữ?
6. Nếu rice có paddy/brown/milled/broken, họ giữ tất cả hay chỉ paddy?
7. Có paper nào explicitly nói về processed goods / primary processed agricultural goods không?
8. Nếu không có paper nào nói, kết luận phải ghi là “literature silent; project-specific choice”.

---

## 6. Literature-based policy decision format

Sau khi đọc literature, cowork append các decision mới vào:

```text
concordance_review_package/reviews/adjudication_decisions.csv
```

Schema hiện có:

```csv
decision_id,date,eu_code,eu_desc,issue_type,before_hs6,after_hs6,release_policy,decision,rationale,decided_by,reviewed_by,source_round
```

Các decision cần có ít nhất:

```csv
ADJ-006-LIT-POLICY,2026-06-29,(global),RAC vs trade coverage,LITERATURE_POLICY,pre-literature policy,post-literature policy,EXPORT_PRODUCT,accepted/revised,"Based on literature matrix: ...",cowork,GPT/Opus pending,006
ADJ-006-DURIAN,2026-06-29,0163100,Durians,TERMINAL_COMMODITY_DROPPED,EXPORT_CHILDREN_ONLY,EXPORT_PRODUCT,EXPORT_PRODUCT,fix_required,"Durian terminal commodity; no exported children; release_reason contradicted policy",cowork,GPT pending,006
ADJ-006-PUMPKINSEED,2026-06-29,0401100,Pumpkin seeds,TERMINAL_COMMODITY_DROPPED,EXPORT_CHILDREN_ONLY,EXPORT_PRODUCT,EXPORT_PRODUCT,fix_required,"Pumpkin seeds terminal/master commodity; no exported children; release_reason contradicted policy",cowork,GPT pending,006
```

Nếu literature thay đổi policy cho nuts/spices/coffee/hops/coconut/cinnamon, append decision cụ thể cho từng nhóm.

---

## 7. Required outputs before next GPT check

Cowork cần push các file sau:

```text
concordance_review_package/reviews/literature_inventory.csv
concordance_review_package/reviews/literature_policy_matrix.csv
concordance_review_package/reviews/round_006_cowork_literature_synthesis.md
concordance_review_package/reviews/adjudication_decisions.csv
concordance_review_package/reviews/ROUND_LOG.md
concordance_review_package/scripts/validate_release_long.py
concordance_review_package/scripts/validate_terminal_policy.py   # hoặc tích hợp vào validate_release_long.py
concordance_review_package/data/concordance_final_asean.csv
concordance_review_package/data/concordance_release_long.csv
```

Optional nhưng rất nên có:

```text
concordance_review_package/data/concordance_release_long_trade_coverage_primary.csv
concordance_review_package/data/concordance_release_long_core_rac_only.csv
```

---

## 8. Acceptance criteria cho vòng tiếp theo

Tôi sẽ coi round tiếp theo pass nếu:

1. `validate_release_long.py` pass.
2. Validator mới bắt được mọi `EXPORT_CHILDREN_ONLY` terminal commodity không có child export.
3. `Durians` và `Pumpkin seeds` không còn bị rơi khỏi release.
4. `ROUND_LOG.md` có Round 006, nêu rõ literature đã đọc và policy có đổi hay không.
5. `literature_policy_matrix.csv` có quote/page/section cho từng paper; không chỉ ghi ý kiến chung.
6. `adjudication_decisions.csv` có decision cho global policy và các ca P0.
7. Nếu main release là trade-coverage, phải có robustness release `CORE_RAC_ONLY` hoặc ít nhất script sinh được nó.

---

## 9. Trạng thái hiện tại của tôi

Tôi chưa đọc được các fulltext học thuật trong folder cowork vì user chỉ đưa các raw CSV/MD ở commit `03bc4a6`, không đưa trực tiếp thư mục fulltext hoặc danh sách file. Vì vậy phần literature phải do cowork đọc trong môi trường repo/folder của cowork và push evidence lại. Khi cowork push literature matrix + synthesis memo, GPT/Opus có thể review lại từng kết luận.
