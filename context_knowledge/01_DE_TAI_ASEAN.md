# 01 — ĐỀ TÀI ASEAN (gravity biến-liên-tục)

> Bài đang HOẠT ĐỘNG. Thiết kế = gravity cấu trúc biến-liên-tục (Pha A, Đợt 1-3 đã chạy). Tạp chí: **The International Trade Journal (Q3)**. Framing: **tương quan có điều kiện, KHÔNG nhân quả**.

---

## 1. DANH TÍNH BÀI
- **Chủ đề:** EU thắt chặt MRL thuốc BVTV → xuất khẩu nông sản ASEAN-5 sang EU, giai đoạn ~2015–2024.
- **ASEAN-5:** Việt Nam, Indonesia, Thái Lan, Malaysia, Philippines.
- **Tạp chí:** The International Trade Journal (Q3). *(Mục tiêu CŨ "The World Economy" đã bỏ — nó gắn với tham vọng nhân quả không đạt.)*
- **Ba giả thuyết:**
  - **H1 (market access):** MRL siết → giảm xuất sang EU. → ✅ ủng hộ mạnh.
  - **H2 (upgrading / unit value):** MRL siết → giá đơn vị tăng (nâng cấp chất lượng). → ⚠️ yếu, không robust.
  - **H3 (reallocation):** MRL siết → xuất dịch sang thị trường khác. → ✅ có chọn lọc.

---

## 2. THIẾT KẾ NHẬN DIỆN — điểm CỐT LÕI phải hiểu đúng

**Mô hình chính = gravity cấu trúc PPML với treatment LIÊN TỤC** (chỉ số stringency MRL EU, không nhị phân hóa). KHÔNG phải event-study.

**Vì sao KHÔNG event-study (và vì sao pre-trends fail KHÔNG giết bài):**
- Đợt 2, Quyết định 40 + Bài học #1: MRL siết là **quá trình liên tục/dần dần**. Ép thành "năm sự kiện T_k" nhị phân → ở các năm τ<0 treatment *đã đang chạy* → sinh **pre-trends giả** (artifact của mis-specification, KHÔNG phải bằng chứng MRL vô hại).
- Mô hình biến-liên-tục (A1) đo đúng treatment liên tục → **không phụ thuộc giả định parallel-trends nhị phân**.
- Event-study chạy như **kiểm tra transparency → để PHỤ LỤC**, kèm thảo luận. (Pha B tái xác nhận pre-trends fail ở mọi khung nhị phân → củng cố phụ lục, KHÔNG đổi kết luận.)
- **Caveat trung thực bắt buộc (NhatKy_P34):** gravity-liên-tục vẫn KHÔNG nhân quả sạch (stringency có thể tương quan xu hướng nền). Framing = "tương quan có điều kiện, vững qua nhiều đặc tả". Đây ĐÚNG chuẩn văn liệu NTM-gravity (Fiankor, Santeramo dùng chỉ số liên tục, không event-study).

---

## 3. DỮ LIỆU & ĐẶC TẢ (Pha A)
- **Panel cũ:** 388.500 dòng, cross-check 7/7 PASS. *(Hạ tầng MỚI Pha B: panel chặng-3 = 292.500 dòng, ASEAN-5 × 126 HS6 × 52 đích, concordance pháp-lý-hóa — sạch hơn. Xem mục 6 "câu hỏi mở".)*
- **Biến phụ thuộc:** giá trị XK (PPML), khối lượng (PPML), unit value (OLS).
- **Treatment:** `EU_MRLₖₜ × EUᵈ` liên tục. Hai thước đo M1 (level) & M2 (thay thế), ρ(M1,M2)=0,34.
- **Ba đặc tả FE:**
  - **S1 Preferred (chính):** αᵢₖₜ + γᵈₜ — giữ ~11% biến thiên.
  - **S3 Minimum:** αᵢₖₜ + γᵈ — ~11,4%, β nhất quán S1.
  - **S2 Conservative:** + δᵢⱼₖ — chỉ 1,48% biến thiên, β ĐỔI DẤU (+0,89) → artifact, xuống robustness (Weidner-Zylkin: incidental parameter khi biến thiên quá ít).
- **Estimator:** PPML (Santos Silva-Tenreyro); ppml_fe_bias approximation (exact cần >131GB RAM, chỉ ảnh hưởng SE ±3-5%).

---

## 4. KẾT QUẢ CHÍNH (Đợt 1-2-3)

### H1 — Market access ✅ mạnh
- **S1-A1 PPML value: β₁ = −2,077*** (SE 0,427), semi-elasticity −87,5%.** Robust qua spec/cluster/treatment/margin. S3 = −2,036 (nhất quán). Quantity β = −3,514 (giảm khối lượng > giá trị → hợp với giá tăng).
- Hệ số LỚN hơn Fiankor (2020) (−0,06 đến −0,14); lý do: (1) treatment song phương vs đơn phương, (2) ASEAN-5 thị phần EU thấp → bị ảnh hưởng nặng hơn (Fiankor 2021), (3) Green Deal cấm hoạt chất hoàn toàn → chi phí cố định Melitz cao.

### Phi tuyến (B2/B3) — đóng góp đối thoại
- **B2 Quadratic: β₁=+20,62, β₂=−3,36*** → inverted-U, turning point 3,07** (trong miền [2,38; 4,26]).
- **Hòa giải Xiong-Beghin (2014, net dương cho OECD) vs Fiankor (2020, net âm cho EU):** dưới 3,07 demand-enhancing áp đảo, trên 3,07 trade-cost. P25 của MRL EU = 3,33 → phần lớn quan sát trên turning point → ròng âm.
- **B3 Bins: dose-response đơn điệu** (Q1 −1,07 → Q4 −2,42; monotonicity χ²=17,24, p<0,001).

### H3 — Reallocation ✅ chọn lọc (A4, baseline = USA)
| Thị trường | θ | p |
|---|---|---|
| EU | −0,914 | 0,025** |
| **Trung Quốc** | **+6,062** | 0,002*** |
| Ấn Độ | −1,996 | 0,008*** (ngược kỳ vọng — có thể IND cũng siết) |
| Nhật-Hàn | +1,144 | 0,107 |
| **ASEAN nội khối** | **+0,811** | 0,070* (đóng góp mới) |
- Joint test χ²(6)=24,21, p=0,0005. **Đóng góp mới: chưa bài MRL nào đo tái phân bổ.** Lưu ý θ_CHN SE lớn (1,91) → kiểm outlier.

### H2 — Unit value ⚠️ yếu
- A3 M1: +0,090* (p=0,093); B1b M2: −0,018 n.s. (đổi dấu). Within-R²=0,0006. → "weak cost pass-through, not robust". Đừng claim mạnh.

### Biên & robustness
- **Intensive margin chủ đạo** (E8 truncated PPML = −2,077 ≈ A1); extensive mơ hồ (LPM +0,029, PPML −0,182). Khác Ferro (2015 tìm extensive) — giải thích: ASEAN-5 quan hệ EU ổn định, ít đứt hẳn.
- **Cluster SE:** D2 (jur×k) bảo thủ nhất (SE +41%), vẫn p=0,001 → robust.
- **Event-study:** pre-trends FAIL (C1 TWFE: τ≤−3 = −5,49***, p≈0); balanced/cohort/SA-IW đều không cứu; SA-IW≈TWFE-OLS → loại staggered-bias (vấn đề là PPML value-weighting + nhị phân hóa). → PHỤ LỤC.
- **RESET:** S1 p=0,01 (nhẹ, treatment vẫn −2,28***); S2 p=1,8e-12 (mạnh).

---

## 5. ĐÁNH GIÁ TÍNH MỚI & ĐỐI THOẠI (NhatKy_P34 C.5)
- **KHÔNG mới:** tính hai mặt barrier/catalyst (Jaffee-Henson 2004, Xiong-Beghin 2014, Jiang 2023); chỉ số mũ phi tuyến trong *cách dựng treatment* (Li-Beghin 2014, Fiankor 2021); dạng phi tuyến/ngưỡng (Ferro 2015).
- **CÓ THỂ bảo vệ (incremental):** đặc tả **hình dạng** bằng nhiều phương pháp hội tụ (quadratic+spline+threshold+bins), hai đặc trưng + intensive margin, bối cảnh Green Deal trên nước xuất ĐNÁ. **Đóng góp thực nghiệm, KHÔNG phải first phương pháp.**
- **Đối thoại mạnh:** đường cong hòa giải Xiong-Beghin vs Fiankor; tái phân bổ là phần mới.
- **Framing đề xuất:** headline = **tái phân bổ + rào cản (H1) + hình-dạng-cong**; KHÔNG đặt phi tuyến đứng một mình làm novelty (dễ bị xem tái phát hiện tính hai mặt).
- **4 caveat bắt buộc kèm mọi phát biểu:** (1) tương quan có điều kiện KHÔNG nhân quả; (2) within-R² rất nhỏ (~0,1-0,2%) — đặc trưng gravity bão hòa; (3) ngưỡng vách nhận dạng yếu (đừng bám 3,07/3,85 chính xác); (4) độ lớn nhạy thành phần (HS9 cà phê/chè khuếch đại, top-value+TQ làm yếu).

---

## 6. CÒN GÌ PHẢI LÀM
- **Đợt 3 robustness (chưa chạy):** D5 loại 2020 (COVID), D4 EU aggregate, E1-E6 heterogeneity nhóm sản phẩm, placebo (random permutation — placebo cũ bị cộng tuyến).
- **CÂU HỎI MỞ quan trọng:** chạy lại Đợt 1-3 trên **hạ tầng MỚI** (concordance pháp-lý-hóa, panel chặng-3 292k dòng, scope rộng hơn) hay **giữ kết quả cũ** (panel 388k)? Hạ tầng mới sạch hơn nhưng kết quả cũ gần publication. → quyết ở phase viết. *Khuyến nghị: chạy lại trên hạ tầng mới để concordance pháp-lý-hóa làm điểm mạnh, nhưng kiểm kết quả có ổn định không trước.*
- **VIẾT bản thảo** (chưa bắt đầu). Bảng chính: A1 + B2 quadratic + B3 bins + A4 reallocation. Robustness: B1-M2 + B4-lag + D1-D3 cluster + E7-E8 margin. Phụ lục: event-study + thảo luận pre-trends.
- Đọc fulltext Ferro (2015) + luận án threshold TRƯỚC khi viết câu novelty (tránh trùng tiền lệ — NhatKy_P34 cảnh báo mới đọc abstract).

## 7. VỊ TRÍ ARTIFACT (Pha A — project knowledge / thư mục cũ)
- Do-files: `Dot1_MoHinhChinh_v2.do`, `Dot2_CungCo.do`, `Dot2_PreTrends_Investigation.do`, Đợt 3 (chưa).
- Outputs: `output_dot1/`, `output_dot2/` (.ster + .rtf + .csv + hình).
- Panel: `panel_prepared_v2.dta` (cũ), `panel_prepared_dot2.dta` (61 biến).
- Nhật ký chi tiết: NhatKy_P27 (Đợt 1), P28+P29 (Đợt 2), P30 (FE ladder), P34 (Đợt 3 phi tuyến), BaoCao_NhomB3 (methods gravity).
- Hạ tầng MỚI (Pha B): xem file 03.
