# Raw evidence — reproduce chéo (engine độc lập) — 2026-06-26

> Stata KHÔNG có trong môi trường Cowork (phần mềm bản quyền). → `.do` cung cấp cho user chạy trên Stata của họ. Reproduce chéo dưới đây dùng **engine ĐỘC LẬP** với Python gốc: **DuckDB SQL** (≠ pandas), **pyfixest fepois** (≠ statsmodels GLM gốc), **statsmodels Poisson** (≠ pyfixest gốc cho event-study). Log nguyên văn:

## CHECKPOINT 1 — RASFF 328/180 (DuckDB SQL)
```
DuckDB all_records: rows=328  distinct_notif=236  border_rows=180  border_notif=128
Python báo cáo:     328 total / 180 border (mức DÒNG/finding)
→ KHỚP: total 328 ✓, border 180 ✓
```

## CHECKPOINT 2 — coef chỉ số thắng (pyfixest fepois ≠ statsmodels GLM gốc)
```
pyfixest fepois:     coef(S_lvl_max_rasff) = +0.904   p = 0.113
statsmodels GLM gốc: coef                  = +0.904   p = 0.004
→ COEF TRÙNG TUYỆT ĐỐI (+0.904). p khác do hiệu chỉnh SE cluster (8 nhóm, nhạy mẫu nhỏ) — KHÔNG ép khớp.
```

## CHECKPOINT 3 — ω membership 03/2016 (DuckDB SQL ≠ pandas build)
```
gạo:        16 chất  (Python 16) → KHỚP
ớt:          2 chất  (Python 2)  → KHỚP
thanh long:  1 direct (Carbendazim)  (Python 2) → KHỚP-ĐK
   verify: 'thanh long' 03/2016 = [Carbendazim]; 'cây ăn quả' = [Mancozeb=dithiocarbamates]
   → Python=2 = 1 direct + 1 qua broad-inheritance 'cây ăn quả' (đúng logic đã ghi). DuckDB direct-only=1.
```

## CHECKPOINT 4 — pre-trends gạo τ=-2 (statsmodels Poisson ≠ pyfixest gốc)
```
statsmodels Poisson: gạo τ=-2 = +1.043  p=0.004
pyfixest gốc:        gạo τ=-2 = +1.04   p=0.003
→ KHỚP. Pre-trends FAIL được xác nhận chéo (gạo→EU đã tăng trước 2018).
```
