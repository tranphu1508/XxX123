> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/02_data_collection_and_api_scripts/rasff_feasibility_scan/rasff_vietnam_density_scan_2026-06-26.md, cập nhật 2026-06-26.

# RASFF — Quét mật độ VN — **ĐÃ CÓ SỐ ĐẾM THỰC** — 2026-06-26

> ✅ **Route B thành công:** người dùng đã tải 2 file (đặt ở `raw/`); Cowork reproduce **KHỚP** số Claude tính (328/180). Verdict nâng **BIÊN GIỚI → ĐỦ (gộp)**. KHÔNG đóng băng, KHÔNG dựng phân tích — DỪNG chờ Claude xác nhận trước khi thiết kế chỉ số/panel.

## 1. Đường dữ liệu & reproduce
- **Nguồn (raw/):** `RASFF notifications pre-2021 public information.xlsx` (EU Open Data, ≤2020) + `RASFF_window_results.xlsx` (RASFF Window export origin=Viet Nam, ≥2021). Provenance: `raw/SOURCES.md`.
- **Logic (script `scripts/parse_rasff_vietnam.py`):** origin~'viet'; pre-2021 hazard category~'pesticide' (mức DÒNG/finding) cho ≤2020 + loại seafood theo `product category` + loại từ `type2`; window pesticide từ free-text `hazards` (nhãn/hoạt chất) cho ≥2021 + loại seafood theo `category` + loại từ `classification`. Gộp.
- **Reproduce KHỚP:** TỔNG VN crop-pesticide = **328** (mục tiêu 328 ✓), border rejection = **180** (mục tiêu 180 ✓). Theo năm khớp từng năm.

## 2. Bảng pesticide VN theo năm + loại thông báo

| Năm |2002 | 2006 | 2007 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n | 4 | 2 | 1 | 4 | 4 | 1 | 12 | 18 | 37 | 18 | 18 | 29 | 22 | 10 | 18 | 32 | 22 | 43 | 19 | 14 |

Theo loại: **border_rejection 180** | information 114 | alert 34.
(T2/T3 trong `outputs/`.)

## 3. Sản phẩm × năm (bảng then chốt) + hoạt chất
Tổng theo sản phẩm: **ớt/tiêu 100**, **thanh long 61**, **other 57**, **trái cây khác 33**, **cà phê/chè 32**, **rau thơm 15**, **gạo 15**, **sầu riêng 9**, **đậu bắp 6**.

| sản phẩm | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| ớt/tiêu | 2 | 17 | 4 | 2 | 4 | 6 | 20 | 3 | 3 |
| thanh long | 1 | 2 | 1 | 0 | 1 | 7 | 7 | 9 | 1 |
| other | 7 | 1 | 3 | 7 | 11 | 0 | 1 | 0 | 0 |
| trái cây khác | 0 | 0 | 0 | 7 | 3 | 3 | 1 | 4 | 5 |
| cà phê/chè | 19 | 0 | 0 | 0 | 1 | 2 | 4 | 1 | 1 |
| rau thơm | 0 | 0 | 0 | 2 | 5 | 0 | 2 | 1 | 1 |
| gạo | 0 | 2 | 2 | 0 | 7 | 1 | 0 | 1 | 0 |
| sầu riêng | 0 | 0 | 0 | 0 | 0 | 3 | 6 | 0 | 0 |
| đậu bắp | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 |

**Product-year ≥20:** chỉ **1 ô** (ớt/tiêu 2024 = 20) → mức product×year quá thưa cho mô hình chi tiết; nhưng GỘP đủ dày.

Top hoạt chất (reproduce): carbendazim 37, permethrin 32, chlorfenapyr 30, chlorpyrifos 28, tricyclazole 23, hexaconazole 21, acetamiprid 21, propiconazole 20, dithiocarbamates 16, carbofuran 15.
- *Lưu ý trung thực (lệch >5%):* số đếm hoạt chất của tôi CAO hơn mục tiêu Claude ở các chất do **file window liệt nhiều hoạt chất/notification** (tôi đếm mọi chất liệt kê; vd permethrin 32 vs ~8). **carbendazim vẫn #1 ở cả hai** → kết luận thiết kế không đổi. Tương tự nhóm 'other' của tôi =57 vs Claude 81 (tôi gom thêm ~24 ca vào trái-cây-khác/rau-thơm) — TỔNG không đổi, chỉ khác hạt mịn phân nhóm.

## 4. VERDICT: **ĐỦ (gộp)**
- Tổng **328 ≥ 300**; **border rejection 180** tự đủ chạy Poisson/PPML gộp; nhiều NĂM (tổng) ≥20 trong 2018–2024 (2018=29, 2022=32, 2024=43…).
- ✅ Chạy được **một bảng hồi quy đếm GỘP** trên ~5–8 nhóm sản phẩm nóng (**product FE + year FE + offset enhanced-control**).
- ❌ KHÔNG đủ ở mức **product×year×hoạt-chất** chi tiết (chỉ 1 product-year ≥20).
- **Vai trò RASFF:** **trụ định lượng BỔ TRỢ** (một bảng đếm gộp thực thụ, không phải minh hoạ suông) + minh hoạ định tính; trụ chính vẫn là MRL gap × kim ngạch BACI.

## 5. Hai phát hiện thiết kế
1. **Hoạt chất VN ≠ 'bộ 5 Nguyen':** **carbendazim DẪN ĐẦU** (rồi carbofuran/hexaconazole/tricyclazole/chlorpyrifos…) → tập A_k và chỉ số MRL phải **neo theo hoạt chất thực tế gây rejection của VN**, không bê nguyên bộ chất của nghiên cứu khác.
2. **Nội sinh cường-độ-kiểm-tra HIỆN RÕ:** ớt/tiêu vọt **2019 (17) và 2024 (20)**, **sầu riêng 2023→2024 (3→6)**, cà phê/chè **2018 (19)** — trùng thời điểm sản phẩm bị liệt **enhanced-control Reg (EU) 2019/1793**. Count đồng biến cường độ kiểm → **bắt buộc đưa cờ enhanced-control (product-year) làm offset**, nếu không hệ số thiên lệch nội sinh.

## 6. 20 subject 'other' hay gặp (để refine mapping — Bước 2, chưa cần xong)
```
7× cyromazine (0.28 mg/kg - ppm) and unauthorised substances carbofuran (0.008 mg
3× spirotetramat (0.18 mg/kg - ppm) and unauthorised substances methamidophos (0.
3× cyromazine (0.09 mg/kg - ppm) and flubendiamide (0.03 mg/kg - ppm), too high c
3× too high content of nitrate (4700 mg/kg - ppm) and unauthorised substances car
2× unauthorised substances methamidophos (0.04 mg/kg - ppm) and acephate (0.026 m
2× unauthorised substances chlorpyrifos (0.05 mg/kg - ppm) and dimethoate (0.04 m
2× Exceedance of the maximum level of ethylene oxide in vegetable mix in instant 
2× dimethoate (sum: 0.60 mg/kg - ppm) and unauthorised substance omethoate in bea
2× unauthorised substances methamidophos (0.17 mg/kg - ppm) and acephate (0.69 mg
2× unauthorised substances carbofuran (0.04 mg/kg - ppm) and chlorfluazuron (0.1 
2× unauthorised substances methamidophos (0.032 mg/kg - ppm) and acephate (0.032 
2× unauthorised substances carbendazim (5.10 mg/kg - ppm) and chlorfenapyr (0.02 
2× Ethylene oxide in instant noodles from Vietnam
1× unauthorised substance carbofuran (0.2 mg/kg - ppm) in yard long beans from Vi
1× unauthorised substance methamidophos (9.7 mg/kg - ppm) in water spinach (Ipomo
1× unauthorised substance carbendazim (4.1 mg/kg - ppm) in pak wan vegetables (Sa
1× unauthorised substance fipronil (0.51 mg/kg - ppm) in dried black mushrooms fr
1× unauthorised substance carbofuran (0.018 mg/kg - ppm) in pickled cucumbers fro
1× unauthorised substance carbofuran (0.038 mg/kg - ppm) in bitter gourds from Vi
1× unauthorised substance carbendazim (24 mg/kg - ppm) in spinach from Vietnam
```
Đa số 'other' là **rau ăn lá/củ-quả ăn kèm + đa-hoạt-chất + chế biến/hỗn hợp** (rau muống, pak wan, yard-long beans, bitter gourd, pickled cucumber, vegetable mix, instant noodles…) — refine sẽ kéo phần lớn về rau/đậu, giảm 'other'.

## 7. Caveat
- **Lệch HS4-vs-HS6:** RASFF chỉ tới HS4/nhóm; ghép thương mại HS6 mất độ phân giải (phần UNMAPPED khi map HS4 — bước sau).
- **Gap 2021:** cổng công khai 2020+ nhưng pre-2021 tới 2020 + window từ 2021 → **đã lấp liền mạch** (2021=18).
- **Đa-hazard:** giữ notification nếu CHỨA pesticide (window), không đếm trùng sang hazard khác.
- **Đơn vị đếm:** pre-2021 ở mức DÒNG/finding (khớp Claude); window ở mức notification.

## DỪNG
Đã reproduce + nâng verdict **ĐỦ (gộp)**. **Chưa đóng băng, chưa dựng panel.** Chờ Claude đọc xác nhận trước khi thiết kế chỉ số/panel (kèm offset enhanced-control + neo hoạt chất VN).