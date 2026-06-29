# Round 006 — Cowork literature synthesis (đọc sâu + search bổ sung)

## Phương pháp
Đọc methodology fulltext **9 bài** MRL/standards-gravity trong `Reading/` (quote/nguồn ở `literature_policy_matrix.csv`; danh mục đầy đủ ở `literature_inventory.csv`) + tra cứu **văn bản pháp lý EU + tài liệu hướng dẫn** (Reg 396/2005, SANTE/10704/2021).

## BA tuyến bằng chứng HỘI TỤ → TRADE_COVERAGE_PRIMARY + RAC làm sàn

### Tuyến 1 — PHÁP LÝ (mạnh nhất, từ chính Reg 396/2005)
- MRL được **đặt trên sản phẩm CHƯA chế biến (RAC)** ở Annex II/III (apples, tomatoes, wheat grain).
- Nhưng quy định **áp lên CẢ processed** qua **"processing factor"** (Art 20): *"MRLs applicable shall be those...for the relevant product covered by Annex I, taking into account changes...caused by processing."*
- Phạm vi: *"products...used as **fresh, processed and/or composite** food"* — **315 sản phẩm fresh + processed**.
- → MRL **lấy RAC làm gốc nhưng pháp lý mở sang dạng chế biến** = đúng mô hình **TRADE_COVERAGE_PRIMARY (gồm processed-primary) + CORE_RAC_ONLY (robustness)**.
- Default 0,01 (Art 18) — **trùng** cách dự án xử missing MRL.
- *Nguồn:* EUR-Lex Reg (EC) 396/2005 Art 18/20; EC guidance SANTE/10704/2021 (processing factors); EU database on processing factors (BfR).

### Tuyến 2 — LITERATURE precedent (gồm processed)
- **Drogue & DeMaria (2012, Food Policy):** MRL apples/pears, **fresh + related processed products**, HS6 (fresh apples 080810), default 0,01. ← precedent sát nhất.
- **Otsuki et al. (2001, Food Policy):** aflatoxin, chuẩn áp **processed + unprocessed**.
- **Xiong & Beghin (2014):** map 109 plant products → HS4/HS6, Codex baseline.
- **Ferro (2015), Shingal (2024), Fiankor (2021/2025), Curzi (2020):** đều **HS6-level**; không bài nào RAC-only-hy-sinh-trade.

### Tuyến 3 — chuẩn nghề
- HS6 + PPML là chuẩn phổ quát; MRL data map HS6 (164 nước × 225 product groups; Shingal/Ehrich web).

## KẾT LUẬN (có cơ sở pháp lý + học thuật)
**Chốt TRADE_COVERAGE_PRIMARY (main) + CORE_RAC_ONLY (robustness)** — không còn là suy luận mà **được Reg 396/2005 (Art 20 processing factor) + Drogue/Otsuki ủng hộ trực tiếp**. Cụ thể: gồm HS6 mà luồng XK ASEAN đi qua (cashew bóc vỏ 080132, tiêu xay, gạo xát), RAC làm sàn, **chỉ loại dạng đổi-cơ-sở-MRL** (dầu ép, chiết xuất — vốn có MRL riêng hoặc rơi ngoài Annex). Default 0,01 cho missing.

## ĐỀ XUẤT BỔ SUNG FULLTEXT (nhờ user tải về)
1. **Nguyen (2026, Agribusiness) — "Pesticide MRLs as Trade Barriers: Vietnam's Coffee and Rice Exporters"** — ĐỐI THỦ trực tiếp; cho thấy chính xác cách một bài VN-MRL chọn HS6 + dạng sản phẩm (coffee green? rice milled?). **Ưu tiên cao nhất.**
2. **"Trade impact of MRL in fresh fruits and vegetables" (Food Policy 2021, ScienceDirect S0306919221001822)** — methodology fresh-FFV MRL HS6.
3. (tùy) Shingal & Ehrich (2024) bản web fulltext nếu khác bản có sẵn.

## Hạn chế
- 9 bài đọc methodology (có quote); 4 bài inventory còn lại (Li/Santeramo/Disdier/Crivelli) ảnh hưởng thấp tới câu hỏi product-form. Bằng chứng pháp lý Art 20 đã đủ để chốt.

---

## BỔ SUNG (đọc thêm Nguyen 2026 + Hejazi 2022) — bằng chứng QUYẾT ĐỊNH

### Nguyen (2026, Agribusiness) — ĐỐI THỦ TRỰC TIẾP (VN coffee + rice)
Bài này đo đúng 2 sản phẩm chủ lực VN, nên là precedent sát nhất:
- *"Green Coffee Beans (HS 0901.11) account for **97.6%** of total coffee volume, while Milled and Broken Rice (HS 1006.30/40) collectively comprise **97.9%** of the rice category."*
- *"applying the Raw Agricultural Commodity (RAC) standard to the HS4 aggregate correctly identifies the binding regulatory [constraint]"* (vì MRL đồng nhất across sub-headings).
- **Hệ quả cho ta:** (1) cà phê → **green 090111** đúng (97,6%); (2) gạo → **milled/broken 100630;100640** là dạng buôn chính (97,9%) — **RAC-only paddy (100610) bỏ sót ~98% trade gạo VN**. Ta đã map gạo gồm cả 100630/640 → ĐÚNG. → **Nguyen xác nhận chính xác cả 2 lựa chọn của ta.**

### Hejazi, Grant & Peterson (2022, Food Policy 106:102203) — fresh-FFV
- Phạm vi **fresh fruits & vegetables**; cho FFV tươi thì **fresh = RAC = dạng buôn** → fresh-only là chuẩn, không mâu thuẫn coverage.

### Nguyên tắc policy TINH CHỈNH (có precedent cho từng nhánh)
| Loại sản phẩm | Dạng lấy | Precedent |
|---|---|---|
| **Rau/quả tươi** (durian, thanh long, xoài... — phần lớn panel) | fresh/RAC (= dạng buôn) | Hejazi 2022 (fresh-FFV) |
| **Commodity processed-dominant** (cà phê→xanh, **gạo→xát**, điều→bóc vỏ, gia vị→xay) | dạng-buôn-chính (coverage) + RAC sàn | Nguyen 2026, Drogue 2012, Reg 396/2005 Art 20 |
| Dạng đổi-cơ-sở-MRL (dầu ép, chiết xuất, rang) | LOẠI | (có MRL riêng/ngoài Annex) |

**Chốt:** policy hiện tại của concordance (cà phê green-only, gạo gồm milled, điều shelled, spices whole+ground) **khớp 100% với đối thủ Nguyen + luật EU + Drogue/Hejazi**. Không cần đổi mapping; chỉ ghi rõ cơ sở vào Methods/Limitations.

## NGUỒN (web + legal)
- EUR-Lex Reg (EC) 396/2005 (Art 18/20); EC SANTE/10704/2021 (processing factors).
- Nguyen 2026, Agribusiness, doi:10.1002/agr.70107 (fulltext trong Reading/).
- Hejazi, Grant & Peterson 2022, Food Policy 106:102203, doi:10.1016/j.foodpol.2021.102203 (fulltext: Reading/Round2_220526/hejazi2022.pdf).
