# Chẩn đoán SỨC NHẬN DIỆN của MRL (biến thiên thời gian) — 2026-06-26

> Phép thử TRƯỚC khi thiết kế chỉ số: MRL ràng buộc EU có đủ biến thiên THEO THỜI GIAN trong 2015–2023 để nhận diện chỉ số theo-thời-gian không? CHỈ ĐỌC panel + concordance; KHÔNG dựng chỉ số, KHÔNG sửa dữ liệu. Dữ liệu = chuỗi binding 2009–2024 dựng từ snapshot frozen (builder đã kiểm chứng 0 sai), 17 mã VN × A_k 515 chất (nêu bật 17 chất RASFF).

## Phương pháp & 2 giả định (minh bạch)
- **Baseline 2009, KHÔNG 2008:** MRL hài hoà EU có hiệu lực **01/09/2008** (Reg 149/2008) → mốc jan01-2008 đọc nhầm "not_yet_set" cho mọi chất, tạo bước giả 2008→2009. Dùng 2009 làm gốc.
- **not_yet_set → 0,01** (mặc định pháp lý Art 18(1)(b) Reg 396/2005: chất chưa liệt kê = LOD 0,01). Đây là ràng buộc thực mà nhà XK đối mặt. `pending_celex` (null) = không rõ → loại (pending_unknown).

## Bước 2 — KHỐI LƯỢNG NHẬN DIỆN (phân loại cặp chất×sản phẩm)

| Phân loại | Toàn A_k (8.755 cặp) | Tập RASFF (289 cặp = 17×17) |
|---|---|---|
| **step_in_window** (đổi ≥1 lần 2015–2023 — *tín hiệu quý nhất*) | **2.986 (34,1%)** | **95 (32,9%)** |
| step_before_window (siết trước 2015 rồi phẳng — cửa sổ BỎ LỠ) | 1.065 (12,2%) | 88 (30,4%) |
| flat_above_floor (hằng > 0,01 — chỉ đóng góp mức, không ID) | 936 (10,7%) | 27 (9,3%) |
| **flat_at_floor** (= 0,01 suốt — max-strict, không ID) | **3.586 (41,0%)** | 63 (21,8%) |
| pending_unknown (null) | 182 (2,1%) | 16 (5,5%) |

→ **~1/3 số cặp có bước trong cửa sổ** (nhận diện được); **41% phẳng-ở-sàn** (đã max-strict, đóng góp hằng số).

### Theo SẢN PHẨM (step_in_window / flat_at_floor, toàn A_k)
- **MRL ĐỘNG:** Chè 247/64 · Cà phê 246/64 · Parsley 256/104 · Basil 255/105 (rau thơm/đồ uống = nhiều bước, ít sàn).
- **MRL TĨNH (ít ID):** Thanh long 136/266 · Sầu riêng 136/266 · Vải/nhãn 136/269 · Chôm chôm 136/266 · Chanh leo 136/269 — **các quả nhiệt đới marquee MRL gần như tĩnh, phần lớn phẳng-ở-sàn**.
- Trung bình: Ớt 181/222 · Gạo 168/230 · citrus ~164/238.

### Theo CHẤT RASFF (17 sản phẩm) — PHÁT HIỆN THEN CHỐT
| chất (xếp theo #rejection) | in_window | before | flat_floor | flat_above | ID trong cửa sổ? |
|---|---|---|---|---|---|
| **carbendazim** (37) | 0 | **16** | 1 | 0 | ❌ siết 2011 → phẳng 0,1 |
| **permethrin** (32) | 0 | 0 | 0 | **17** | ❌ HẰNG (không đổi) |
| **chlorfenapyr** (30) | 0 | **16** | 0 | 1 | ❌ siết 2014 (trước cửa sổ) |
| chlorpyrifos (28) | **9** | 0 | 8 | 0 | ✅ (siết 2021 Green Deal) |
| tricyclazole (23) | **15** | 0 | 0 | 2 | ✅ (siết 2018: 1→0,01) |
| hexaconazole (21) | 0 | 14 | 0 | 3 | ❌ trước cửa sổ |
| acetamiprid (21) | — | — | — | — | (KHÔNG in-window, def (R) 2025+) |
| propiconazole (20) | **9** | 0 | 8 | 0 | ✅ |
| dithiocarbamates (16) | **17** | 0 | 0 | 0 | ✅✅ (mọi sp có bước) |
| imidacloprid (15) | **14** | 0 | 0 | 0 | ✅ |
| carbofuran (15) | 5 | 4 | 8 | 0 | ◑ |
| dinotefuran (13) | 0 | 1 | 0 | 0 | (16 pending null) |
| profenofos (12) | 5 | 0 | 12 | 0 | ◑ |
| cypermethrin (11) | 0 | **17** | 0 | 0 | ❌ trước cửa sổ |
| acephate (10) | 0 | 13 | 0 | 4 | ❌ |
| methamidophos (10) | 0 | 4 | 13 | 0 | ❌ phẳng-ở-sàn |
| dimethoate (8) | 4 | 0 | 13 | 0 | ◑ |
| fipronil (8) | **17** | 0 | 0 | 0 | ✅✅ (siết 2021: 0,01→0,005) |

**→ 3 chất gây từ chối NHIỀU NHẤT (carbendazim 37, permethrin 32, chlorfenapyr 30 = 99/~300 vụ) KHÔNG có biến thiên trong cửa sổ** (siết trước 2015 hoặc hằng). Tín hiệu nhận diện đến từ nhóm GIỮA: **tricyclazole, fipronil, dithiocarbamates, chlorpyrifos, imidacloprid, propiconazole**.

## Bước 3 — THỜI ĐIỂM CÚ SIẾT (histogram down-step 2009–2024)

```
year   #down(A_k)  #down(RASFF)
2012      100          2
2014      314         43   ← cụm TRƯỚC cửa sổ (carbendazim/chlorfenapyr/hexaconazole…)
2015*     134          0
2016*     717          5   ← CỤM LỚN: omnibus Reg (EU) 2015/868 cắt 48 chất → 0,01 trên MỌI sp
2017*      76          0
2018*      72         15   ← tricyclazole×gạo 1→0,01
2019*      28          0
2020*      87          0
2021*      86         26   ← Green Deal: chlorpyrifos, fipronil, dithiocarbamates
2022*     183          5
2023*      33         14
2024      194          2   (ngoài mẫu chính)
```
(* = trong cửa sổ 2015–2023)
- **77% cú siết (A_k) rơi TRONG cửa sổ** (1.416/1.830), 23% trước 2015. → regime siết mạnh trong cửa sổ.
- **NHƯNG cảnh báo: cụm 2016 = omnibus CHUNG** (Reg (EU) 2015/868, 48 chất × hầu hết sp, **bằng chứng nguyên văn dưới**) → siết ĐỒNG LOẠT, **bị year-FE hấp thụ**, đóng góp ÍT cho nhận diện WITHIN (cần biến thiên KHÁC-BIỆT product×year mới sống sót FE).
- **RASFF down-steps: 65 trong cửa sổ vs 45 TRƯỚC** → 41% cú siết của chất-nóng rơi trước 2015.

### Bằng chứng nguyên văn (chuỗi + record gốc)
```
tricyclazole × Gạo (step_in_window, siết 2018):
  2009..2017 = 1.0  →  2018..2024 = 0.01   (cắt mạnh 100×, đúng vụ EU siết tricyclazole trên gạo)
chlorpyrifos × Gạo (step_in_window):
  2009..2018 = 0.01 → 2019–2020 = 0.5 → 2021..2024 = 0.01  (Green Deal cấm chlorpyrifos 2020)
fipronil × Ớt (step_in_window, siết 2021): 0.01 → 0.005
carbendazim × Ớt & × Thanh long (step_BEFORE_window): 0.01(2009-10) → 0.1(2011→) phẳng suốt cửa sổ
  ↳ #1 RASFF nhưng MRL TĨNH trong 2015–2023
chlorfenapyr × Sầu riêng (step_before): 0.05 → 0.01 (2014, ngay trước cửa sổ)
omnibus 2016 — record gốc (2,4,5-T × ớt 0231020):
  01/09/2008 | 0.05* | Annex V | Reg.(EC) 149/2008
  30/12/2015 | 0.01* | Annex V | Reg.(EU) 2015/868   → binding jan01-2016 = 0.01 (siết chung)
```

## Bước 4 — VERDICT (thẳng)

**1. Đủ biến thiên trong cửa sổ?** CÓ nhưng KHU TRÚ. 34% cặp A_k (33% RASFF) có bước trong 2015–2023 — đủ để nhận diện một chỉ số theo-thời-gian *về tổng thể*, NHƯNG tín hiệu tập trung ở **nhóm chất giữa** (tricyclazole/fipronil/dithiocarbamates/chlorpyrifos/imidacloprid) và **sản phẩm động** (cà phê/chè/rau thơm/gạo). Quả marquee (thanh long/sầu riêng/vải) MRL gần tĩnh.

**2. Cú siết rơi đâu?** Chủ yếu TRONG cửa sổ (77% A_k). Cụm lớn: **2016 (omnibus chung — bị FE hấp thụ)**, 2021–2022 (Green Deal — KHÁC-BIỆT, quý), 2014 (trước cửa sổ). RASFF: 41% siết trước 2015.

**3. Phẳng-ở-sàn:** 41% (A_k) đã max-strict 0,01 suốt → đóng góp HẰNG SỐ, không nhận diện within. Cộng flat_above (11%) + pending (2%) → ~54% cặp KHÔNG mang biến thiên thời gian.

**4. ĐIỂM YẾU ID then chốt:** **3 chất gây rejection nhiều nhất (carbendazim, permethrin, chlorfenapyr) KHÔNG biến thiên trong cửa sổ** → chỉ số theo-thời-gian thuần (within/FE) sẽ YẾU cho đúng các chất "nóng" nhất. Cụm 2016 chung bị year-FE nuốt.

### KHUYẾN NGHỊ (chờ Claude/người dùng quyết, CHƯA làm)
- **Giữ 2015–2023 làm cửa sổ chính** (bắt 77% cú siết + các sự kiện sạch tricyclazole×gạo 2018, chlorpyrifos/fipronil 2021).
- **THÊM robustness kéo lùi 2011–2023** (hoặc 2012–2023) để bắt cú siết carbendazim (2011) + chlorfenapyr (2014) — *đúng các chất top-rejection*. Đây là đề xuất mạnh nhất.
- **Cảnh báo weak-ID theo-thời-gian** cho top-3 chất → bổ sung **nhận diện CẮT-NGANG** (mức strictness MRL khác nhau giữa sản phẩm) và/hoặc **trọng số chất** nghiêng về nhóm động; dựa vào các "thí nghiệm tự nhiên" product-specific (tricyclazole×gạo, chlorpyrifos×gạo, fipronil×ớt) thay vì cụm chung 2016.
- **KHÔNG** dựa cụm omnibus 2016 cho ID (year-FE hấp thụ).

## DỪNG
Đọc-panel xong. **CHƯA dựng chỉ số.** Chờ Claude/người dùng quyết cửa sổ (2015–2023 vs kéo lùi 2011–2023) + chiến lược nhận diện (thời-gian vs bổ sung cắt-ngang) TRƯỚC khi thiết kế chỉ số.
