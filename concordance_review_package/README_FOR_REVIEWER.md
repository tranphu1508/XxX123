# 🔍 GÓI RÀ SOÁT CONCORDANCE EU→HS6 — cho người soi độc lập (Claude / GPT)

> **Mục đích:** Nhờ bạn (reviewer độc lập) rà lại bản đồ **EU Annex I product → HS6 (revision HS2012)** dùng cho nghiên cứu gravity về tác động MRL EU lên xuất khẩu nông sản ASEAN-5. Tìm MỌI sai sót còn lại trong ánh xạ.

## 1. Bối cảnh
- Bài: EU siết MRL thuốc BVTV → xuất khẩu nông sản ASEAN-5 (gravity PPML, treatment liên tục). Tạp chí mục tiêu ITJ (Q3).
- Concordance này quyết định **mỗi sản phẩm EU (có MRL) khớp mã thương mại HS6 nào** → sai concordance thì panel & hệ số lệch theo.
- File chính cần soi: `data/concordance_final_asean.csv` (cột `eu_code`, `eu_desc`, `annex1_legal_ref`, `hs6`, `note`, `phase2_status`, `resolve`, `hs6_lumped`).

## 2. PIPELINE đã dùng (3 nguồn — mời bạn kiểm chéo y hệt)
1. **Pháp lý EU (sản phẩm là gì + loài Latin):** `sources/annex1_species_to_code.csv` (parse từ Annex I Reg (EU) 2018/62, 1.305 dòng; khóa parent_code+sub_code).
2. **Nomenclature đích (mô tả chính thức HS2012):** `sources/product_codes_HS12_V202601.csv` (5.202 mã HS6 của BACI HS12 V202601 — chuẩn vàng).
3. **Literature + web chính thống** (bắc cầu loài→HS): Ferro (2015, Food Policy), Shingal (2024, Food Policy); WCO HS / EU CN / US HTS cho ca khó.

## 3. ĐÃ LÀM (tóm tắt — chi tiết ở `audit_evidence/` + `handoffs_this_work/`)
- Soi 100% cả **381 mã**. Đối chiếu mọi HS6 với universe HS2012 → **136/137 atomic hợp lệ** (giải cờ HS-revision).
- **Sửa ~26 lỗi ánh xạ** + **tái-neo ~26 mã ngoài-panel** về n.e.c. đúng nhóm. Danh sách: `audit_evidence/concordance_confirmed_errors_2026-06-29.csv`, và các note `HSFIX*/REANCHOR*` trong concordance.
- **Kiểm cuối: 0 lỗi map sản phẩm còn lại.** Còn 10 ca lumping gộp-cùng-họ HỢP LỆ (xem §5).
- **Đo tác động:** loại 24,8% số dòng dính lỗi+lumping → β S1 −1,47→−1,38, S2 ≈không đổi (`audit_evidence/concordance_distortion_betatest_2026-06-29.txt`). ⇒ sai sót còn lại (nếu có) gần như không đổi kết quả, nhưng vẫn cần đúng.

## 4. 🎯 ĐỀ NGHỊ BẠN KIỂM (việc cụ thể)
1. **Từng dòng `data/concordance_final_asean.csv`:** với mỗi eu_code, đối chiếu `eu_desc`+loài (nguồn 1) với mô tả HS2012 của `hs6` (nguồn 2). Báo mọi ca mã HS6 mô tả một SẢN PHẨM KHÁC với sản phẩm EU.
2. **Rà 26 mã đã sửa** (`concordance_confirmed_errors` + note HSFIX*): mã mới có đúng không?
3. **Rà 10 ca lumping** (§5): có chấp nhận được không, hay có mã riêng tốt hơn mình bỏ sót?
4. **Mã đa-mã & umbrella** (081090 trái cây n.e.c.; 121190 dược thảo; cà phê 0901xx; gạo 1006xx): tách/gộp hợp lý chưa?
5. **97 mã NO_HS6** (động vật/nec): loại đúng chưa, có cây nào bị loại nhầm?

## 5. HẠN CHẾ ĐÃ BIẾT — 10 ca lumping gộp-cùng-họ (đã chốt GIỮ)
purslane→aubergine(0709), parsnip→carrots(0706), loquat/medlar→pears(0808), red-mustard/land-cress/lamb's-lettuce→lettuce(0705), lentils→fresh-legumes(0708), dill→caraway-family(0909), PULSES→peas(0713). Lý do: sản phẩm KHÔNG có mã HS6 riêng → buộc gộp họ hàng gần (chuẩn Ferro/Shingal). Chi tiết + biện minh: `audit_evidence/concordance_LIMITATIONS_lumping_2026-06-29.md`.

## 6. CÂY THƯ MỤC GÓI
- `data/` — concordance final + backup trước sửa (so diff thấy đã đổi gì).
- `sources/` — Annex I species map + HS2012 universe (2 nguồn vàng).
- `audit_evidence/` — toàn bộ bảng phân loại/lỗi/chứng nhận/đo-méo.
- `scripts/` — script Python đã dùng (tái lập được).
- `decision_logs/` — issues_log, analytical_decisions, data_sources_provenance.
- `handoffs_this_work/` — nhật ký từng turn + PLAN.

**Lưu ý cho reviewer:** đừng tin tóm tắt — mở `data/concordance_final_asean.csv` và `sources/product_codes_HS12_V202601.csv`, đối chiếu trực tiếp. Báo bất kỳ ca nào nghi ngờ kèm eu_code + hs6 + lý do.
