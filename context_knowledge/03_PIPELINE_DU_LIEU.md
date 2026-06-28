# 03 — PIPELINE DỮ LIỆU (hạ tầng dùng chung)

> Mọi artifact đã dựng + trạng thái. **Đã AUDIT** (inventory sạch, tái lập chéo DuckDB↔pandas khớp). Claude KHÔNG mở được file gốc của user — chỉ biết qua repo handoff (file 04). Đây là bản đồ những gì TỒN TẠI.

---

## 1. THƯ MỤC DỰ ÁN (Windows)
Gốc: `D:\Research\AGU Projects\EU standards Effects on ASEAN Agri-food Exports\`
- Container: `eu_maximum_residue_level_asean_export_study/` với thư mục số `00_`–`13_`:
  - `00_documentation`, `01_raw_data_frozen`, `02_data_collection`, `03_concordance`, `04_mrl_panel`, `05_active_ingredient_set`, `06_merge`, `07_main_estimation_stata`, `08-13` robustness/tables/audit/manuscript, `internal_handoff_log_for_claude`.
- Thông tư VN đã tải (nguồn Công báo Chính phủ): `...\Version 2\Dữ liệu pháp lý ASEAN\Việt Nam\Các thông tư` (14 thông tư 2013–2024).
- Quy ước: tên file English ASCII snake_case, ngày ISO.

## 2. ARTIFACT THEO GIAI ĐOẠN

### 01_ Dữ liệu đóng băng (frozen)
- **BACI** HS12, snapshot 202601. Thương mại song phương. ✅ validated.
- **EU MRL snapshot** (API, 2026-05-27): 519.650 dòng (chất × sản phẩm). ✅.
- **Annex I PHÁP LÝ** (Reg (EU) 2018/62, CELEX 32018R0062, frozen): 381 nhóm + 924 sub. Ground-truth cho concordance. ✅.
- **MARD MASTER** (rổ đăng ký): `MASTER_pesticide_crop_parsed.csv` 26.878 dòng, 14 thông tư 2013–2024, crop-level. ✅.

### 03_ Concordance EU→HS6
- **Lát VN:** `concordance_final_vn` — 17 mã, pháp-lý-hóa 17/17 chống Annex I, cột `annex1_legal_ref`. Sửa rambutan→0163060, thanh long 0162040→081090. ✅ FINAL.
- **Lát ASEAN:** `concordance_final_asean` — 304 mã thực-vật (loại 70 động vật + 7 nec), 284 có HS6, legal ref 304/304. 59 HS6-gộp, 20 umbrella (bỏ — nút mẹ). Verbatim bắt lá-dâu-tây 0632010≠quả. ✅ FINAL.
- Sửa phổ quát (lợi cả hai): melons 0233010→080719 (không phải watermelon).

### 04_ Panel MRL
- **Lát VN:** panel ràng buộc 17 mã (hàm-bậc-thang: application_date ≤ Jan-1-t, tie-break Annex II>III>V, not_yet_set→0,01, baseline 2009). thanh long ĐỦ. ✅.
- **Lát ASEAN:** `asean_mrl_panel` 137 HS6 × 13 năm = 1.781 dòng (77 sạch/60 gộp), weakest-link. ✅. **11 `lump_divergent`** (070920/40/51/60/70/99, 081010/20/30/40, 090421) — dùng mẫu-sạch loại 11 này.
- **mrl_time_variation_diagnostic:** 34% step-in-window, 41% flat-floor, 54% no time-var.

### 05_ Active ingredient set (A_k) + ω
- **A_k:** 515 chất. ⚠️ `acetamiprid` MISSING_FROM_A_k; `dinotefuran` null 16/17. Cả hai neonicotinoid — chờ CELEX recovery.
- **ω rổ đăng ký:** `omega_vn_registration_basket` (918 dòng, crop-level, 2016 chính + 2023 robustness) + `omega_vn_national_fallback`. banned-but-used carbofuran/methamidophos = 0 suốt mọi thông tư.

### 06_/07_ Chỉ số + ước lượng
- **Chỉ số VN:** `vn_stringency_index_variants` + `_weighted`. Biến thể THẮNG = weakest-link × RASFF-18 × level. ω-filter membership (fit RASFF kém hơn đều = kỳ vọng, double-dip; ω vẫn ngoại sinh cho phân tích). `vn_change_natural_experiments` (cú siết chế độ 2).
- **Ước lượng ASEAN (Pha A):** `output_dot1/`, `output_dot2/` — β=−2,077, quadratic, reallocation. Panel cũ `panel_prepared_v2.dta` / `panel_prepared_dot2.dta`.
- **Panel ASEAN mới (Pha B chặng-3):** 292.500 dòng (ASEAN-5 × 126 HS6 × 52 đích × 2015-2023), zero 81%, khóa duy nhất ✅. **event-study đã chạy → pre-trends FAIL (xem file 05).**

### RASFF
- `rasff_T4_product_x_year` + `rasff_T5_active_substances`: 328 notification/180 border. Nguồn: 2 file user tải (RASFF_window_results.xlsx 2019-2026 + RASFF pre-2021). pre21≤2020 + window≥2021 (tránh overlap).

## 3. AUDIT (đã qua)
- **Inventory CỔNG SẠCH:** 2 lệch = header off-by-1 (lành), null = cờ not_yet_set. Không file mồ côi.
- **Tái lập chéo (DuckDB độc lập với pandas):** RASFF 328/180 ✅; coef chỉ số +0,904 trùng tuyệt đối ✅; ω gạo16/ớt2 ✅; pre-trends gạo τ=−2 +1,04 ✅.
- **Stata:** Cowork không chạy được Stata trong môi trường nó → để lại `.do` cho USER chạy. **Chân Stata là việc user tự làm** (cross-tool đã làm bằng DuckDB).

## 4. CỜ PENDING / CẦN XỬ
- acetamiprid + dinotefuran CELEX recovery (2 neonicotinoid).
- 11 HS6 `lump_divergent` ASEAN → mẫu-sạch chính + robustness gồm chúng.
- Khử nội sinh cường-độ-kiểm-tra RASFF (Reg 2019/1793) — cho bài VN.
- Câu hỏi mở: chạy lại ASEAN Đợt 1-3 trên hạ tầng mới (292k) hay giữ cũ (388k) — xem file 01.

## 5. NGUỒN DỮ LIỆU
- BACI: CEPII. EU MRL: EU Pesticides Database API. Annex I: EUR-Lex Reg 2018/62. RASFF: RASFF Window + public pre-2021 (user tải tay). MARD đăng ký: Công báo Chính phủ VN (user tải tay, 14 thông tư). MRL đa đích (CHƯA có): Homologa = chuẩn nhưng bất khả với VN institutions (file 05).
