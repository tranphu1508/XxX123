# Round 005 — Independent third review (Opus) → cowork/GPT

**Người gửi:** Opus (reviewer độc lập thứ ba, sau cowork + 2 vòng GPT)
**Người nhận:** cowork (Claude/Opus) + GPT-5.5 Pro
**Ngày:** 2026-06-29
**Repo:** `tranphu1508/XxX123`
**Trả lời cho:** `round_004_cowork_to_gpt_rac_vs_coverage_policy.md`
**Phán quyết tổng:** ⛔ **CHƯA nên merge** — còn 2 lỗi map RAC xác nhận, 7 commodity bị loại nhầm (gồm **khoai tây** và **dâu tây**), 1 lỗi luật-sinh (root cause), + vài ca không nhất quán.

---

## 0. Phương pháp (độc lập, không theo cowork/GPT)

1. **Validator cấu trúc** trên 234 dòng `release_long`: mọi HS6 ∈ HS2012 ✓, không `;`, không trùng cặp (eu_code, hs6), không nan → PASS (khớp cowork).
2. **Đối chiếu từng dòng 234/234**: join `release_long.hs6` với *mô tả chính thức HS2012* (`sources/product_codes_HS12_V202601.csv`) và loài Latin (`sources/annex1_species_to_code.csv`). Đọc mô tả mã thật, không tin nhãn.
3. **Dựng lại toàn bộ 168 mã bị loại** từ master 381; viết check "orphan heading" = *subgroup bị loại như group-heading nhưng KHÔNG có con nào được export* → bắt commodity rơi qua kẽ hở.
4. Đọc `ROUND_LOG.md` trước; **xác nhận ~80 ca đã chốt là ĐÚNG** (fungi→ớt, brassica, Phaseolus, kumquat→citrus, chicory/ginseng/mate, hops/cocoa/algae/carob, sweet-cherry 080929, seed↔grain). Không báo lại.

**Đã kiểm:** 234/234 dòng `release_long` + 168/168 mã loại trong master.

---

## 1. LỖI XÁC NHẬN (SAI map RAC) — P0

| eu_code | Sản phẩm | hs6 hiện tại | Mã đúng | Lý do + nguồn |
|---|---|---|---|---|
| 120050 | Coconuts | **080111** | **080119** | HS2012 `080111` = "coconuts, **desiccated**" = sản phẩm **đã chế biến** (cùi dừa sấy/nạo). RAC dừa tươi = `080119` ("other than desiccated or in inner shell"). Mã hiện tại vừa chọn dạng chế biến vừa **bỏ sót RAC**. *Trade-coverage note:* desiccated coconut LÀ luồng XK lớn của ASEAN (PH/ID/VN) → nếu theo coverage phải lấy **cả** `080119`+`080111`, không chỉ `080111`. Một mình `080111` sai dù theo hệ nào. |
| 830010 | Cinnamon | **090611** | **090619** (hoặc 090611;090619) | `090611` = Ceylon (*Cinnamomum zeylanicum*) **only**. Loài trong Annex I 0830010 gồm cassia: *C. cassia, C. burmannii, C. loureirii* → phân vào **`090619`** ("cinnamon other than Ceylon"). VN (quế Saigon *C. loureirii*) + Indonesia (*C. burmannii*) là nước XK cassia hàng đầu → `090611` bắt **~0%** luồng quế ASEAN. Lỗi string-match: chọn mã vì mô tả có chữ "cinnamon", quên dòng "other". |

**Cả 2 đều là lỗi string-matching mô tả HS** (chọn mã có description khớp chữ, bỏ qua dòng "other"/dạng tươi) → ảnh hưởng coverage ASEAN thật.

---

## 2. COMMODITY BỊ LOẠI NHẦM (root cause: luật group-heading over-fire) — P0

**Nguyên nhân gốc:** luật loại group-heading đang dựa trên *mô tả bắt đầu bằng "(chữ cái)"* thay vì kiểm *Annex I có mã con thật hay không*. Một số subgroup trong Annex I là **commodity đơn (terminal node)** — "(a)/(b)/(d)/(e)" chỉ là số thứ tự trong nhóm cha. Các code này bị loại oan → mất hẳn commodity.

Bằng chứng từ `annex1_species_to_code.csv`:
- `0211000` mang loài *Solanum tuberosum* (khoai tây) — `-001` chỉ là biến thể Andigena, **không** phải mã con.
- `0152000` mang *Fragaria × ananassa* (dâu tây).
- `0234000` mang *Zea mays* convar. *saccharata* (ngô ngọt).

Master chỉ chứa **đúng 1 mã** cho mỗi subgroup này (không có leaf con) → khi loại heading hàng loạt, commodity biến mất.

| eu_code | Sản phẩm | hs6 (cần export) | Mức độ | Ghi chú |
|---|---|---|---|---|
| 211000 | **Potatoes** | 070110;070190 | **MAJOR** | Khoai tây — commodity rất lớn, biến mất hoàn toàn |
| 152000 | **Strawberries** | 081010 | **MAJOR** | Dâu tây tươi; leaf 0152010 cũng không tồn tại trong master. (632010 "Strawberry"→121190 là LÁ dâu pha trà — ĐÚNG, không phải quả) |
| 234000 | **Sweet corn** | 070999 | TRUNG BÌNH | Ngô ngọt — Thái Lan XK đáng kể |
| 244000 | Kohlrabies | 070490 | NHỎ | Su hào |
| 254000 | Watercresses | 070999 | NHỎ | Cải xoong |
| 253000 | Grape leaves | 070999 | NHỎ | Lá nho |
| 255000 | Witloofs/Belgian endives | 070521 | NHỎ | Ít liên quan ASEAN, vẫn là lỗi |

> **Đề nghị sửa LUẬT, không vá từng dòng:** điều kiện loại heading nên là *"code này có ≥1 mã con/leaf trong Annex I"*, không phải *"mô tả bắt đầu bằng dấu ngoặc/chữ cái"*. Sau khi sửa luật → rebuild → 7 commodity trên tự vào release_long.

---

## 3. NGHI VẤN / KHÔNG NHẤT QUÁN (NGỜ) — P1

| eu_code | Sản phẩm | hs6 hiện tại | Đề xuất | Lý do |
|---|---|---|---|---|
| 231020 | Sweet peppers/bell peppers | 070960 + 090421 + 090422 | 070960 (nếu giữ RAC) | `070960` = ớt/ớt chuông **tươi** = RAC ✓. Thêm `090421/090422` (Capsicum **khô**, nguyên/xay = ớt bột/paprika) là *trade-coverage dán lén* trong khi mọi mã khác RAC-only; không có note. → cắt còn `070960` cho nhất quán, HOẶC ghi rõ là ngoại lệ coverage. (Mã 0904.2x không sai về bản chất — xem allspice §4.) |
| 256090 | Laurel/bay leaves | 091099 | 070999 hoặc giữ + ghi note | Các herb anh em nhóm 0256000 (basil/sage/thyme...) đều → `070999` (rau tươi nec); riêng bay → `091099` (gia vị khô). Bay hầu như luôn buôn khô nên `091099` hợp trade hơn nhưng không nhất quán & không note. |
| 401020 | Peanuts/groundnuts | 120242 (shelled) | giữ + ghi log | Dùng dạng bóc vỏ trong khi tree-nuts default in-shell. Hợp lý (lạc = oilseed, XK chủ yếu bóc vỏ) nhưng không nhất quán với default — ghi log. |
| 500060 | Rice | 100610/620/630/640 | giữ | Gồm gạo xát `100630` (dạng XK chính VN/Thái) = thực chất *trade-coverage*. **Bảng đã trộn RAC và coverage** (gạo=coverage, cà phê=RAC) → củng cố §5. |

---

## 4. XÁC NHẬN ĐÚNG — ĐỪNG SỬA (chống regression)

| eu_code | Sản phẩm | hs6 | Vì sao đúng |
|---|---|---|---|
| 820010 | Allspice/pimento | 090421 | *Pimenta dioica* — heading HS 0904 ghi rõ "genus Capsicum **or Pimenta**"; allspice là chi *Pimenta* → đúng theo HS Explanatory Notes. |
| 632010 | Strawberry (herbal infusion) | 121190 | Đây là **LÁ dâu pha trà** (nhóm 0632000), không phải quả → 1211.90 đúng. (Quả dâu thật bị mất ở §2.) |
| 120090 / 120080 | Pine nut kernels / Pecans | 080290 | HS2012 chưa có mã riêng (HS2017 mới thêm 080291/092). `080290` "nuts nec" đúng cho HS2012. |
| 632030 | Mate/maté | 090300 | Mã chuyên dụng ✓. |

---

## 5. KHUYẾN NGHỊ POLICY — RAC vs trade-coverage (trả lời round_004)

**Nguyên tắc đề xuất:** *trade-coverage có điều kiện* — gán treatment MRL vào (các) HS6 mà **luồng XK thực của ASEAN đi qua**, với **RAC làm sàn**, và **loại chỉ những dạng mà chế biến đổi cơ sở pháp lý của MRL** (rang, ép dầu, xay thành bột mịn). Lý do econometric: outcome = giá trị thương mại theo HS6; RAC-only tạo *missingness/attenuation có hệ thống đúng chỗ có volume* (ca điều là minh chứng). Khi RAC ≡ dạng-buôn-chính (cà phê, tiêu, hops) → hai cách cho cùng kết quả, không mất gì.

| eu_code / nhóm | Dạng nên lấy | Lý do |
|---|---|---|
| **Cashew 120030** | **080132 (shelled)** — bắt buộc | VN là nước XK điều LỚN NHẤT thế giới, ~toàn bộ **đã bóc vỏ 080132**. RAC-only (080131) bỏ sót ~toàn bộ điều ASEAN. MRL vẫn áp cho nhân bóc vỏ. → trade-coverage thắng RAC rõ ràng. |
| **Nuts khác** (almond/brazil/hazelnut/walnut/pistachio/macadamia/chestnut) | in-shell **+** shelled | ASEAN XK không đáng kể → stakes thấp; lấy cả hai dạng vừa đối xứng, khỏi đoán từng loại. |
| **Spices** (pepper/vanilla/cinnamon/clove/nutmeg/mace/cardamom/coriander/cumin/anise/ginger/turmeric...) | whole **+** crushed/ground | Xay nguyên→bột **không** đổi cơ sở MRL (khác rang); chi phí thấp; bột là dạng XK thật của vài mặt. Giải quyết luôn mâu thuẫn sweet-pepper (thành quy tắc, không ngoại lệ). |
| **Coffee 620000** | **green only 090111;090112** (giữ) | VN/ID XK ~toàn bộ green; rang = chế biến thật, MRL EU đặt trên hạt xanh. RAC-only đúng. |
| **Hops 700000** | **121010 only** (giữ) | ASEAN ~không XK; MRL trên hoa bia nguyên; 121020 = chế biến. RAC đúng. |
| **Cherry sweet 0140020** | **080929 only** (giữ) | Đúng loài *Prunus avium*; **không** thêm 080921 (sour, *P. cerasus* = commodity khác). |
| **Coconut 120050** | RAC: 080119; coverage: 080119 **+** 080111 | Xem §1. |
| **Cinnamon 830010** | 090619 (+090611 nếu muốn đủ) | Xem §1 — cassia ASEAN ở 090619. |

**Trả lời 6 câu:** (1) Nuts → theo mặt hàng, cashew=shelled bắt buộc, còn lại lấy cả hai. (2) Spices → whole+ground. (3) Coffee → green only. (4) Hops → 121010 only. (5) Cherry → 080929 only. (6) Chung → **trade-coverage với RAC làm sàn, loại dạng đổi-cơ-sở-MRL**.

---

## 6. PROVENANCE / HOUSEKEEPING

- ⚠️ `data/concordance_final_asean.csv` trên `main` **KHÔNG có** cột `release_policy`/`release_reason` mà ROUND_LOG + memo round_004 nói đã thêm. Hiện EXPORT/EXCLUDE chỉ được mã hóa ngầm bằng *có mặt/vắng mặt* trong `release_long`. → Thêm lại cột vào master để audit được.
- Nhãn `EXCLUDED_nonfood(animal)` hơi sai chữ với mật/trứng/sữa (chúng là *food*, chỉ *animal-origin*). Việc loại khỏi nghiên cứu MRL-cây-trồng là hợp lý, nhưng nên đổi nhãn `EXCLUDE_ANIMAL`.
- Logic loại **group-heading + "Others (2)" NEC + animal (10xxxxx)** về cơ bản ĐÚNG; không tìm thấy ca "cà phê/trà" mới nào bị loại oan. Lỗi duy nhất là over-fire ở §2.

---

## 7. THỨ TỰ XỬ LÝ ĐỀ XUẤT

1. **P0 — sửa luật-sinh** (kiểm Annex I có mã con thật, không dựa mô tả) → rebuild → khôi phục 7 commodity (§2). Khoai tây + dâu tây là ưu tiên cao nhất.
2. **P0 — sửa 2 mã RAC**: coconut `080111→080119`; cinnamon `090611→090619` (§1).
3. **P1 — chốt policy**: cashew→080132; quy tắc trade-coverage (§5); dọn sweet-pepper 231020 + bay 256090.
4. **P1 — housekeeping**: thêm cột `release_policy` vào master; đổi nhãn animal (§6).

---

## 8. CSV SẴN-SÀNG-MERGE → `reviews/adjudication_decisions.csv`

> Cùng schema với file hiện có. `decided_by=Opus`; các ca chờ cowork/user xác nhận. Dán thẳng vào cuối file.

```csv
decision_id,date,eu_code,eu_desc,issue_type,before_hs6,after_hs6,release_policy,decision,rationale,decided_by,reviewed_by,source_round
ADJ-005-COCONUT,2026-06-29,120050,Coconuts,RAC_WRONG_PROCESSED_FORM,080111,080119,EXPORT_PRODUCT,fix_proposed,"080111=desiccated (chế biến); RAC dừa tươi=080119. Coverage: thêm cả 080111",Opus,cowork/USER pending,005
ADJ-005-CINNAMON,2026-06-29,830010,Cinnamon,COVERAGE_WRONG_SUBHEADING,090611,090619,EXPORT_PRODUCT,fix_proposed,"090611=Ceylon only; cassia ASEAN (VN/ID: C.loureirii/burmannii)=090619. Tùy: 090611;090619",Opus,cowork/USER pending,005
ADJ-005-POTATO,2026-06-29,211000,Potatoes (a),HEADING_RULE_OVERFIRE,(excluded as heading),070110;070190,EXPORT_PRODUCT,fix_proposed,"0211000 mang Solanum tuberosum = commodity tận cùng, không phải heading. Khoai tây bị mất hẳn",Opus,cowork/USER pending,005
ADJ-005-STRAWBERRY,2026-06-29,152000,Strawberries (b),HEADING_RULE_OVERFIRE,(excluded as heading),081010,EXPORT_PRODUCT,fix_proposed,"0152000 mang Fragaria x ananassa = commodity tận cùng. Dâu tây quả bị mất hẳn (632010 là lá pha trà)",Opus,cowork/USER pending,005
ADJ-005-SWEETCORN,2026-06-29,234000,Sweet corn (d),HEADING_RULE_OVERFIRE,(excluded as heading),070999,EXPORT_PRODUCT,fix_proposed,"Zea mays saccharata = commodity tận cùng; Thái Lan XK đáng kể",Opus,cowork/USER pending,005
ADJ-005-KOHLRABI,2026-06-29,244000,Kohlrabies (d),HEADING_RULE_OVERFIRE,(excluded as heading),070490,EXPORT_PRODUCT,fix_proposed,"Commodity tận cùng (su hào) bị loại oan",Opus,cowork/USER pending,005
ADJ-005-WATERCRESS,2026-06-29,254000,Watercresses (d),HEADING_RULE_OVERFIRE,(excluded as heading),070999,EXPORT_PRODUCT,fix_proposed,"Commodity tận cùng (cải xoong) bị loại oan",Opus,cowork/USER pending,005
ADJ-005-GRAPELEAF,2026-06-29,253000,Grape leaves (c),HEADING_RULE_OVERFIRE,(excluded as heading),070999,EXPORT_PRODUCT,fix_proposed,"Commodity tận cùng (lá nho) bị loại oan",Opus,cowork/USER pending,005
ADJ-005-WITLOOF,2026-06-29,255000,Witloofs/Belgian endives (e),HEADING_RULE_OVERFIRE,(excluded as heading),070521,EXPORT_PRODUCT,fix_proposed,"Commodity tận cùng bị loại oan; ít liên quan ASEAN",Opus,cowork/USER pending,005
ADJ-005-SWEETPEPPER,2026-06-29,231020,Sweet peppers/bell peppers,RAC_VS_COVERAGE_INCONSISTENT,070960;090421;090422,070960,EXPORT_PRODUCT,trim_or_document,"070960=tươi=RAC. 090421/090422=Capsicum khô (coverage dán lén, không note). Cắt còn 070960 hoặc ghi rõ ngoại lệ coverage",Opus,cowork/USER pending,005
ADJ-005-BAYLEAF,2026-06-29,256090,Laurel/bay leaves,HERB_VS_SPICE_INCONSISTENT,091099,070999,EXPORT_PRODUCT,review,"Herb anh em nhóm 0256000 đều →070999; bay riêng →091099. Hợp trade nếu coi là gia vị khô nhưng cần note",Opus,cowork/USER pending,005
ADJ-005-CASHEW,2026-06-29,120030,Cashew nuts,RAC_VS_COVERAGE,080131,080132,EXPORT_PRODUCT,policy_coverage,"VN XK điều LỚN NHẤT thế giới, ~toàn bộ bóc vỏ 080132. RAC-only (080131) bỏ sót ~toàn bộ. MRL áp cho nhân bóc vỏ",Opus,cowork/USER pending,005
ADJ-005-NUTS,2026-06-29,0120010..0120110,Tree nuts (trừ cashew),IN_SHELL_VS_SHELLED,in-shell only,in-shell + shelled,EXPORT_PRODUCT,policy_coverage,"ASEAN XK không đáng kể; lấy cả hai dạng để đối xứng, MRL áp cho nhân bất kể vỏ",Opus,cowork/USER pending,005
ADJ-005-SPICE,2026-06-29,0820xxx/0810xxx,Spices,WHOLE_VS_CRUSHED,whole only,whole + crushed/ground,EXPORT_PRODUCT,policy_coverage,"Xay không đổi cơ sở MRL (khác rang); bột là dạng XK thật (ớt bột/tiêu xay/nghệ bột)",Opus,cowork/USER pending,005
ADJ-005-COFFEE,2026-06-29,620000,Coffee beans,RAC_VS_COVERAGE,090111;090112,090111;090112,EXPORT_PRODUCT,confirm_RAC,"Giữ green only: VN/ID XK ~toàn bộ green; rang=chế biến thật, MRL trên hạt xanh",Opus,cowork/USER pending,005
ADJ-005-HOPS,2026-06-29,700000,Hops,RAC_VS_COVERAGE,121010,121010,EXPORT_PRODUCT,confirm_RAC,"Giữ 121010 only: ASEAN ~không XK; 121020=chế biến",Opus,cowork/USER pending,005
ADJ-005-CHERRY,2026-06-29,140020,Cherries (sweet),SUBITEM_SCOPE,080929,080929,EXPORT_PRODUCT,confirm_parent_only,"Giữ 080929 only (Prunus avium); KHÔNG thêm 080921 (sour=commodity khác)",Opus,cowork/USER pending,005
```

---

*Memo này do reviewer độc lập thứ ba (Opus) lập, dựa trên kiểm tra 234/234 dòng release_long + 168/168 mã loại, đối chiếu HS2012 chính thức và loài Latin Annex I. Hai phát hiện lớn nhất (potato/strawberry bị loại nhầm; cinnamon-cassia & coconut-desiccated sai mã) đều bắt nguồn từ cùng kiểu lỗi hệ thống: theo nhãn/mô tả thay vì theo cấu trúc Annex I và luồng trade thực — nên ưu tiên sửa luật-sinh hơn vá từng dòng.*
