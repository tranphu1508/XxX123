> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/03_concordance_product_code_to_harmonized_system_six_digit/concordance_rebuild_phase2_report_2026-06-26.md, cập nhật 2026-06-26.

# Báo cáo Phase 2 — Concordance EU→HS6 (HS2012) neo Codex + tên khoa học — 2026-06-26

> **PHASE 2 = neo có thẩm quyền + đa-phiếu hội tụ + trọng tài có trích dẫn. ĐÃ DỪNG chờ duyệt residual.** Mỗi dòng có cơ sở kiểm chứng, không phải niềm tin.

## Nguồn neo + provenance
- **Tên khoa học (Latin):** từ EU product catalogue (`Pesticide-residues-products-All.csv`, snapshot 2026-05-27) — ground-truth độc lập với AI.
- **Phân loại nhóm = Codex CCPR:** phân cấp EU Annex I (0110 Citrus, 0130 Pome, 0500 Cereals…) chính là phân loại commodity Codex (cùng gốc CCPR).
- **HS đích = HS2012:** text heading HS từ metadata BACI HS12 đóng băng (01_) — dùng làm văn bản tham chiếu cho heading + verify.
- *Nguồn ngoài (Codex CXA-4 PDF, HS-EN, Fiankor A1): KHÔNG kéo được trong môi trường này (FAO web_fetch timeout 180s; HS-EN/Fiankor paywall/JS). Neo thay bằng tên khoa học + text heading HS2012 local + cấu trúc Codex/EU — đều kiểm chứng được.*

## Bước 1 — Mỏ neo lõi: nhóm Codex/EU → heading HS2012
`codex_group_to_hs_heading_2026-06-26.csv`: **60 dòng (nhóm EU → heading)**, **verify 60/60** (heading tồn tại trong BACI HS12, có HS6, text khớp). Ví dụ:

| EU subgroup | nhóm | heading HS | text heading (HS2012, BACI) |
|---|---|---|---|
| 0110 | Citrus fruits | 0805 | Fruit, edible: oranges, fresh or dried |
| 0120 | Tree nuts | 0801 | Nuts, edible: coconuts, desiccated |
| 0120 | Tree nuts | 0802 | Nuts, edible: almonds, fresh or dried, i |
| 0130 | Pome fruits | 0808 | Fruit, edible: apples, fresh |
| 0140 | Stone fruits | 0809 | Fruit, edible: apricots, fresh |
| 0151 | (a) grapes | 0806 | Fruit, edible: grapes, fresh |
| 0152 | (b) strawberries | 0810 | Fruit, edible: strawberries, fresh |
| 0153 | (c) cane fruits | 0810 | Fruit, edible: strawberries, fresh |

## Bước 2-3 — Hội tụ đa-phiếu (A loài+heading / B fuzzy / C bản cũ / D auto)
Trên 381 mã EU: **verified_high 84** (A trong heading + (≥1 phiếu trùng HOẶC heading duy-nhất-HS6)), needs_confirm 30, needs_arbitration 60, needs_review_group (một-nhiều) 85, needs_review_noanchor (ngoài-neo/chế biến/động vật) 75, excluded n.e.c. 47.
- **verified_high auto-accept = 84 dòng, KHÔNG cần duyệt từng cái** (có trích dẫn loài+heading). Trong đó form: {'fresh_raw': 84}.
- Residual chờ duyệt: needs_confirm 30 + needs_arbitration 60 + nhóm 85 + ngoài-neo 75 + n.e.c. 47.

## Bước 4 — Trọng tài có TRÍCH DẪN — Phase 2 SỬA lỗi fuzzy của Phase 1
Neo loài→heading sửa đúng các ca Phase 1 sai (token khớp nhầm):

| eu_code | sản phẩm | Phase 1 (fuzzy, SAI) | Phase 2 vote_A (neo, có trích dẫn) |
|---|---|---|---|
| 0500090 | Wheat | 100810 Cereals: buckwheat | **100111** Cereals: wheat and meslin, |
| 0233010 | Melons | 081400 Peel: of citrus frui | **080711** Fruit, edible: watermelons |
| 0212010 | Cassava roots/manioc | 090300 Mate | **071410** Vegetable roots and tubers |
| 0252010 | Spinaches | 091099 Spices: n.e.c. in he | **070970** Vegetables: spinach, New Z |
| 0500010 | Barley | 100390 Cereals: barley, oth | **100310** Cereals: barley, seed |

Ví dụ trích dẫn (cột authoritative_citation): EU group 0233 ((c) cucurbits with inedible peel) → heading 0807 'Fruit, edible: watermelons, fresh' (HS2012); loài/mô tả → 080711 'Fruit, edible: wate…

## Bước 5 — Quyết định phạm vi (đề xuất, ghi analytical_decisions_log khi finalize — KHÔNG gọi 'verified')
- **Tươi/thô vs chế biến:** mặc định map EU product → HS6 dạng **tươi/thô** (MRL áp trực tiếp sản phẩm thô). HS6 chế biến (0710 đông, 0711/0712 bảo quản/khô, 0811/0812/0813 đông/khô quả) gắn cờ `form=processed` cho robustness/extension, KHÔNG vào mẫu chính.
- **Một-nhiều (nhóm EU → nhiều HS6 con):** giữ TẤT CẢ con (MRL áp mọi con). 85 nhóm.
- **n.e.c./'Others':** loại + lý do. 47 mã.

## Bước 6 — Cross-check / coverage / referential
- **Referential:** mọi HS6 đề xuất ∈ BACI HS12 — **0 lỗi** (kỳ vọng 0).
- **Coverage in-scope (184 lá chương 01/02/03/05/06/08):** có vote_A = 174 (95%).
- **Độ phủ HS07–10:** 198 HS6; có ≥1 EU vote_A = 104; chưa có = 94 (HS chế biến-gộp / no MRL product).
- **Fiankor 2021 Bảng A1:** KHÔNG truy cập được (paywall/không fetch được) → bỏ qua, ghi chú; có thể đối chiếu thủ công sau.

## DỪNG
Đã DỪNG. **84 verified_high auto-accept** (có trích dẫn, không cần duyệt từng cái). Chờ duyệt residual: needs_confirm 30 (xác nhận nhanh) + needs_arbitration 60 + nhóm 85 + ngoài-neo 75 + n.e.c. 47; + quyết định phạm vi tươi/chế biến. Sau khi chốt → finalize concordance + ghi `analytical_decisions_log` + đóng cờ HS revision.