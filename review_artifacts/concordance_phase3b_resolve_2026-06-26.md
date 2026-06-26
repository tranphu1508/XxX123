> Bản sao chỉ-đọc của 03_/concordance_phase3b_resolve_2026-06-26.md, cập nhật 2026-06-26.

# Concordance Phase 3b — GIẢI cờ + đối chiếu MRL → FINAL lát VN — 2026-06-26

> ✅ **Lát VN gọi FINAL:** 2 cờ đã giải bằng trường synonyms catalogue; **KHÔNG có cờ ĐỎ** MRL-coverage. ⚠ Cờ VÀNG: 6 mã VN có MRL trong snapshot nhưng CHƯA vào A_k/panel → mở rộng A_k ở bước thiết kế chỉ số (KHÔNG đụng 05_ ở task này; chỉ ĐỌC 04_).

## 1. Tra catalogue — 3 sản phẩm còn cờ (giải bằng synonyms)
| sản phẩm | mã EU | cơ sở (catalogue) | HS6 | nguồn MRL |
|---|---|---|---|---|
| **Ớt cay/chili** | **0231020** (chung ớt ngọt) | synonym field = 'Chili peppers' (Capsicum annuum) → KHÔNG có mã riêng | 070960 + 0904.21/22 | **MRL Capsicum 0231020 dùng chung ớt cay+ngọt** (panel có) |
| **Thanh long** | **0162040** 'Prickly pears/cactus fruits' | synonym = 'Pitayas/dragon fruits, Red pitayas' (cùng cụm cactus, 0162 nhỏ-vỏ-không-ăn) | 081090 | **MRL từ 0162040** (snapshot 691 chất; KHÔNG phải 'Others' đoán) |
| **Nhãn/longan + chôm chôm** | **0162020** (chung vải/litchi) | synonym = 'Longans' (Litchi chinensis nhóm) | 081090 | MRL từ 0162020 |
→ Cả 3 đều có mã EU thực (qua synonyms), KHÔNG cần đoán 'Others'. (Phase 3 trước đoán thanh long rơi 'Others' — nay SỬA: là 0162040 cactus.)

## 2. Sửa nhỏ — cà phê rang
- Cà phê: **nhân xanh 090111/090112 = RAC, GIỮ mẫu chính**; **rang 090121/090122 → `processed`** (VN xuất gần như toàn nhân xanh). Đã cập nhật `concordance_final_vn`.

## 3. ĐỐI CHIẾU PANEL MRL (đọc 04_) — `vn_product_x_mrl_coverage.csv`
| mã EU | sản phẩm | trong panel? | #chất MRL | #năm | nguồn | cờ |
|---|---|---|---|---|---|---|
| 0110010 | Bưởi | yes | 489 | 10 | panel (A_k) | OK |
| 0110020 | Cam | yes | 489 | 10 | panel (A_k) | OK |
| 0110030 | Chanh | yes | 489 | 10 | panel (A_k) | OK |
| 0110050 | Quýt | yes | 489 | 10 | panel (A_k) | OK |
| 0231020 | ỚT cay/ngọt | yes | 489 | 10 | panel (A_k) | OK |
| 0231040 | Đậu bắp | no | 691 | (snapshot) | snapshot — CHƯA vào A_k/panel | YELLOW: cần mở rộng A_k |
| 0162020 | Vải+Nhãn | no | 691 | (snapshot) | snapshot — CHƯA vào A_k/panel | YELLOW: cần mở rộng A_k |
| 0162030 | Chanh leo | no | 691 | (snapshot) | snapshot — CHƯA vào A_k/panel | YELLOW: cần mở rộng A_k |
| 0162040 | THANH LONG | no | 691 | (snapshot) | snapshot — CHƯA vào A_k/panel | YELLOW: cần mở rộng A_k |
| 0163030 | Xoài | yes | 489 | 10 | panel (A_k) | OK |
| 0163100 | Sầu riêng | yes | 489 | 10 | panel (A_k) | OK |
| 0500060 | GẠO | yes | 493 | 10 | panel (A_k) | OK |
| 0620000 | Cà phê | yes | 489 | 10 | panel (A_k) | OK |
| 0610000 | Chè | yes | 490 | 10 | panel (A_k) | OK |
| 0256040 | Parsley | no | 691 | (snapshot) | snapshot — CHƯA vào A_k/panel | YELLOW: cần mở rộng A_k |
| 0256080 | Basil | no | 691 | (snapshot) | snapshot — CHƯA vào A_k/panel | YELLOW: cần mở rộng A_k |

- **CỜ ĐỎ (ớt cay/thanh long rỗng MRL)? KHÔNG.** Ớt cay 0231020 = 489 chat×10 năm trong panel; thanh long 0162040 = **691 chất MRL trong snapshot** (chỉ chưa vào A_k/panel).
- **CỜ VÀNG (6 mã):** Đậu bắp, Vải+Nhãn, Chanh leo, THANH LONG, Parsley, Basil — có MRL trong snapshot nhưng A_k/panel chưa gồm các mã này → **bước thiết kế chỉ số phải MỞ RỘNG A_k** để thêm chúng (đặc biệt thanh long #2, đậu bắp, vải/nhãn, chanh leo, rau thơm).

## 4. FINAL lát VN
- **15 mã EU → 26 dòng** `status=final_vn` (có trích dẫn). 2 cờ giải; cà phê rang→processed; **không cờ đỏ** → **GỌI FINAL**.
- ⚠ Index sẽ rỗng MRL ở 6 sản phẩm VÀNG cho tới khi A_k/panel mở rộng — ghi `issues_log`. Residual ASEAN vẫn `parked_asean`.

## DỪNG
Lát VN FINAL (concordance). Chờ Claude xem MRL-coverage (đặc biệt cờ vàng 6 mã) trước khi sang thiết kế chỉ số. KHÔNG đụng 01_/05_; chỉ đọc 04_.