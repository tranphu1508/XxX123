# Kiểm toán tái lập: inventory artifact + reproduce chéo — 2026-06-26

> Xác minh dữ liệu THẬT (không chỉ tin báo cáo): (1) mọi artifact tồn tại/toàn vẹn/khóa duy nhất; (2) tái lập 4 con số quyết định bằng **engine độc lập** với Python gốc. Bằng chứng thô (hash, đếm, log) xuất ra repo. Quy tắc bằng chứng nguyên văn.

## CỔNG — PHẦN 1: INVENTORY = **SẠCH** (0 cờ đỏ thật) → mở Phần 2

| artifact | rows (thật) | key_unique | claimed vs actual |
|---|---|---|---|
| 01 BACI zip | 1.267.950.839 B | n/a | tồn tại ✓ |
| 01 EU MRL snapshot | 519.650 | n/a | **KHỚP** |
| 01 Annex I legal HTML | 1.430.139 B | n/a | tồn tại ✓ |
| 01 MARD MASTER | 26.877 data | n/a | KHỚP (claim 26.878 = wc-l **kèm header**) |
| 03 concordance_final_vn | 27 | YES | **KHỚP** (16 mã, có annex1_legal_ref) |
| 03 annex1_species_to_code | 1.305 | YES | **KHỚP** |
| 04 panel jan01 reference | 578.090 data | YES | KHỚP (claim 578.091 = wc-l kèm header) |
| 04 panel jan01 extended | 36.050 | YES | **KHỚP** |
| 04 mrl_time_variation_diag | 8.755 | YES | **KHỚP** |
| 05 omega_basket | 918 | YES | **KHỚP** |
| 05 omega_national_fallback | 54 | YES | **KHỚP** |
| 05 A_k_members | 57.957 | YES | **KHỚP** |
| 07 index_variants | 272 | YES | **KHỚP** |
| 07 index_weighted | 272 | YES | **KHỚP** |
| 07 natural_experiments | 62 | n/a | **KHỚP** |
| 07 baci_eventstudy_panel | 7.488 | YES | **KHỚP** |
| RASFF T4 / T5 / all_records | 78 / 18 / 328 | YES | **KHỚP** (T5=18 chất, all=328) |

**Không có artifact mồ côi/trống/khóa-trùng.** Hai "lệch" duy nhất = **off-by-one do header** (số "claimed" trước đây dùng `wc -l` tính cả dòng tiêu đề; data rows = claimed−1). Null trong `mrl_mg_kg` panel = **139.699 not_yet_set + 1.324 pending_celex** (ô được gắn cờ theo quy tắc (a)/(c), KHÔNG phải hỏng dữ liệu). → **CỔNG MỞ.**

## PHẦN 2 — REPRODUCE CHÉO
> **Stata KHÔNG có trong môi trường Cowork** (phần mềm bản quyền). → đã viết **`.do` sạch** (`reproduce_2A_validate_rasff.do`, `reproduce_2B_checkpoints.do`) cho người dùng chạy trên Stata + `ppmlhdfe`. Reproduce chéo tại đây dùng **engine ĐỘC LẬP** với Python gốc: **DuckDB SQL** (≠ pandas), **pyfixest fepois** (≠ statsmodels GLM gốc), **statsmodels Poisson** (≠ pyfixest gốc). Log nguyên văn: `raw_evidence_crosstool.log.md`.

### 4 CHECKPOINT QUYẾT ĐỊNH
| # | metric | Python gốc | engine độc lập | giá trị | verdict |
|---|---|---|---|---|---|
| 1 | RASFF total / border | 328 / 180 | DuckDB SQL | **328 / 180** | ✅ KHỚP |
| 2 | coef S_lvl_max_rasff | +0,904 (statsmodels) | pyfixest fepois | **+0,904** | ✅ KHỚP coef (p khác do SE cluster) |
| 3 | ω membership gạo/ớt | 16 / 2 (pandas) | DuckDB SQL | **16 / 2** | ✅ KHỚP |
| 3 | ω membership thanh long | 2 (pandas) | DuckDB direct | 1 + 1 inherit | ✅ KHỚP-ĐK (xem dưới) |
| 4 | pre-trends gạo τ=−2 | +1,04 (pyfixest) | statsmodels Poisson | **+1,043** | ✅ KHỚP (pre-trends FAIL xác nhận chéo) |

### Trích log nguyên văn các con số chốt
```
CP1 DuckDB:    all_records rows=328  border_rows=180          → 328/180 ✓
CP2 pyfixest:  coef(S_lvl_max_rasff)=+0.904 (statsmodels gốc +0.904) → coef TRÙNG TUYỆT ĐỐI
CP3 DuckDB:    gạo=16 ✓  ớt=2 ✓  thanh long direct=Carbendazim(1); 'cây ăn quả'=Mancozeb → +dithiocarbamates ⇒ Python=2
CP4 statsmodels: gạo τ=-2 = +1.043 p=0.004 (pyfixest gốc +1.04 p=0.003) → pre-trends FAIL ✓
```

### Ghi chú trung thực (không ép khớp)
- **CP2 p-value lệch** (0,004 statsmodels vs 0,113 pyfixest): **coef trùng tuyệt đối +0,904**; chênh p do hiệu chỉnh SE cluster khác nhau (8 nhóm → nhạy mẫu nhỏ). Điểm ước lượng tái lập chính xác; suy luận-SE phụ thuộc engine — Stata `ppmlhdfe` của user sẽ là trọng tài thứ 3.
- **CP3 thanh long**: cross-check lộ rõ membership=2 **phụ thuộc broad-inheritance** ('cây ăn quả' → Mancozeb/dithiocarbamates); direct 'thanh long' chỉ có carbendazim (1). Khớp logic Python đã ghi (kế thừa nhóm rộng) — KHÔNG phải lỗi, nhưng minh bạch rằng con số 2 dựa trên giả định inheritance.

## VERDICT
1. **Inventory SẠCH** — mọi artifact tồn tại, khóa duy nhất; 2 "lệch" = header-convention; null = cờ not_yet_set/pending. KHÔNG cờ đỏ.
2. **4 checkpoint KHỚP** (coef +0,904 trùng tuyệt đối; 328/180; ω 16/2; pre-trends τ=−2 +1,04). Cross-tool (DuckDB/pyfixest/statsmodels) xác nhận Python.
3. Hai minh bạch: CP2 p-value lệch (SE-impl, coef trùng); CP3 thanh long dựa inheritance. **Không ép khớp.**
4. Stata chưa chạy (không có trong Cowork) → `.do` cung cấp cho user; reproduce chéo bằng engine độc lập đã thay thế.

## DỪNG
Chờ Claude đọc bằng chứng thô (inventory + 4 checkpoint + log). Đề xuất user chạy `.do` trên Stata để có trọng tài thứ 3 (đặc biệt SE cluster CP2).
