# Thiết kế bộ máy chỉ số stringency (level/change kép) + VALIDATE RASFF — 2026-06-26

> Xây bộ máy chỉ số + cấu trúc nhận diện KÉP cho lát VN từ panel, chọn biến thể bằng RASFF (độc lập outcome thương mại). Hai khe ngoài → THAM SỐ HÓA, không chờ: ω (rổ đăng ký MARD — PENDING), Codex baseline (PENDING). Rổ tạm = RASFF-18 + trọng số đều. **DỪNG trước hồi quy BACI.** Quy tắc bằng chứng nguyên văn áp dụng.

## PHẦN 1 — Stringency mỗi ô s_akt (chất×sản phẩm×năm)
- Nguồn: panel binding 17 mã VN × 2009–2024 (builder kiểm chứng 0 sai). `not_yet_set→0,01` (mặc định pháp lý Art 18(1)(b)); loại `pending_celex` (null).
- **g-level (XÂY ĐƯỢC NGAY):** `g = −ln(MRL_EU)` (MRL ngặt hơn → g cao hơn). Baseline VN hấp thụ qua FE (VN xuất duy nhất, kiểu Nguyen).
- **g-gap-vs-Codex (PENDING):** `g = ln(Codex_ak / MRL_EU)` cắt ≥0 — cờ `PENDING_codex` trong CSV; cần thu giá trị Codex MRL, KHÔNG chặn phần còn lại.
- Hai rổ chất: **(a) RASFF-18** (proxy "VN có dùng"; 17 chất có mặt trong A_k/panel — acetamiprid loại vì def (R) 2025+ không có MRL in-window); **(b) A_k 515** (rộng, robustness).

## PHẦN 2 — Gộp chất → chỉ số product×year (hai toán tử)
- **MEAN:** trung bình g trên rổ (exposure trung bình).
- **Weakest-link (MAX g = MIN MRL):** chất NGẶT NHẤT quyết định ("một chất vượt là cả lô bị chặn" — đáp Nguyen). *Lưu ý đặt tên:* "min MRL" = "max g" = weakest-link.
- **Khe trọng số ω_ia (PENDING):** cột `omega` tham số, mặc định **=1 đều**. ω THẬT = rổ đăng ký quốc gia VN kỳ-gốc/trễ (thông tư MARD) — ngoại sinh với MRL & kiểm tra. **KHÔNG dùng RASFF làm trọng số** (sẽ thành vòng nội sinh).

## PHẦN 3 — CẤU TRÚC KÉP (level vs change — KHÔNG trộn)
- **Chỉ số MỨC `S_lvl[k,t]`:** gộp trên MỌI chất ràng buộc (gồm chất tĩnh carbendazim) → chế độ 1 (cắt-ngang) + outcome RASFF. Cột: `S_lvl_{mean,max}_{rasff,ak}`.
- **Chỉ số THAY ĐỔI `dS[k,t]`:** CHỈ từ cặp `step_in_window` (lấy từ diagnostic), tách riêng **tightening** (Δg>0 = MRL giảm). Cột: `dS_tighten_{max,sum}_{rasff,ak}`, `n_tighten_*`. → chế độ 2 (event-study/DiD).
- **Danh mục "thí nghiệm tự nhiên" sạch** (`vn_change_natural_experiments.csv`, 62 cú Δg>0,5):
```
propiconazole × citrus  2022: 9.0/5.0 → 0.01  (Δg≈+6.2..6.8)
chlorpyrifos  × chè     2021: 2.0 → 0.01      (Δg=+5.30)  [Green Deal]
chlorpyrifos  × gạo     2021: 0.5 → 0.01      (Δg=+3.91)  [Green Deal]
tricyclazole  × gạo     2018: 1.0 → 0.01      (Δg=+4.61)  [vụ kinh điển rice]
fipronil      × ớt      2021: 0.01 → 0.005    [post-fipronil scandal]
```
- ⚠ Hai biến XUẤT RIÊNG BIỆT, nhãn rõ; **KHÔNG bao giờ trộn** level với change.

## PHẦN 4 — VALIDATE bằng RASFF (chọn chỉ số, độc lập thương mại)
Panel: **80 obs** (8 nhóm RASFF map sang eu_code × 2015–2024), tổng 200 rejection. Poisson `count ~ S_lvl + nhóm FE + năm FE`. Map: ot_tieu→0231020, thanh_long→0162040, gao→0500060, dau_bap→0231040, sau_rieng→0163100, caphe_che→{0620000,0610000}, rau_thom→{0256040,0256080}, trai_cay_khac→{vải,chôm chôm,chanh leo,xoài,citrus}. ('other' loại — chưa map.)

| biến thể (level) | coef | p | AIC | pseudo-R² | ΔLL vs FE-only |
|---|---|---|---|---|---|
| **S_lvl_max_rasff (weakest-link, RASFF-18)** | **+0,904** | **0,004** | **386,1** | **0,364** | **+4,57** |
| S_lvl_max_ak (weakest-link, A_k) | +0,469 | 0,037 | 391,0 | 0,355 | +2,13 |
| S_lvl_mean_rasff (mean, RASFF-18) | +0,093 | 0,890 | 395,3 | 0,347 | +0,01 |
| S_lvl_mean_ak (mean, A_k) | −0,094 | 0,901 | 395,3 | 0,347 | +0,01 |
*(FE-only baseline: AIC 393,29. Robustness product-FE-only: thứ hạng giữ nguyên — weakest-link signif, mean_ak sai dấu.)*

### BIẾN THỂ THẮNG: **S_lvl_max_rasff** (weakest-link × rổ RASFF-18 × level)
- Hai phát hiện chọn-chỉ-số: **(1) Weakest-link >> MEAN** — chất ngặt nhất dự báo rejection (hệ số +0,90, p=0,004), trung bình KHÔNG (p≈0,9). Xác nhận logic "một chất vượt là chặn lô" (Nguyen). **(2) Rổ RASFF-18 > A_k** — neo theo chất VN thực dùng sắc hơn rổ 515 (A_k-mean còn sai dấu).
- **Caveat nội sinh (de facto, KHÔNG nhân quả):** chất "nóng" bị liệt enhanced-control (Reg 2019/1793) → kiểm dày hơn → rejection nhiều, đồng biến stringency. Đây là **validate đo lường** (chỉ số bắt đúng ràng buộc), KHÔNG phải hiệu ứng thương mại. Chưa có offset enhanced-control (PENDING dữ liệu Reg 2019/1793 product-year).

## PHẦN 5 — BẢN ĐỒ "đã xây vs chờ"
| | Trạng thái |
|---|---|
| s_akt = g-level (−ln MRL), 2 rổ | ✅ ĐÃ XÂY |
| MEAN + weakest-link(max) | ✅ ĐÃ XÂY |
| LEVEL `S_lvl` vs CHANGE `dS` (tách) | ✅ ĐÃ XÂY |
| Chỉ số trọng số ĐỀU (ω=1) | ✅ ĐÃ XÂY |
| Validate RASFF → biến thể thắng | ✅ ĐÃ XÂY (S_lvl_max_rasff) |
| **ω = rổ đăng ký MARD** | ⏳ **PENDING (CRITICAL)** — cột `omega` chờ cắm; critical-path song song |
| **g-gap-vs-Codex** | ⏳ PENDING (tùy chọn) — cần giá trị Codex MRL |
| offset enhanced-control (Reg 2019/1793) | ⏳ PENDING (cho validate/estimation) |
| **Hồi quy thương mại BACI** | ⛔ **CHƯA CHẠY** (DỪNG đúng phạm vi) |

## DỪNG
Bộ máy chỉ số + cấu trúc kép đã xây, biến thể thắng RASFF = **S_lvl_max_rasff** (weakest-link, RASFF-18). **CHƯA chạy hồi quy thương mại BACI.** Chờ Claude/người dùng: (a) xác nhận biến thể thắng, (b) chốt trước khi cắm ω (MARD) + chạy thương mại.
