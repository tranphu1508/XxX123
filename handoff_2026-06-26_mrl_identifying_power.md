# Handoff — 2026-06-26 — Chẩn đoán sức nhận diện MRL (biến thiên thời gian)

## 1. Metadata
- Ngày: 2026-06-26 | Task: chẩn đoán identifying power TRƯỚC khi dựng chỉ số | Trạng thái: HOÀN TẤT — DỪNG
- CHỈ ĐỌC panel/snapshot; KHÔNG dựng chỉ số, KHÔNG sửa dữ liệu.

## 2. Đã làm
- Dựng chuỗi binding 2009–2024 (17 mã VN × A_k 515) từ snapshot frozen (builder kiểm chứng 0 sai). Baseline 2009 (MRL hài hoà 01/09/2008); not_yet_set→0,01 (Art 18 default); pending→loại.
- Phân loại mỗi cặp: step_in_window / step_before_window / flat_above_floor / flat_at_floor / pending.
- Histogram cú siết 2009–2024; đối chiếu chất RASFF.

## 3. KẾT QUẢ
- **Khối lượng:** toàn A_k (8.755 cặp): step_in_window 34,1% | flat_at_floor 41,0% | step_before 12,2% | flat_above 10,7% | pending 2,1%. RASFF (289): step_in_window 32,9%.
- **Cú siết:** 77% rơi TRONG cửa sổ. Cụm: **2016 omnibus Reg (EU) 2015/868 (CHUNG → year-FE hấp thụ)**, 2021–2022 Green Deal (khác-biệt, quý), 2014 (trước cửa sổ).
- **ĐIỂM YẾU then chốt:** 3 chất top-rejection (carbendazim 37 siết 2011, permethrin 32 hằng, chlorfenapyr 30 siết 2014) KHÔNG biến thiên trong cửa sổ. Tín hiệu ID từ tricyclazole/fipronil/dithiocarbamates/chlorpyrifos/imidacloprid.
- **Sản phẩm:** cà phê/chè/rau thơm động; thanh long/sầu riêng/vải/chôm chôm gần tĩnh (266/515 phẳng-ở-sàn).

## 4. VERDICT
- Cửa sổ 2015–2023 đủ ID *tổng thể* nhưng KHU TRÚ (nhóm chất giữa + sp động). Weak-ID theo-thời-gian cho top-3 chất.
- KHUYẾN NGHỊ: giữ 2015–2023 chính + **robustness kéo lùi 2011–2023** (bắt carbendazim/chlorfenapyr) + bổ sung nhận diện CẮT-NGANG + trọng số chất động; KHÔNG dựa cụm chung 2016.

## 5. Output
- 04_/outputs/mrl_time_variation_diagnostic.csv (8.755 cặp × phân loại + chuỗi 2009-2024).
- 04_/mrl_identifying_power_2026-06-26.md (báo cáo + histogram + verdict + verbatim).

## 6. Cờ review
- Claude/người dùng quyết: cửa sổ (2015–2023 vs kéo lùi 2011–2023) + chiến lược ID (thời-gian vs cắt-ngang) TRƯỚC khi thiết kế chỉ số.
