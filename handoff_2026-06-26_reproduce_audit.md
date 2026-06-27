# Handoff — 2026-06-26 — Kiểm toán tái lập (inventory + reproduce chéo)

## 1. Metadata
- Ngày: 2026-06-26 | Trạng thái: HOÀN TẤT — DỪNG | CỔNG Phần 1 SẠCH → Phần 2 chạy.

## 2. PHẦN 1 INVENTORY = SẠCH (0 cờ đỏ thật)
- 19 artifact (01_→07_ + RASFF): tồn tại hết, khóa duy nhất hết. 2 "lệch" = off-by-one HEADER (claimed dùng wc-l kèm header: MARD 26.878→data 26.877; panel 578.091→578.090). Null panel = 139.699 not_yet_set + 1.324 pending (cờ theo quy tắc, không hỏng). KHÔNG mồ côi/trùng.

## 3. PHẦN 2 REPRODUCE (Stata vắng → .do cho user + engine độc lập)
- **Stata KHÔNG có trong Cowork** → viết .do (2A validate ppmlhdfe + 2B 4 checkpoint) cho user. Reproduce chéo bằng DuckDB SQL / pyfixest / statsmodels (đều ≠ engine Python gốc).
- **4 CHECKPOINT KHỚP:**
  1. RASFF 328/180 (DuckDB) ✓
  2. coef S_lvl_max_rasff = **+0,904 trùng tuyệt đối** (pyfixest vs statsmodels gốc); p khác (0,113 vs 0,004) do SE-cluster impl — coef trùng, không ép p.
  3. ω membership gạo 16 ✓ ớt 2 ✓; thanh long 2 = 1 direct (carbendazim) + 1 inherit ('cây ăn quả'→dithiocarbamates) ✓-ĐK.
  4. pre-trends gạo τ=−2 = **+1,043** (statsmodels) khớp pyfixest +1,04 → pre-trends FAIL xác nhận chéo.

## 4. Output (12_audit/)
- inventory_audit.csv (19 artifact) + reproduce_crosscheck.csv (4 CP) + raw_evidence_crosstool.log.md (log nguyên văn) + reproduce_2A/2B.do (cho Stata user) + reproduce_audit report.

## 5. Cờ review (DỪNG)
- Không cờ đỏ. 2 minh bạch: CP2 p-value lệch (SE-impl, coef trùng) → user chạy Stata ppmlhdfe làm trọng tài; CP3 thanh long=2 dựa broad-inheritance.
