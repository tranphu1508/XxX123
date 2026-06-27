# Reproduce crosscheck (4 checkpoint Python↔engine độc lập) — 2026-06-26

| checkpoint | metric | python_value | independent_engine | independent_value | tolerance | verdict |
|---|---|---|---|---|---|---|
| 1 RASFF density | total VN crop-pesticide | 328 | DuckDB SQL | 328 | <=1% | KHỚP |
| 1 RASFF density | border_rejection | 180 | DuckDB SQL | 180 | <=1% | KHỚP |
| 2 Index winner | coef S_lvl_max_rasff | +0.904 | pyfixest fepois | +0.904 | <=1% | KHỚP (coef trùng tuyệt đối) |
| 2 Index winner | p-value | 0.004 | pyfixest fepois | 0.113 | n/a | LỆCH-SE (cluster 8 nhóm; coef trùng |
| 3 omega membership | gạo #chất | 16 | DuckDB SQL | 16 | exact | KHỚP |
| 3 omega membership | ớt #chất | 2 | DuckDB SQL | 2 | exact | KHỚP |
| 3 omega membership | thanh long #chất | 2 | DuckDB SQL (direct) | 1 | exact | KHỚP-ĐK (1 direct carbendazim + 1 dithiocarbamates qua 'cây ăn quả' inheritance) |
| 4 Pre-trends | gạo τ=-2 coef | +1.04 | statsmodels Poisson | +1.043 | <=1% | KHỚP (pre-trends FAIL xác nhận chéo) |
