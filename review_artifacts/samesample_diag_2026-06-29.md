# Review artifact — Same-sample diagnostic (2026-06-29)

**Hỏi:** 73 HS6 mà concordance pháp-lý-hóa loại có lái β=−2,077 (panel cũ, mean-stringency) không?
**Engine:** pyfixest fepois; tái lập full-185 KHỚP TUYỆT ĐỐI ppmlhdfe Stata cũ.

| Mẫu (dựng kiểu CŨ) | nHS6 | S1 ikt+jt | S3 ikt+j+t | S2 ikt+jt+ijk | N(S1) |
|---|---|---|---|---|---|
| FULL (tái lập) | 185 | −2,0770*** | −2,0358*** | +0,8943** | 308.994 |
| KEPT (mã sạch) | 112 | −2,8781*** | −2,8629*** | +0,4965 ns | 191.688 |
| DROPPED (mã loại) | 73 | −0,3209 ns | −0,2201 ns | +1,9241** | 117.306 |
| KEPT (alt: MRL-panel) | 122 | −2,8835*** | −2,8682*** | +0,4866 ns | 209.538 |

**73 mã DROPPED:** 16,7% kim ngạch (28% đi-EU), cùng chương HS 07/08/09/10/12, cùng độ-ngặt (3,49≈3,54), cùng ~502 hoạt chất → mã khớp-mờ, KHÔNG khác loại sản phẩm.

**Kết luận:**
1. Giả thuyết "mã loại lái −2,077" → **BÁC BỎ**. Mã sạch cho β **mạnh hơn (−2,88\*\*\*)**; mã loại **null (−0,32 ns)**.
2. Cơ chế = **attenuation do sai số đo** ở mã khớp-mờ; pháp-lý-hóa **gia cố** H1.
3. β panel mới yếu/đổi dấu **không do loại mã** → do thước đo (weakest-link vs mean) + cấu trúc đa phương.
4. S2 (3 chiều) đổi dấu dương ở MỌI mẫu → **artifact incidental-parameter**, không phải bất ổn panel mới.

Nguồn: `12_audit/samesample_*` (log, csv, py, do).
