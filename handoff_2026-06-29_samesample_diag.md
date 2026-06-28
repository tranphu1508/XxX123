# Handoff — 2026-06-29 — ASEAN: diagnostic SAME-SAMPLE (mã loại có lái β=−2,077 không?)

## 1. Metadata
- Ngày giờ: 2026-06-29 | Thực thi: **Cowork** (làm chính)
- Task: VIỆC #1 trong `_KICKOFF_ASEAN_REDESIGN.md` — tách nguyên nhân β cũ↔mới bằng same-sample.
- Engine: **pyfixest fepois (PPML)**. **Tái lập full-185 KHỚP TUYỆT ĐỐI log Stata ppmlhdfe cũ** (S1 −2,0770 · S3 −2,0358 · S2 +0,8943) → engine hợp lệ. `.do` ppmlhdfe trọng tài đã kèm.
- Trạng thái: **HOÀN TẤT — nghi vấn STOP-RULE được GIẢI (bác bỏ giả thuyết "mã loại lái kết quả"). Chờ user chốt bước sau.**

## 2. Thiết kế
Giữ NGUYÊN cách dựng panel CŨ (treatment_M1 = **độ-ngặt TRUNG BÌNH** ánh xạ rổ hoạt chất × eu_dummy; 5 nước × 43 đích × 2015–2024), chỉ **đổi tập HS6** để cô lập tác động của việc concordance pháp-lý-hóa loại mã:
- **FULL** = 185 HS6 (toàn panel cũ) — để tái lập −2,077.
- **KEPT** = 112 HS6 cũ CÓ trong panel mới sạch (BACI 125 HS6). *(KICKOFF ghi "126" là ước lượng; số thực giao = 112; bản MRL-panel = 122.)*
- **DROPPED** = 73 HS6 cũ BỊ loại khi pháp-lý-hóa.

## 3. Kết quả (NGUYÊN VĂN — pyfixest, cluster i×j)
| Mẫu (dựng kiểu CŨ) | nHS6 | S1 (ikt+jt) | S3 (ikt+j+t) | S2 (ikt+jt+ijk) |
|---|---|---|---|---|
| **FULL** (tái lập) | 185 | −2,0770*** | −2,0358*** | +0,8943** |
| **KEPT** (mã sạch, có trong panel mới) | 112 | **−2,8781*** | −2,8629*** | +0,4965 (ns) |
| **DROPPED** (mã bị loại) | 73 | **−0,3209 (ns)** | −0,2201 (ns) | +1,9241** |
| KEPT (định nghĩa thay thế: MRL-panel) | 122 | −2,8835*** | −2,8682*** | +0,4866 (ns) |

Đặc tả 73 mã DROPPED: 16,7% tổng kim ngạch (28,0% kim ngạch đi-EU); **cùng chương HS** (07/08/09/10/12), **cùng độ-ngặt** (mean 3,49 vs 3,54), cùng số hoạt chất (~502) → KHÔNG phải nhóm sản phẩm khác; là các mã **khớp-mờ** mà pháp-lý-hóa gỡ bỏ.

## 4. VERDICT — giả thuyết STOP-RULE bị BÁC BỎ
- Nghi vấn cũ: *"loại mã 185→126 lái kết quả −2,077; giới hạn mã sạch → β về ~0"*. **SAI, ngược lại:**
  - Mã **sạch (112)** cho β **MẠNH HƠN: −2,88\*\*\*** (không phải ~0).
  - Mã **bị loại (73)** mới là **NULL: −0,32 (ns)**.
- **Cơ chế:** 73 mã khớp-mờ mang **treatment đo sai** (gán độ-ngặt nhầm HS6) → sai số đo cổ điển → **làm loãng** (attenuation) β về phía 0. Pháp-lý-hóa gỡ chúng → β sắc hơn −2,08 → **−2,88**. ⇒ **Concordance pháp-lý-hóa LÀM MẠNH H1, không làm yếu.**
- **Hệ quả cho panel mới:** β mới yếu/đổi dấu (S1 −1,47; S2 +0,15) **KHÔNG do loại mã.** Phải đến từ khác biệt CÒN LẠI: (a) thước đo **weakest-link vs mean**, (b) cấu trúc **BACI đa phương 52 đích/9 năm vs 43/10**.
- **S2 (3 chiều ijk) đổi dấu dương ở MỌI mẫu** (+0,50 → +1,92) → xác nhận đây là **artifact cấu trúc incidental-parameter (Weidner–Zylkin)**, lặp lại ở cả mean (đây) lẫn weakest-link (panel mới); **KHÔNG phải bất ổn riêng của panel mới.** (Khớp trực giác Xiong: thành phần demand-enhancing nổi lên khi FE 3 chiều hút hết biến thiên trade-cost.)

## 5. Đề xuất bước sau (CHỜ user chốt, chưa chạy)
1. **Tái-neo quyết định:** dùng concordance pháp-lý-hóa (nó gia cố kết quả). −2,077 cũ là cận DƯỚI (bị loãng); mã sạch = −2,88.
2. **Cô lập nốt thước đo:** chạy panel-cũ-clean-112 với **weakest-link** (hoặc panel-mới với **mean**) → tách phần −2,88→−1,47 là do "đo" hay do "cấu trúc đa phương".
3. Khung bài: S1/S3 (âm mạnh, ổn định) = mô hình chính; S2 = chỉ robustness (ghi rõ incidental-parameter). Giữ framing "tương quan có điều kiện".

## 6. Cờ review
- KHÔNG kích STOP-RULE: S1 (mô hình chính) âm mạnh & sắc hơn; không có pre-trends ở đây.
- Cần user xem: chấp nhận diễn giải "mã loại = nhiễu đo" + chọn bước 2 (tách thước đo) trước khi re-design đặc tả chính.

## 7. Con trỏ bằng chứng (trong `12_audit/`, không git-track vì repo chỉ-md)
- `samesample_diag_log_2026-06-29.txt` — log chạy nguyên văn (12 hồi quy).
- `samesample_results_2026-06-29.csv` — bảng hệ số.
- `samesample_hs6_membership_2026-06-29.csv` — 185 mã + cờ KEPT/DROPPED.
- `samesample_diag_2026-06-29.py` — script pyfixest.
- `samesample_diag_arbiter_2026-06-29.do` — bản ppmlhdfe để user chạy SE trọng tài.
