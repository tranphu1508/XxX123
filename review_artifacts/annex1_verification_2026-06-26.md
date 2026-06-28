> Bản sao chỉ-đọc của 03_/annex1_verification_2026-06-26.md, cập nhật 2026-06-26.

# Verify phân loại Annex I cho mã VN — BẰNG CHỨNG NGUYÊN VĂN — 2026-06-26

> Kiểm độc lập 3 mã giải-bằng-synonym (thanh long 0162040, longan/nhãn 0162020, ớt cay 0231020). **Dán bằng chứng THÔ để Claude tự đọc + phán định.** KHÔNG sửa concordance ở task này.

## Nguồn Annex I (Bước 1)
- **A. SANTE products taxonomy:** ✅ CÓ (frozen snapshot 2026-05-27 = output endpoint `pesticide-residues-products`). Raw: `outputs/annex1_verify/annex1_taxonomy_vn_2026-06-26.json` (15 mã VN, đủ trường name/scientific/synonyms/parent/type).
- **B. EUR-Lex (Annex I pháp lý nguyên văn):** ❌ **BỊ CHẶN** — `web_fetch` CELEX:32018R0062 trả rỗng (trang JS, như EUR-Lex các lần trước).
- **C. Để người dùng tự kiểm legal text** (mở trình duyệt): bản hợp nhất `https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02005R0396` và act sửa Annex I `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R0062`. Cần tìm: 0162040 'Prickly pears/cactus fruits' có liệt pitaya/dragon fruit không; longan & rambutan nằm mã nào; có 0162990 'Others' riêng không.

## Grep frozen MRL snapshot (product_name): pitaya/dragon/longan/rambutan = **0 hit** → đúng (đây là synonym, không phải tên chính → không có trong trường product_name của snapshot MRL; bằng chứng phải lấy từ catalogue taxonomy).

---

## Mã 1 — Thanh long → 0162040
**Dòng nguyên văn (catalogue):**
```
[0162040] (b) inedible peel, small
  name       : Prickly pears/cactus fruits
  scientific : Opuntia ficus-indica
  synonyms   : Pitayas/dragon fruits, Red pitayas, Saguaro fruits, ...
```
**Grep `pitaya|pitahaya|dragon|hylocereus|selenicereus` TOÀN catalogue (mọi mã):**
```
0162040 | Prickly pears/cactus fruits | hit={Pitaya, pitaya, dragon} | trong: synonyms
0632010 | Strawberry (nhóm 0632 'leaves and herbs')| hit={dragon} | trong: synonyms  ← FALSE POSITIVE (từ "dragon" trong danh mục thảo mộc/trà, KHÔNG phải dragon fruit)
```
**Phán định:** **XÁC NHẬN (theo catalogue)** — "Pitaya/dragon fruit" chỉ xuất hiện ở **0162040** (hit 0632010 là từ "dragon" trong synonym thảo mộc, không phải quả). KHÔNG có ở 0162990. *Annex I pháp lý: CHƯA KIỂM ĐƯỢC (EUR-Lex bị chặn).*

## Mã 2 — Longan/nhãn (+ chôm chôm) → 0162020 ⚠
**Dòng nguyên văn (catalogue):**
```
[0162020] (b) inedible peel, small
  name       : Litchis/lychees
  scientific : Litchi chinensis
  synonyms   : Baels, Longans, Marulas, Salaks/snake fruits, ...
```
**Grep `longan|rambutan|dimocarpus|nephelium` TOÀN catalogue:**
```
0162020 | Litchislychees | hit={Longan} | trong: synonyms
0163060 | Cherimoyas     | hit={Rambutan} | trong: synonyms   ← RAMBUTAN nằm mã KHÁC!
```
**Phán định:** **Longan → XÁC NHẬN 0162020** (synonym "Longans" chung vải/litchi). **Rambutan → XÉT LẠI:** bằng chứng cho thấy rambutan là synonym của **0163060 'Cherimoyas'** (nhóm 0163 lớn-vỏ-không-ăn), **KHÔNG phải 0162020**. → HS6 cả hai vẫn 081090, NHƯNG **nguồn MRL khác**: longan=0162020, rambutan=**0163060**. (Phase 3b từng gộp longan+rambutan vào 0162020 — cần Claude xem lại rambutan.)

## Mã 3 — Ớt cay → 0231020
**Dòng nguyên văn (catalogue):**
```
[0231020] (a) Solanaceae and Malvaceae
  name       : Sweet peppers/bell peppers
  scientific : Capsicum annuum
  synonyms   : Chili peppers, Chili peppers, Chili peppers, Chili peppers, Chili peppers
```
**Grep `chili|chilli|capsicum` TOÀN catalogue:**
```
0231020 | Sweet peppersbell peppers | hit={Capsicum, Chili} | (Capsicum ở scientific, Chili ở synonyms)
```
**Phán định:** **XÁC NHẬN (theo catalogue)** — "chili/Capsicum" chỉ xuất hiện ở **0231020**; KHÔNG có mã ớt-cay riêng → ớt cay & ớt ngọt chung 0231020, MRL Capsicum dùng chung. *Annex I pháp lý: CHƯA KIỂM ĐƯỢC.*

---

## Tóm tắt phán định (3 mã)
| mã | sản phẩm | phán định | ghi chú |
|---|---|---|---|
| 0162040 | Thanh long | **XÁC NHẬN** (catalogue) | pitaya/dragon chỉ ở 0162040 |
| 0162020 | Longan | **XÁC NHẬN** (catalogue) | synonym "Longans" |
| (0163060) | **Rambutan** | **XÉT LẠI** | rambutan là synonym của 0163060 Cherimoyas, KHÔNG phải 0162020 → MRL khác |
| 0231020 | Ớt cay | **XÁC NHẬN** (catalogue) | không có mã ớt-cay riêng |

Mọi phán định "XÁC NHẬN" chỉ dựa **catalogue taxonomy** (= Annex I máy-đọc); **legal text Annex I (EUR-Lex) CHƯA KIỂM** (bị chặn). KHÔNG sửa concordance — chờ Claude (đặc biệt rambutan).
