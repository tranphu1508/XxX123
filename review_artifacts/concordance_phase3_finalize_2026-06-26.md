> Bản sao chỉ-đọc của 03_/concordance_phase3_finalize_2026-06-26.md, cập nhật 2026-06-26.

# Concordance Phase 3 FINALIZE — lát VN (VN-first, GIỮ ASEAN) — 2026-06-26

> **Cộng-thêm, KHÔNG phá ASEAN.** Lát VN hoàn thiện (verify từng dòng); residual ASEAN gắn `parked_asean` (không xóa/ép). **ĐÃ DỪNG** chờ Claude verify ~14 sản phẩm VN trước khi gọi 'final'.

## 1. Lỗi phổ quát đã sửa (lợi cả hai nhánh)
| eu_code | sản phẩm | Phase 2 (sai/niche) | Phase 3 (sửa) | cơ sở |
|---|---|---|---|---|
| 0233010 | Melons (Cucumis melo) | 080711 (dưa hấu) | **080719** (dưa khác) | heading 0807 đúng, lỗi chọn con; 080719='melons other than watermelons' |
| 0233030 | Watermelons (Citrullus) | — | **080711** (xác nhận) | dưa hấu |
| 0500090 | Wheat (Triticum) | 100111 (durum *giống*) | **1001.xx toàn bộ** (100111/119/191/199) | one-to-many; MRL áp hạt thương phẩm, không pin nhánh giống |
| 0500010 | Barley (Hordeum) | 100310 (*giống*) | **100310+100390** | giữ nhánh non-seed |
- **Spot-check heading nhiều-con** (0807 cucurbit, 1001/1003/1005/1006 ngũ cốc, 0810 quả khác, 0709 ớt/đậu bắp): xác nhận con HS6 khớp commodity (gạo→1006 đủ 4 con; ngô→1005; durian→081060; ớt→070960). Referential **0 lỗi**.

## 2. Bảng LÁT VN (finalized_vn — verify từng dòng, có trích dẫn)
| sản phẩm VN | EU code | HS6 con | form | so kỳ vọng |
|---|---|---|---|---|
| Grapefruits | 0110010 | 080540 | fresh | 080540 ✓ (pomelo) |
| Oranges | 0110020 | 080510 | fresh | 080510 ✓ |
| Lemons | 0110030 | 080550 | fresh | 080550 ✓ |
| Mandarins | 0110050 | 080520 | fresh | 080520 ✓ |
| Sweet peppersbell peppers | 0231020 | 070960+090421+090422 | fresh+RAC_dried | 070960 ✓ + 0904 (ớt khô RAC) |
| Okralady's fingers | 0231040 | 070999 | fresh | 070999 ✓ — **LỆCH: kỳ vọng EU 0239, thực tế 0231040** |
| Litchislychees | 0162020 | 081090 | fresh | 081090 ✓ |
| Passionfruitsmaracujas | 0162030 | 081090 | fresh | 081090 ✓ |
| Mangoes | 0163030 | 080450 | fresh | 080450 ✓ |
| Durians | 0163100 | 081060 | fresh | 081060 ✓ |
| Rice | 0500060 | 100610+100620+100630+100640 | RAC | 1006 đủ 4 con ✓ |
| Coffee beans | 0620000 | 090111+090112+090121+090122 | RAC_bean | 090111(+con) ✓ |
| Teas | 0610000 | 090210+090220+090230+090240 | RAC_dried | 0902 con ✓ |
| (f) herbs and edible flowe | 0256000 | 070999 | fresh | 070999 ✓ (herbs) |

**⚠ 2 sản phẩm VN KHÔNG có mã EU riêng** (rơi vào 'Others' → 081090, CẦN người dùng xác nhận mã dùng):
- **Thanh long/dragon fruit (pitahaya)** — catalogue EU không có code riêng (gần nhất 0162040 cactus/Opuntia); → 0162990 'Others' → **081090**.
- **Nhãn/chôm chôm (longan/rambutan)** — không có code riêng → 0162990 'Others' → **081090**. (Vải/litchi CÓ: 0162020.)

## 3. Số dòng
- **finalized_vn: 14 mã EU** (25 dòng eu×hs6 con). **universal_fix: 4**. **parked_asean: 363** (residual ASEAN giữ nguyên, hoàn thiện nếu nối lại ASEAN). Tổng 381.
- Referential: mọi HS6 ∈ BACI HS12 (0 lỗi). Cờ HS-revision **ĐÓNG cho lát VN**.

## 4. Quyết định phạm vi RAC (tươi/thô = dạng MRL áp)
- **GIỮ mẫu chính (RAC, KHÔNG gắn processed):** ớt KHÔ/paprika (0904 — RAC của Capsicum là khô), cà phê NHÂN (0901), chè khô (0902), gia vị. Vì MRL EU áp trên dạng RAC này.
- **Gắn `processed` (ngoài mẫu chính):** đông/đóng hộp/chế biến sâu — 0710 (đông), 0711/0712 (bảo quản/khô-rau), 0811/0812/0813 (đông/khô-quả).
- One-to-many: nhóm/heading nhiều con thương phẩm → GIỮ TẤT CẢ con (gạo 4, wheat 4, citrus theo loài).

## DỪNG
Lát VN hoàn thiện (chờ Claude verify 14 sản phẩm + 2 cờ thanh long/longan). Residual parked_asean. Sau khi Claude OK → gọi 'final' + (đã ghi) analytical_decisions_log. **Chưa đụng 01_/04_/05_.**