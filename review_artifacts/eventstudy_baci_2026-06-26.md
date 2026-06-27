# Event-study BACI (chế độ 2: cú siết MRL → thương mại) — 2026-06-26

> Ước lượng NHÂN QUẢ cú siết MRL EU → xuất khẩu VN (thí nghiệm tự nhiên). Treatment ngoại sinh = ω2016-filter. **Kết luận thẳng (theo yêu cầu): pre-trends KHÔNG phẳng + nhiều confounder lớn → thiết kế chế độ 2 CHƯA nhận diện được hiệu ứng nhân quả sạch.** Báo cáo trung thực, không che.

## Bước 1 — Panel BACI
- Đơn vị: VN xuất sản phẩm k → đích d → năm t. **7.488 dòng** = 12 sp (HS6, gom từ 23 HS6 lát VN) × 52 đích (EU27 + 25 RoW lớn) × 12 năm (2012–2023). Giữ zero (46%). **Khóa (k,d,t) duy nhất ✓.**
- *Lưu ý cấu trúc:* HS6 `081090` gộp 4 quả (vải/nhãn, chanh leo, thanh long, chôm chôm) → 1 sản phẩm thương mại; `070999` gộp đậu bắp+rau thơm. Trade ở HS6 KHÔNG tách được mịn hơn.
- Validation: tổng VN-xuất 17 sp = $6,4–11,3 tỷ/năm (khớp quy mô cà phê+gạo+trái cây).

## Bước 2 — Treatment (ω2016-membership, product-specific, loại omnibus 2016)
**4 cohort sạch** (chất binding ∈ ω2016 membership bị EU siết, Δg>0,5): **gạo 2018** (tricyclazole 1→0,01), **cam/cà phê/fruits081090 2021** (fipronil/chlorpyrifos). 8 sp never-treated (control). *Ớt/chè never-treated vì fipronil/chlorpyrifos KHÔNG đăng ký trên cây đó 2016 (phantom — đã lọc đúng).*

## Bước 3 — PPML tam-sai + event-study
### A. Tam-sai (PPML, FE prodk×year + dest×year + prodk×dest, cluster prodk)
`β(treated×EU×post) = +0,207 (SE 0,133, p=0,121) → exp(β)−1 = +23%` — **DƯƠNG, không ý nghĩa.** (Dấu NGƯỢC kỳ vọng "siết → giảm xuất".)
### B. Event-study (ref τ=−1)
| τ | coef | p | | τ | coef | p |
|---|---|---|---|---|---|---|
| ≤−4 | +0,19 | 0,35 | | 0 | −0,19 | 0,19 |
| −3 | **−0,19** | **0,056** | | +1 | +0,56 | 0,009 |
| −2 | +0,02 | 0,92 | | +2 | +0,98 | <0,001 |
| | | | | ≥+4 | +1,70 | <0,001 |
→ post DƯƠNG tăng dần (ngược kỳ vọng). **τ=−3 gần ý nghĩa (p=0,056) → pre-trend đáng ngờ.**

### Sun-Abraham vs TWFE (staggered)
- TWFE static ATT (unit=prodk×dest): **+0,015 (p=0,91) ≈ 0** — khác hẳn tam-sai +23% → **kết quả NHẠY đặc tả**.
- *Hạn chế kỹ thuật:* Sun–Abraham/Callaway–Sant'Anna PPML KHÔNG fit được (pyfixest fepois sập với FE thưa nhiều singleton). Nhưng vì **pre-trends fail là mối đe doạ nhận-dạng CỐT LÕI** (không phải chệch trọng số TWFE), hiệu chỉnh staggered không cứu được.

## Bước 4 — PRE-TRENDS (phép thử hiệu lực) — **KHÔNG ĐẠT, báo thẳng**
- Full sample: τ=−3 p=0,056 (gần ý nghĩa).
- **Cohort sạch nhất (gạo 2018, tiền-EVFTA): τ=−2 = +1,04 (p=0,003) → VI PHẠM song song RÕ.** Gạo→EU đã tăng MẠNH trước 2018. Rice DiD = +0,95 (p=0,004).
→ **Giả định song song KHÔNG thỏa** ngay cả ở cohort sạch nhất → hệ số post KHÔNG diễn giải nhân quả được.

## Bước 5 — Tái phân bổ RoW
`treated×post` (FE prodk×dest + year): **EU = −0,196 (p=0,008, −18%)**; RoW = −0,342 (p=0,187, −29%). → sản phẩm bị siết xuất KÉM hơn control ở CẢ EU lẫn RoW (EU đỡ hơn RoW) — KHÔNG phải dịch hướng EU→RoW; nhưng **control bị nhiễm** (xem dưới).

## Confounder (vì sao thất bại) — bằng chứng nguyên văn
```
EVFTA (EU–Vietnam FTA) hiệu lực 01/08/2020 → cắt thuế nông sản VN→EU, đúng lúc 3/4 cohort treated (2021).
   all17→EU 2020→2023 = +65% (vs RoW +59%) — EU vọt hậu-EVFTA.
Durian (NEVER-treated CONTROL) bùng nổ: 2018 $268M → 2023 $2.137M (8×) → CONTROL NHIỄM.
rice→EU bé tí ($10–77M; EU không phải thị trường gạo chính của VN) → thí nghiệm gạo yếu lực.
```
→ Hiệu ứng MRL (kỳ vọng âm, nhỏ) bị **EVFTA (dương, EU-riêng) + tăng trưởng thế tục + bùng nổ durian (control)** nhấn chìm.

## Bước 6 — Robustness
- Cửa sổ 2012–2023 + rice-only + dose-response: pyfixest fepois **sập (FE thưa)** ở các cấu hình này — ghi cờ hạn chế công cụ. Các model chạy được đều cho kết luận nhất quán: dương/nhiễu, pre-trend fail.

## VERDICT (thẳng)
1. **β tam-sai: +23% (p=0,12)** — dương, không ý nghĩa; dấu ngược kỳ vọng (confounded).
2. **Pre-trends KHÔNG phẳng** (gạo τ=−2 p=0,003) → **phép thử hiệu lực THẤT BẠI** → không kết luận nhân quả.
3. **Tái phân bổ:** không thấy dịch EU→RoW (cả hai âm so control nhiễm) — không kết luận dead-loss vs reallocation được.
4. **SA vs TWFE:** nhạy đặc tả (ATT +23% vs ~0) → bất ổn nhận dạng.
- **Nguyên nhân:** EVFTA 2020 + bùng nổ durian (control) + gạo→EU bé. Khớp định hướng cẩm nang (pre-trends fail, khung "tương quan có điều kiện" KHÔNG nhân quả).
- **Đề xuất (chờ Claude):** (a) kiểm soát EVFTA tariff-line tường minh; (b) loại sp bùng nổ (durian) khỏi control; (c) chuyển trọng tâm sang **chế độ 1** (biên mở rộng + RASFF count — đã có tín hiệu) thay vì ép chế độ 2 nhân quả.

## DỪNG
Chế độ 2 (event-study BACI) chạy xong — **pre-trends fail, không nhận diện nhân quả sạch** (báo thẳng). Chờ Claude đọc: hiệu lực (pre-trends), confounder EVFTA, hướng đi (chế độ 1). KHÔNG dựng chế độ 1/level ở task này.
