> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/03_concordance_product_code_to_harmonized_system_six_digit/concordance_rebuild_phase1_report_2026-06-26.md, cập nhật 2026-06-26.

# Báo cáo Phase 1 — Rebuild concordance EU product_code → HS6 (HS2012) — 2026-06-26

> **PHASE 1 = sinh ứng viên tự động + bảng quyết định. ĐÃ DỪNG chờ duyệt.** Chưa chốt concordance cuối.

## 1. Hai tập tham chiếu + provenance
- **Vế nguồn (EU):** `Pesticide-residues-products-All.csv` — **381 sản phẩm EU** (product_code 7 ký tự + product_name + `product_scientific_names` Latin + synonyms + phân cấp). Nguồn: EU Pesticides Database, endpoint products (API v3.0), **snapshot 2026-05-27**. 228/381 có tên khoa học.
- **Vế đích (HS2012):** metadata BACI HS12 đóng băng `01_/trade_data_baci/.../product_codes_HS12_V202601.csv` — 5202 HS6, **198 thuộc chương 07–10**. HS neo HS2012 → **referential = 0 lỗi** (mọi ứng viên ∈ BACI).
- Bản cũ `concordance_EU_HS6_v3.csv`: chỉ tham chiếu (gợi ý + đối chiếu), KHÔNG nguồn chân lý.

## 2. Match ứng viên (tự động, tái lập: `scripts/build_concordance_candidates.py` — rapidfuzz: tên khoa học + fuzzy mô tả + gợi ý bản cũ)
Trên 381 mã EU: **auto_accept 59**, needs_review 96, needs_review_group (một-nhiều) 62, excluded n.e.c. 47, ngoài-07-10 88, excluded không-khớp 29.
- **184 mã lá in-scope (chương 01/02/03/05/06/08, type=4):** auto_accept 59, needs_review 96, excluded không-khớp 29. Có ứng viên ≥medium(72) = 114 (62%).
- Auto-accept SIẾT: chỉ khi score ≥90 VÀ (bản cũ đồng thuận HOẶC khớp tên khoa học); mọi ca **bản cũ bất đồng → hạ về needs_review (cờ OLD_DISAGREE)** vì auto-match dễ sai dạng (tươi/khô/đông).

## 3. Ca khó (cần người quyết)
- **Một-nhiều (nhóm EU type 1/2/3): 62 mã** (vd 'PULSES' 0300000, 'Leaf vegetables' 0250000) → giữ tất cả HS6 con (MRL áp mọi con) hay map cấp lá?
- **Nhiều-một (>1 mã EU → 1 HS6): 32 HS6.** Ví dụ: 090300(Mate)×7, 090962(Spices: seeds of)×5, 071490(Vegetable roots )×5, 070519(Vegetables: lett)×4, 070690(Vegetables, root)×4.
- **n.e.c. ('Others', type=5): 47 mã** → đề xuất LOẠI (không có HS6 sạch).
- **Ngoài chương 07–10 (chế biến/dầu/đường/động vật): 88 mã** (EU 04 dầu→HS12, 09 đường→HS17, 10 động vật) → EXCLUDE hay map HS12/17?
- **Lá in-scope không khớp HS6 sạch: 29 mã** → soi tay (vd Purslanes 0252020, Loquats 0130050, Celeriacs 0213030).

## 4. Đối chiếu bản cũ (tham chiếu nhẹ — KHÔNG theo)
- Đồng thuận (suggested ∈ bản cũ) ≈ **76%**. **21 ca bản-cũ-bất-đồng** (cờ OLD_DISAGREE, ưu tiên soi). Một số lộ **lỗi auto-match** (token khớp nhưng sai dạng) — đúng vùng người duyệt quyết:

| eu_code | eu_desc | suggested(mới) | hs6_desc | score | old_hs6 |
|---|---|---|---|---|---|
| 0280020 | Wild fungi | 071233 | Vegetables: jelly fungi (Tremell | 70.0 | 070959 |
| 0260010 | Beans (with pods) | 071333 | Vegetables, leguminous: kidney b | 100.0 | 070820;071022 |
| 0233010 | Melons | 081400 | Peel: of citrus fruit or melons  | 100.0 | 080719 |
| 0212010 | Cassava roots/manioc | 090300 | Mate | 66.7 | 071410;071440;071450 |
| 0500090 | Wheat | 100810 | Cereals: buckwheat | 100.0 | 100111;100119;100191;100199 |
| 0153030 | Raspberries (red and yellow) | 081040 | Fruit, edible: cranberries, bilb | 65.4 | 081020;081120 |
| 0260030 | Peas (with pods) | 071310 | Vegetables, leguminous: peas (pi | 100.0 | 070810;071021 |
| 0140010 | Apricots | 081310 | Fruit, edible: apricots, dried | 100.0 | 080910 |
| 0212020 | Sweet potatoes | 071490 | Vegetable roots and tubers: arro | 100.0 | 071420 |
| 0154030 | Currants (black, red and white) | 081120 | Fruit, edible: raspberries, blac | 100.0 | 081030 |
| 0252010 | Spinaches | 091099 | Spices: n.e.c. in heading no. 09 | 80.0 | 070970;071030 |
| 0212030 | Yams | 071490 | Vegetable roots and tubers: arro | 100.0 | 071430 |

## 5. Độ phủ HS 07–10
- 198 HS6 (07–10): **96 có ≥1 mã EU đề xuất**; **102 CHƯA có mã EU nào** (vùng 'không có sản phẩm MRL' / HS chế biến-gộp). Ví dụ chưa map: 070110(Vegetables: seed), 070190(Vegetables: pota), 070490(Vegetables, bras), 070511(Vegetables: cabb), 070529(Vegetables: chic), 070700(Vegetables: cucu).

## 6. Mẫu bảng quyết định (đầy đủ ở `outputs/concordance_decision_table_2026-06-26.csv` — người duyệt điền hs6_final/decision/reason/reviewer)
| eu_code | eu_desc | suggested_hs6 | score | status | old_hs6 |
|---|---|---|---|---|---|
| 0163100 | Durians | 081060 | 100.0 | auto_accept | 081060 |
| 0110030 | Lemons | 080550 | 100.0 | auto_accept | 080550 |
| 0300010 | Beans | 071350 | 100.0 | auto_accept | 071331;071332;071333;071334;071335;071350 |
| 0242010 | Brussels sprouts | 070420 | 93.8 | auto_accept | 070420 |
| 0161010 | Dates | 080410 | 100.0 | auto_accept | 080410 |
| 0280020 | Wild fungi | 071233 | 70.0 | needs_review | 070959 |
| 0260010 | Beans (with pods) | 071333 | 100.0 | needs_review | 070820;071022 |
| 0233010 | Melons | 081400 | 100.0 | needs_review | 080719 |
| 0252020 | Purslanes | 090922 | 55.6 | excluded_proposed_nomatch |  |
| 0213030 | Celeriacs/turnip rooted cele | 070940 | 59.4 | excluded_proposed_nomatch |  |
| 0130050 | Loquats/Japanese medlars | 100410 | 52.4 | excluded_proposed_nomatch |  |

## DỪNG
Đã DỪNG — chưa chốt concordance. Chờ duyệt: 96 needs_review (ưu tiên 21 cờ OLD_DISAGREE) + 62 nhóm một-nhiều + 47 n.e.c. + 88 ngoài-scope + 29 không-khớp. Quyết định ghi `concordance_decision_table`; Phase 2 suy ra concordance cuối + ghi `analytical_decisions_log` + sổ điền tay (phần gán tay).