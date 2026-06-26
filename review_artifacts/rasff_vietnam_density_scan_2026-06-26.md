> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/02_data_collection_and_api_scripts/rasff_feasibility_scan/rasff_vietnam_density_scan_2026-06-26.md, cập nhật 2026-06-26.

# RASFF — Quét mật độ dữ liệu cho Việt Nam (kiểm tra khả thi, CHƯA đóng băng) — 2026-06-26

**Phạm vi:** notification/rejection dư lượng thuốc BVTV (pesticide residues) của Việt Nam trên nông sản HS 07–10. **Câu hỏi quyết định:** RASFF VN có **đủ dày** (vụ × sản phẩm × năm) để chạy mô hình đếm (Poisson/PPML), hay quá thưa → chỉ minh hoạ định tính?

> ⚠️ **TRẠNG THÁI: BÁN PHẦN.** Đường A (lập trình) **bị chặn hạ tầng** trong môi trường này; cần **Đường B (người dùng tải tay 1 cú click)** để ra bảng đếm vi mô chính xác. Báo cáo đưa **verdict SƠ BỘ có căn cứ** + **script sẵn sàng** (`scripts/parse_rasff_vietnam.py`) tự sinh 6 bảng khi có file. Đã DỪNG — không dựng phân tích, không đóng băng. (Mirror lần quét trước trong thư mục gốc cũ; xác nhận lại block trong phiên này.)

## 1. Đường lấy dữ liệu nào chạy được? (A vs B)
**Đường A — lập trình: ĐÃ THỬ, BỊ CHẶN** (nhất quán với giới hạn web phiên này: EUR-Lex rỗng, FAO timeout, không có Chrome):

| Nguồn | Kết quả |
|---|---|
| File EU Open Data `RASFF notifications pre-2021 public information.xlsx` (nguồn tốt nhất 2008–2020) | Tồn tại, NHƯNG sandbox `bash`/`curl` bị **proxy chặn (403 allowlist)**; `web_fetch` trả **[binary data]** (.xlsx nhị phân không parse được). |
| RASFF Window (`webgate.ec.europa.eu/rasff-window`) | SPA Angular → `web_fetch` rỗng; backend API là **POST có session** → GET-only không gọi được. |
| WFSR-WUR / Mendeley historical | Cần đăng nhập/dashboard tương tác hoặc nút "Download All" (trình duyệt). |

→ **Phải dùng Đường B** (xem `ROUTE_B_export_instructions.md`). **Độ phủ năm khả dĩ:** pre-2021 xlsx (≈2008–2020, có border rejection từ 2008) + export RASFF Window cho **2020–2025**. **% map HS:** script tính tự động khi có file (ước ≥85% ở HS4 cho nhóm nóng, tiền lệ Beestermöller 89%).

## 2. Bảng đếm (Bước 3) — KHUNG sẵn, dữ liệu CHỜ Đường B
`scripts/parse_rasff_vietnam.py` (đã có, kiểm thử logic) tự sinh vào `outputs/`:

1. `T1_vn_all_hazards_by_year.csv` — VN tổng mọi hazard/năm (bối cảnh).
2. `T2_vn_pesticide_by_year.csv` — VN pesticide residues/năm (2008–2025).
3. `T3_vn_pesticide_by_year_x_type.csv` — tách **border rejection / alert / information**.
4. `T4_vn_pesticide_product_x_year.csv` + `T4b_vn_product_totals.csv` — **sản phẩm (HS4/nhóm) × năm** (bảng then chốt).
5. `T5_vn_active_substance_counts.csv` — theo hoạt chất (nối tập A_k / chỉ số MRL).
6. Cờ **enhanced-control** Reg (EU) 2019/1793 (lấy tay từ Annex — biến cường-độ-kiểm-tra nội sinh).

Logic: origin=Viet Nam → giữ hazard chứa *pesticide* (kể cả đa-hazard) → **loại HS03/thuỷ sản/thú y** → map mô tả→HS4 nhóm nóng → đếm. In `_SUMMARY_verdict_inputs.txt` (tổng, %border, product-year ≥20/≥30).

## 3. VERDICT SƠ BỘ: **BIÊN GIỚI (BORDERLINE)** — *cần xác nhận bằng số đếm thực (Đường B)*
Từ nguồn công bố (chưa có vi mô VN — cần kiểm bằng export):
- **VN là origin HẠNG TRUNG** cho pesticide residues, KHÔNG top-3 (Drożdż et al. 2022: dẫn đầu Ấn Độ ~18,1%, Thổ Nhĩ Kỳ ~17,6%, rồi Trung Quốc). → tổng vụ VN ước **trăm–vài trăm** trên 2008–2025, không phải hàng nghìn.
- **Tập trung số ít sản phẩm nóng** (điểm quyết định khả thi): **ớt/peppers (Capsicum)** (2019 tỷ lệ phát hiện không tuân thủ rất cao), **đậu bắp (okra)** (kiểm soát tăng cường), **thanh long**, **rau thơm (ngò/húng/bạc hà)**; mới nổi: **sầu riêng, chanh leo, gạo**.
- **Border rejection ≈ một nửa** tổng notification pesticide → border-only còn thưa hơn ~½.

**Suy ra cho Poisson/PPML:**
- ✅ Mô hình đếm **GỘP trên ~5–8 sản phẩm nóng** (product FE + year FE + kiểm soát cường-độ-kiểm-tra), tổng **vài trăm sự kiện** → *có thể chạy* PPML.
- ⚠️ Ma trận product×year **đầy đủ rất THƯA** (đa số ô 0–3 vụ; chỉ vài product-year đỉnh ~20–40 khi bị liệt Annex) → fine-grained product×year×hoạt-chất **KHÔNG đủ**.
- ❌ Border-rejection-only theo product×year: **quá thưa** cho mô hình đếm độc lập.

→ **BIÊN GIỚI:** đủ cho **một mô hình đếm GỘP có kiểm soát**, KHÔNG đủ làm **trụ kinh tế lượng đứng một mình** ở mức chi tiết. **Khuyến nghị vai trò RASFF:** biến kết quả đếm **thứ cấp/bổ trợ trên nhóm sản phẩm nóng** (kèm cờ enhanced-control) **+ minh hoạ định tính**; trụ định lượng chính dựa nguồn dày hơn (MRL gap, kim ngạch BACI).

> **Để CHỐT:** chạy `parse_rasff_vietnam.py` trên file Đường B → đọc `_SUMMARY`. Nếu **tổng ≥ ~300** và **≥2–3 product-year ≥20 (2018–2024)** → nâng **ĐỦ (gộp)**. Nếu tổng < ~150 và không product-year nào ≥20 → hạ **THƯA → chỉ định tính**.

## 4. Caveat bắt buộc
- **Nội sinh cường-độ-kiểm-tra:** sản phẩm VN bị liệt Annex I/II Reg (EU) 2019/1793 (kiểm 10–50%/lô) → **nhiều kiểm ⇒ nhiều phát hiện**, không thuần mức dư lượng. Count RASFF đồng biến cường độ kiểm → phải đưa **cờ enhanced-control (product-year)** làm biến kiểm soát/offset.
- **Lệch HS4 vs HS6:** RASFF chỉ mô tả chữ → map tới **HS4** (~89%); ghép thương mại HS6 mất độ phân giải. Ghi rõ phần UNMAPPED.
- **Đa-hazard (~18,7%):** giữ nếu CHỨA pesticide (tránh bỏ sót), không đếm trùng sang hazard khác.
- **Đứt gãy độ phủ:** cổng công khai 2020+; pre-2020 ở file lưu trữ → 2 nguồn lệch thời điểm, nối cẩn thận.
- **Verdict trên là SƠ BỘ** từ tổng hợp công bố, **chưa phải số đếm vi mô VN**.

## 5. Nguồn (raw URL — để Đường B + kiểm chứng)
- File chính thức (Đường B): `https://data.europa.eu/euodp/data/storage/f/2021-06-03T125456/RASFF%20notifications%20pre-2021%20public%20information.xlsx` (EU Open Data, CC-BY 4.0).
- RASFF Window (export 2020+): `https://webgate.ec.europa.eu/rasff-window/screen/list`
- Drożdż et al. 2022 (pesticide-RASFF): `https://pmc.ncbi.nlm.nih.gov/articles/PMC9324178/`
- Border rejections 2008–2023 (MDPI Sustainability): `https://www.mdpi.com/2071-1050/17/7/2923`
- Enhanced controls Reg 2019/1793 (Annex hợp nhất): `https://eur-lex.europa.eu/eli/reg_impl/2019/1793/oj`

## 6. Bước tiếp (DỪNG tại đây)
1. Người dùng tải file theo `ROUTE_B_export_instructions.md` → đặt vào `raw/`.
2. `python scripts/parse_rasff_vietnam.py` → đọc `outputs/_SUMMARY_verdict_inputs.txt` + T1–T5.
3. Chốt verdict ĐỦ/BIÊN GIỚI/THƯA theo ngưỡng §3. **Chưa đóng băng, chưa dựng phân tích.**
