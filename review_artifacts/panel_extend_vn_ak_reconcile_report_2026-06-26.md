# Mở rộng panel MRL lát VN (7 mã) + Bảng đối chiếu A_k×RASFF — 2026-06-26

> Hai phần: **A** mở rộng panel ràng buộc cho 7 mã VN còn thiếu (đụng 04_ build, chỉ ĐỌC 01_ frozen); **B** dựng bảng đối chiếu A_k×RASFF (đầu vào quyết định, KHÔNG khóa A_k). Kèm **Bước 0** sửa rambutan. **DỪNG** chờ Claude/người dùng quyết định nghĩa A_k trước khi thiết kế chỉ số. Mọi quyết-định-tra-cứu kèm **dòng nguồn nguyên văn**.

---

## BƯỚC 0 — Sửa concordance: rambutan 0162020 → 0163060 (XÉT LẠI từ verify Annex I)

**Bằng chứng nguyên văn (catalogue `Pesticide-residues-products-All.csv`):**
```
[0162020] name='Litchis/lychees'  scientific='Litchi chinensis'
   synonyms='Baels, Longans, Marulas, Salaks/snake fruits, Spanish limes/mamoncillos/genips'
            → CÓ 'Longans', KHÔNG có rambutan

[0163060] name='Cherimoyas'  scientific='Annona cherimola'
   synonyms='Elephant apples, Ilamas, Mammey sapotes, Marmeladedos, Pulasans,
             Rambutans/hairy litchis, Sapodillas, Sweetsops/sugar apples, Wild sweetsops/custard apples'
            → 'Rambutans/hairy litchis' nằm Ở ĐÂY
```
**Hành động:** trong `concordance_final_vn_2026-06-26.csv`: (1) sửa note 0162020 = "Vải/litchi + NHÃN/longan; KHÔNG phủ chôm chôm"; (2) THÊM dòng **0163060 Cherimoyas → HS6 081090** (form=fresh, final_vn) cho **chôm chôm/rambutan + mãng cầu**. HS6 cả hai vẫn `081090` (chung heading 0810) **nhưng nguồn MRL KHÁC**: longan lấy panel 0162020, chôm chôm lấy panel **0163060**. (Backup: `*.bak_before_rambutan_2026-06-27`.) Lát VN nay **16 mã EU / 27 dòng**.

---

## PHẦN A — Mở rộng panel ràng buộc cho 7 mã VN

### A.1 Phương pháp (TÁI LẬP đúng panel đã chốt)
Hàm bậc thang trên **TOÀN BỘ** bản ghi snapshot frozen: MRL ràng buộc (chất, sản phẩm) năm t = bản ghi có `application_date` mới nhất **≤ 1/1 năm t** (biến thể robustness **31/12**); tie cùng ngày → dedup `mrl_value` rồi **Annex II>III>V** (phụ: regulation mới nhất); không có bản ghi ≤ mốc → `not_yet_set`; value NULL → `pending_celex_recovery` (KHÔNG impute). Năm 2024 = `is_robustness_year`. Tập chất = **A_k hiện tại (515 chất)**.

### A.2 KIỂM CHỨNG builder (tái lập khớp 100%)
Vì script panel gốc không lưu ở `04_/scripts/`, builder được **dựng lại + kiểm chứng cell-by-cell** với panel hiện hành cho **10 mã đang trong panel**:
```
ĐÃ ĐỐI CHIẾU: 50.750 ô (10 mã × ~507 chất × 10 năm, jan01)
SAI KHÁC: 0  (mrl_mg_kg, mrl_status, binding_application_date, included_in_annex đều khớp)
```
→ builder trung thành; áp cho 7 mã mới an toàn.

### A.3 Độ phủ 7 mã mới (jan01) — ĐẠT NGANG 9 mã OK
| eu_code | sản phẩm | #chất có MRL (ok) | #chất not_yet_set | #chất pending(null) | #ô-ok | #dòng |
|---|---|---|---|---|---|---|
| 0231040 | Đậu bắp/okra | **489** | 240 | 11 | 3836 | 5150 |
| 0162020 | Vải+Nhãn | **489** | 240 | 11 | 3836 | 5150 |
| 0162030 | Chanh leo | **489** | 240 | 11 | 3836 | 5150 |
| 0162040 | **THANH LONG** | **489** | 240 | 11 | 3836 | 5150 |
| 0163060 | Chôm chôm/mãng cầu | **489** | 240 | 11 | 3836 | 5150 |
| 0256040 | Parsley | **489** | 240 | 11 | 3836 | 5150 |
| 0256080 | Basil | **489** | 240 | 11 | 3836 | 5150 |

**489 chất × 10 năm = TRÙNG KHỚP** mức của 9 mã OK (citrus/ớt/xoài/sầu riêng/cà phê = 489; gạo 493; chè 490). **Thanh long (#2) ĐỦ độ phủ.** Không mã nào rỗng bất thường.

### A.4 Bằng chứng nguyên văn — thanh long lấy MRL từ 0162040
Catalogue: `[0162040] Prickly pears/cactus fruits | syn 'Pitayas/dragon fruits'`. Ví dụ **carbendazim** trên thanh long:
```
SNAPSHOT (0162040, chất 38 'Carbendazim and benomyl…'):
   01/01/2012 | 0.1* | Annex III | Applicable        | Reg.(EU) 559/2011
   01/01/2012 | 0.1* | Annex II  | Applicable        | Reg.(EU) 559/2011   ← chọn (Annex II > III)
   10/10/2010 | 0.1* | Annex II  | No longer applicable | Reg.(EU) 893/2010
PANEL mở rộng[0162040] chất 38, năm 2020 & 2024:
   bind_date=01/01/2012 | mrl=0.1* | mg_kg=0.1 | Annex II | status=ok
```
→ thanh long×carbendazim = **0.1 mg/kg** (KHÔNG phải LOD 0.01) — đúng bậc-thang + tie-break Annex II. (chlorpyrifos id56 → 0.01* Annex V 13/11/2020; fipronil id302 → 0.005* Annex V 18/05/2020.)

### A.5 Kiểm tra khóa & referential
- Khóa **(chất, sản phẩm, năm, reference)**: **0 trùng** (36.050 dòng jan01 + 36.050 dec31).
- Referential: mọi `mrl_value`/`application_date`/`annex` đều copy từ snapshot frozen (SHA-256 `bc3643ec…a798bb`), không sinh giá trị mới.
- Output: `04_/outputs/eu_mrl_binding_panel_vn_extended_jan01_2026-06-26.csv` + `…_dec31_…csv`.

---

## PHẦN B — Bảng đối chiếu A_k × RASFF T5 (đầu vào quyết định, KHÔNG khóa A_k)

`05_/ak_rasff_reconciliation_2026-06-26.csv`. MRL & độ phủ tính từ ô ràng buộc **jan01-2024** trên **17 mã VN lá** (10 in-panel + 7 mở rộng).

| substance | id | in_A_k | in_snap | in-window | #VN có MRL | typ MRL | rejection (T5) | flag |
|---|---|---|---|---|---|---|---|---|
| carbendazim | 38 | yes | yes | yes | 17 | 0.1 | 37 | |
| permethrin | 467 | yes | yes | yes | 17 | 0.05 | 32 | |
| chlorfenapyr | 48 | yes | yes | yes | 17 | 0.01 | 30 | |
| chlorpyrifos | 56 | yes | yes | yes | 17 | 0.01 | 28 | |
| tricyclazole | 394 | yes | yes | yes | 17 | 0.01 | 23 | |
| hexaconazole | 126 | yes | yes | yes | 17 | 0.01 | 21 | |
| **acetamiprid** | **10** | **NO** | yes | **no** | **0** | — | **21** | **MISSING_FROM_A_k** |
| propiconazole | 188 | yes | yes | yes | 17 | 0.01 | 20 | |
| dithiocarbamates | 83 | yes | yes | yes | 17 | 5.0 | 16 | |
| imidacloprid | 326 | yes | yes | yes | 17 | 0.01 | 15 | |
| carbofuran | 39 | yes | yes | yes | 17 | 0.01 | 15 | |
| dinotefuran | 2322 | yes | yes | (null) | 1 | 8.0 | 13 | pending_celex |
| profenofos | 186 | yes | yes | yes | 17 | 0.01 | 12 | |
| cypermethrin | 65 | yes | yes | yes | 17 | 2.0 | 11 | |
| acephate | 9 | yes | yes | yes | 17 | 0.01 | 10 | |
| methamidophos | 154 | yes | yes | yes | 17 | 0.01 | 10 | |
| dimethoate | 76 | yes | yes | yes | 17 | 0.01 | 8 | |
| fipronil | 302 | yes | yes | yes | 17 | 0.005 | 8 | |

### B.1 Phát hiện chính — **acetamiprid bị A_k BỎ SÓT** (21 rejection, KHÔNG trong A_k)
**Bằng chứng nguyên văn** (snapshot, chất 10 trên thanh long 0162040):
```
id=10 'Acetamiprid  (R)'   ← snapshot CHỈ có định nghĩa dư lượng REVISED (R)
   20/08/2025 | 0.01* | Annex II | No longer applicable | Reg.(EU) 2025/1212
   12/05/2026 | 0.01* | Annex II | Applicable           | Reg.(EU) 2026/876
   → record sớm nhất 20/08/2025 = SAU cửa sổ 2015–2024 → not_yet_set MỌI năm in-window
A_k name chứa 'acetamiprid' = [] (không có)
```
→ acetamiprid (#6–7 theo tần suất rejection) **vừa MISSING_FROM_A_k vừa không có MRL ràng buộc 2015–2024** trong snapshot, vì EU đã **sửa định nghĩa dư lượng** sang biến thể "(R)" (chỉ có record 2025+); định nghĩa CŨ (in-window) **không còn** trong snapshot product records. **Ứng viên #1 cần Claude quyết:** thêm acetamiprid vào A_k VÀ khôi phục MRL in-window từ định nghĩa cũ/CELEX.

### B.2 Caveat trung thực — dinotefuran (trong A_k nhưng MRL NULL)
```
id=2322 'Dinotefuran' (0162040): 05/06/2014 | val=None (NULL) | Annex III | Applicable | Reg.(EU) 491/2014
   → pending_celex_recovery 16/17 mã VN; chỉ 1 mã có giá trị số (8.0)
```
→ dinotefuran trong A_k nhưng giá trị thuộc nhóm 40-null đã ghi (cần CELEX recovery trước khi vào chỉ số).

### B.3 Ánh xạ chất nguyên văn (RASFF → snapshot residue definition)
Khớp tên (substring) → định nghĩa dư lượng chính thức trong snapshot; loại biến thể `-methyl`/`(R)` trùng tên:
```
carbendazim → id38 'Carbendazim and benomyl (sum… expressed as carbendazim) (R)'  [A_k]  (id3310 'Carbendazim (R)' = PLAN tương lai, bỏ)
permethrin  → id467 'Permethrin (sum of isomers) (F)'                              [A_k]
chlorpyrifos→ id56  'Chlorpyrifos (F)'                                             [A_k]  (id57 chlorpyrifos-methyl = chất khác, bỏ)
dithiocarbamates → id83 'Dithiocarbamates (… maneb, mancozeb, metiram, propineb, thiram, ziram)' [A_k]
carbofuran  → id39  'Carbofuran (sum of carbofuran… and 3-OH carbofuran…) (R)'     [A_k]
fipronil    → id302 'Fipronil (sum fipronil + sulfone metabolite… )(F)'           [A_k]
acetamiprid → id10  'Acetamiprid (R)'                                             [KHÔNG A_k]
```
(18 chất còn lại id: tricyclazole 394, hexaconazole 126, propiconazole 188, imidacloprid 326, dinotefuran 2322, profenofos 186, cypermethrin 65, acephate 9, methamidophos 154, dimethoate 76 — tất cả trong A_k.)

### B.4 Chất A_k KHÔNG gây rejection VN (ứng viên ngoài-lề)
A_k = **515** chất; A_k ∩ RASFF-T5 = **17**; → **498 chất A_k KHÔNG xuất hiện trong bất kỳ rejection VN nào** (T5). Đây là ứng viên cho phần trọng-số/validation (chất EU siết nhưng VN chưa từng bị bắt) — KHÔNG tự loại, chờ thiết kế chỉ số.

---

## PHẦN C — Quy tắc bằng chứng nguyên văn (đã cố định vào Cẩm nang)
Đã thêm **CHUẨN THƯỜNG TRỰC** vào `00_/Cam_Nang…md` + dòng checklist audit + ghi `analytical_decisions_log`. (Lỗi rambutan 0162020→0163060 là ví dụ: tóm tắt giấu lỗi, grep nguyên văn bắt được.)

---

## DỪNG
Panel 7 mã VN đã mở rộng (489 chất × 10 năm, thanh long ĐỦ). Bảng đối chiếu cho thấy **acetamiprid MISSING_FROM_A_k** + dinotefuran null. **KHÔNG tự thêm/bớt A_k, KHÔNG dựng chỉ số.** Chờ Claude/người dùng quyết định nghĩa A_k (membership).
