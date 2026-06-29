# Handoff memo cho cowork — Round 003: sửa `release_long`, policy export, và nhật ký audit

**Người gửi:** GPT-5.5 Pro  
**Người nhận:** cowork / Claude / Opus reviewer  
**Ngày:** 2026-06-29  
**Repo:** `tranphu1508/XxX123`  
**Commit đang được review:** `256e572bfac3122a3665218784e044f0f1a2a715`  
**Mục tiêu:** đưa concordance EU Annex I → HS2012 vào pipeline có thể audit độc lập, không chỉ sửa thủ công CSV.

---

## 1. Tóm tắt trạng thái hiện tại

Commit `256e572` đã đi đúng hướng:

- Đã tạo `concordance_review_package/data/concordance_release_long.csv`.
- Đã explode nhiều mapping one-to-many thành dạng one `eu_code` – one `hs6` per row.
- Đã xử lý các split quan trọng như rice, wheat, barley, rye, oat, maize, sorghum, soyabeans, cotton seeds.
- Đã thêm validator `concordance_review_package/scripts/validate_gpt_concordance_rules.py`.
- Đã loại literal `nan` khỏi nhiều ô `hs6`.

Tuy nhiên, **chưa nên coi `concordance_release_long.csv` hiện tại là final release**, vì còn lỗi logic ở tầng export:

1. Rule group-heading đang quá thô, có khả năng loại nhầm commodity hợp lệ chỉ vì `eu_code` kết thúc bằng `0000`.
2. Một số parent/group rows vẫn bị lọt vào `release_long` dù chúng span nhiều HS6.
3. Một số nhóm cần policy rõ trước khi release: tree nuts in-shell/shelled, spice whole/crushed, cherry parent-only vs parent+subitems, tea/coffee/cocoa/hops/algae có phải export không.

---

## 2. Yêu cầu bắt buộc: push nhật ký chỉnh sửa qua các vòng GPT ↔ cowork lên Git

Từ vòng này trở đi, đề nghị cowork **không chỉ push file dữ liệu**, mà push cả log để agent khác có thể audit pipeline.

Tạo hoặc cập nhật các file sau:

```text
concordance_review_package/reviews/ROUND_LOG.md
concordance_review_package/reviews/agent_rounds_log.csv
concordance_review_package/reviews/adjudication_decisions.csv
concordance_review_package/reviews/round_003_gpt_to_cowork_release_long_policy_and_logging.md
```

File Markdown này nên được commit vào đúng path:

```text
concordance_review_package/reviews/round_003_gpt_to_cowork_release_long_policy_and_logging.md
```

### 2.1. Mẫu `ROUND_LOG.md`

```markdown
# Concordance review round log

## Round 001 — Initial GPT independent audit
- Date:
- Actor:
- Source commit / input SHA:
- Files reviewed:
- Output files:
- Main findings:
- Follow-up required:

## Round 002 — Cowork fixes + GPT post-cowork proposal bundle
- Date:
- Actor:
- Source commit / input SHA:
- Files changed:
- Output files:
- Main findings:
- Follow-up required:

## Round 003 — Release_long export policy and audit-log requirement
- Date: 2026-06-29
- Actor: cowork, responding to GPT handoff
- Source commit: 256e572bfac3122a3665218784e044f0f1a2a715
- Files to change:
  - concordance_review_package/data/concordance_final_asean.csv
  - concordance_review_package/data/concordance_release_long.csv
  - concordance_review_package/scripts/build_release_long.py, if created
  - concordance_review_package/scripts/validate_release_long.py, if created
  - concordance_review_package/reviews/agent_rounds_log.csv
  - concordance_review_package/reviews/adjudication_decisions.csv
- Main issue:
  - Current group-heading export rule is too coarse.
  - Need explicit release_policy instead of relying on eu_code suffix.
```

### 2.2. Mẫu `agent_rounds_log.csv`

```csv
round_id,date,actor,source_commit,base_file,output_file,proposal_id,eu_code,eu_desc,before_hs6,after_hs6,action,status,rationale,evidence_file,reviewer,next_action
003,2026-06-29,cowork,256e572bfac3122a3665218784e044f0f1a2a715,concordance_final_asean.csv,concordance_release_long.csv,GPT_R3_EXPORT_POLICY,0610000,Teas,090210;090220;090230;090240,090210;090220;090230;090240,EXPORT_PRODUCT,accepted,"Tea is a commodity product even though eu_code ends with 0000; do not filter by suffix alone.",,cowork,
```

### 2.3. Mẫu `adjudication_decisions.csv`

```csv
decision_id,date,eu_code,eu_desc,issue_type,before_hs6,after_hs6,release_policy,decision,rationale,decided_by,reviewed_by,evidence_file,source_round
ADJ-003-001,2026-06-29,0610000,Teas,EXPORT_POLICY,"090210;090220;090230;090240","090210;090220;090230;090240",EXPORT_PRODUCT,accepted,"Valid commodity with HS2012 tea codes; suffix 0000 is not sufficient reason to exclude.",cowork,Opus/GPT,,003
```

**Quan trọng:** log phải ghi được “trước/sau”, lý do, ai quyết định, và round nào đề xuất. Agent khác chỉ cần đọc `ROUND_LOG.md`, `agent_rounds_log.csv`, `adjudication_decisions.csv`, và `release_long` là hiểu được pipeline.

---

## 3. Blocker chính cần sửa: không filter group bằng `eu_code.endswith("0000")`

Không dùng rule kiểu:

```python
if eu_code.endswith("0000"):
    exclude_from_release_long()
```

Rule này sai vì nhiều EU code kết thúc bằng `0000` vẫn là commodity hợp lệ hoặc có HS rõ. Thay vào đó, cần cột explicit:

```text
release_policy
```

Controlled vocabulary đề xuất:

```text
EXPORT_PRODUCT        # export dòng này vào release_long
EXPORT_CHILDREN_ONLY  # không export parent, dùng child rows
EXCLUDE_NEC           # loại Others/catch-all NEC
EXCLUDE_NONFOOD       # loại animal/nonfood/out-of-study
ADJUDICATE            # chưa đủ rõ, không export cho tới khi quyết định
```

Nên thêm thêm cột:

```text
release_reason
decision_round
last_reviewed_by
last_reviewed_date
evidence_file
```

Nếu chưa muốn đổi schema master ngay, có thể tạo file phụ:

```text
concordance_review_package/reviews/release_policy_overrides.csv
```

với schema:

```csv
eu_code,release_policy,release_reason,decision_round,last_reviewed_by,last_reviewed_date
```

---

## 4. Whitelist: các `eu_code` kết thúc `0000` nhưng không được loại máy móc

Các dòng sau cần được adjudicate theo hướng **EXPORT_PRODUCT** nếu thuộc scope nghiên cứu ASEAN/MRL:

```text
0610000  Teas
0620000  Coffee beans
0640000  Cocoa beans
0650000  Carobs/Saint John's breads
0700000  HOPS
0290000  Algae and prokaryotes organisms
```

Đề xuất mapping/policy:

```text
0610000 Teas -> 090210;090220;090230;090240
0620000 Coffee beans -> 090111;090112;090121;090122
0640000 Cocoa beans -> 180100
0650000 Carobs/Saint John's breads -> 121292
0700000 HOPS -> adjudicate 121010 only vs 121010;121020
0290000 Algae and prokaryotes organisms -> 121221 if edible algae only; consider 121229 only if non-food scope is included
```

Lưu ý: `0700000 HOPS` hiện từng được đề xuất `121010`, nhưng HS2012 cũng có `121020` cho hop cones ground/powdered/pellets/lupulin. Cần quyết định policy: RAC-only hay trade coverage broader.

---

## 5. Blacklist / cần `EXPORT_CHILDREN_ONLY`: parent/group rows không nên export đơn mã

Các dòng sau đang là parent/group rows hoặc span nhiều HS6. Không nên export một mã đại diện nếu chưa có policy rõ.

Tối thiểu cần rà lại:

```text
0161000  (a) edible peel
0162000  (b) inedible peel, small
0163000  (c) inedible peel, large
0231000  (a) Solanaceae and Malvaceae
0232000  (b) cucurbits with edible peel
0233000  (c) cucurbits with inedible peel
0241000  (a) flowering brassica
0251000  (a) lettuces and salad plants
0252000  (b) spinaches and similar leaves
0260000  Legume vegetables
0270000  Stem vegetables
0280000  Fungi, mosses and lichens
0300000  PULSES
0810000  Seed spices
0820000  Fruit spices
0840000  Root and rhizome spices
```

Đề xuất default:

```text
release_policy = EXPORT_CHILDREN_ONLY
```

Nếu cowork/Opus quyết định export parent group vì nghiên cứu cần group-level MRL, phải ghi rõ trong `adjudication_decisions.csv` và phải dùng multi-HS set đầy đủ, không dùng một mã đại diện quá hẹp.

---

## 6. `release_long` hiện còn dòng cần xem lại

Trong `concordance_release_long.csv` hiện có một số rows có khả năng là group/parent rows lọt vào release. Cần kiểm tra và quyết định:

```text
0161000  -> hiện 080430; có thể đang đại diện cho pineapple, không đủ cho edible-peel group
0162000  -> hiện 081070; parent group, không đủ cho all small inedible-peel fruits
0163000  -> hiện 080310; parent group, không đủ cho all large inedible-peel fruits
0231000  -> hiện 070999; parent Solanaceae/Malvaceae, không đủ vì children span 070200, 070930, 070960, 070999, etc.
0232000  -> hiện 070993; parent cucurbits edible peel, cần quyết định children only
0233000  -> hiện 080719; parent cucurbits inedible peel, children include melons/watermelons/pumpkins etc.
0241000  -> hiện 070410; group flowering brassica, có thể acceptable only if exactly broccoli+cauliflower group
0251000  -> hiện 070511; group lettuces and salad plants; too narrow if includes rocket/cress/etc.
0252000  -> hiện 070970; group spinaches and similar leaves; may be acceptable only if group scope is exactly spinach-like leaves
0633000  -> hiện 121190; root herbal infusion group; likely acceptable only as group if study intentionally aggregates herbal-infusion roots
```

Action: mark each as `EXPORT_CHILDREN_ONLY` or `EXPORT_PRODUCT` with explicit rationale.

---

## 7. Tree nuts policy còn chưa đóng

Hiện nhiều nut rows chỉ lấy mã in-shell. Nếu nghiên cứu trade cần bao phủ cả shelled, nên thêm cặp shelled.

Cần adjudicate các dòng sau:

```text
0120010 Almonds: current 080211; consider 080211;080212
0120020 Brazil nuts: current 080121; consider 080121;080122
0120030 Cashew nuts: current 080131; consider 080131;080132
0120040 Chestnuts: current 080241; consider 080241;080242
0120060 Hazelnuts/cobnuts: current 080221; consider 080221;080222
0120070 Macadamias: current 080261; consider 080261;080262
0120100 Pistachios: current 080251; consider 080251;080252
0120110 Walnuts: current 080231; consider 080231;080232
```

Nếu giữ only in-shell, phải ghi rationale: ví dụ “RAC definition / group source only maps to in-shell form”. Nếu mục tiêu là trade coverage, nên split cả in-shell và shelled.

---

## 8. Spice whole/crushed policy còn chưa đóng

Nhiều spice HS2012 tách:

```text
090411 vs 090412  pepper whole vs crushed/ground
090421 vs 090422  Capsicum/Pimenta dried whole vs crushed/ground
090510 vs 090520  vanilla whole vs crushed/ground
090611/090619 vs 090620 cinnamon whole vs crushed/ground
090710 vs 090720  cloves whole vs crushed/ground
090811 vs 090812  nutmeg whole vs crushed/ground
090821 vs 090822  mace whole vs crushed/ground
090831 vs 090832  cardamom whole vs crushed/ground
090921 vs 090922  coriander seeds whole vs crushed/ground
090931 vs 090932  cumin seeds whole vs crushed/ground
090961 vs 090962  anise/fennel/caraway/juniper whole vs crushed/ground
091011 vs 091012  ginger whole vs crushed/ground
```

Cần policy rõ:

```text
A. RAC-only / primary commodity only -> giữ whole/neither crushed nor ground nếu đó là RAC.
B. Trade-coverage -> include both whole and crushed/ground pairs.
```

Không nên để ngầm định. Ghi quyết định vào `adjudication_decisions.csv`.

---

## 9. Sweet cherry policy cần ghi rõ

`0140020 Cherries (sweet)` hiện đã chuyển sang `080929` trong `release_long`. Điều này hợp lý nếu policy là:

```text
parent/main commodity only
```

Nếu policy là:

```text
parent + all Annex subitems
```

thì cần thêm `080921` vì Annex có subitem sour cherries, còn HS2012 tách sour cherries (`080921`) và other cherries (`080929`).

Action: ghi một dòng adjudication:

```csv
ADJ-003-CHERRY,2026-06-29,0140020,Cherries (sweet),SUBITEM_SCOPE,080921,080929,EXPORT_PRODUCT,accepted_parent_only,"Use 080929 because parent commodity is sweet cherries; do not include sour-cherry subitem unless release policy covers all subitems.",cowork,Opus/GPT,,003
```

Hoặc nếu chọn full subitem scope:

```csv
ADJ-003-CHERRY,2026-06-29,0140020,Cherries (sweet),SUBITEM_SCOPE,080921,080921;080929,EXPORT_PRODUCT,accepted_parent_plus_subitems,"Include both sour and other cherries because Annex code contains sour-cherry subitem.",cowork,Opus/GPT,,003
```

---

## 10. Build/release requirements

`concordance_release_long.csv` nên là generated artifact, không sửa thủ công nếu có thể.

Đề xuất tạo script:

```text
concordance_review_package/scripts/build_release_long.py
concordance_review_package/scripts/validate_release_long.py
```

`build_release_long.py` nên:

1. Đọc `concordance_final_asean.csv`.
2. Đọc `release_policy_overrides.csv` nếu có.
3. Chuẩn hóa null: `"nan"`, `"NaN"`, empty-like values -> empty string.
4. Tách `hs6` theo `;`, comma, whitespace.
5. Chỉ export rows có `release_policy == EXPORT_PRODUCT`.
6. Không export `excluded_nec`, `excluded_nonfood`, `NO_HS6`, hoặc `needs_review` unresolved.
7. Không export group rows nếu `release_policy == EXPORT_CHILDREN_ONLY`.
8. Ghi one `eu_code` – one `hs6` per row.
9. Deduplicate `(eu_code, hs6)`.
10. Ghi thêm metadata nếu có thể:

```text
eu_code
eu_desc
hs6
annex1_legal_ref
release_policy
mapping_basis
decision_round
evidence_file
```

`validate_release_long.py` nên fail nếu:

```text
- hs6 missing / literal nan
- hs6 not exactly 6 digits
- hs6 not present in HS2012 source
- semicolon remains in hs6
- duplicate eu_code + hs6
- excluded_nec or excluded_nonfood row appears in release_long
- row marked EXPORT_CHILDREN_ONLY appears in release_long
- required whitelist commodity missing
- known group blacklist appears without explicit adjudication
```

---

## 11. Acceptance criteria cho PR tiếp theo

PR tiếp theo chỉ nên merge nếu đạt các điều kiện sau:

```text
[ ] ROUND_LOG.md updated
[ ] agent_rounds_log.csv updated
[ ] adjudication_decisions.csv updated
[ ] This handoff memo committed under reviews/
[ ] release_policy or release_policy_overrides.csv added
[ ] build_release_long.py added or current generation method documented
[ ] validate_release_long.py added or equivalent validator extended
[ ] Tea, coffee, cocoa, carobs, hops, algae adjudicated explicitly
[ ] Group/parent rows in release_long adjudicated explicitly
[ ] Tree nuts policy adjudicated explicitly
[ ] Spice whole/crushed policy adjudicated explicitly
[ ] Sweet cherry parent-only vs parent+subitems policy recorded
[ ] concordance_release_long.csv rebuilt
[ ] All HS6 in release_long exist in HS2012
[ ] No semicolon in release_long.hs6
[ ] No literal nan in release_long
[ ] No duplicate eu_code-hs6 pairs
[ ] No excluded_nec/nonfood rows in release_long
```

---

## 12. Suggested commit message

```text
Round 3: add explicit release policy, audit logs, and rebuild release_long

- Add GPT/cowork round log and machine-readable adjudication files
- Replace suffix-based group filtering with explicit release_policy
- Restore valid 0000 commodity exports where applicable: tea/coffee/cocoa/carobs/hops/algae after adjudication
- Mark true group headings as EXPORT_CHILDREN_ONLY
- Rebuild concordance_release_long with one eu_code-HS6 per row
- Add/extend release_long validator
```

---

## 13. Final note for cowork

Please do not treat this as a request to blindly accept GPT suggestions. The request is:

1. Adjudicate each policy issue explicitly.
2. Push both data changes and decision logs.
3. Make the pipeline auditable so a later agent can reconstruct why every row entered or did not enter `release_long`.

The key design change is moving from implicit rules like “code ending 0000 means group heading” to explicit release decisions recorded in version control.
