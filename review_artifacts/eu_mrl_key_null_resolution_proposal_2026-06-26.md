> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/04_maximum_residue_level_panel/eu_mrl_key_null_resolution_proposal_2026-06-26.md, cập nhật 2026-06-26.

# Đề xuất phân giải khóa trùng & null — EU MRL — 2026-06-26

> Task CHẨN ĐOÁN + ĐỀ XUẤT. **CHƯA dựng bảng panel resolved.** Chờ người dùng/Claude xác nhận 3 quy tắc (a)(b)(c) ở cuối.

- Nguồn: snapshot đóng băng `01_raw_data_frozen/european_union_maximum_residue_level_snapshot/eu_mrl_bulkdownload_snapshot_2026-05-27.json` (519.650 record, CHỈ ĐỌC).
- Phạm vi phân tích (in-scope): HS 07–10 × A_k, lấy từ `concordance_EU_HS6_v3.csv` (eu_code→hs6, lọc hs2 ∈ {07,08,09,10}) + `A_k_members.csv` (cặp eu_code×pest_res_id, `in_A_k='yes'`). *Cờ MEDIUM đang mở: revision HS của concordance giả định HS2012, chưa chính thức (folder 03).*
- Công cụ: Python streaming NDJSON.

## Bước 1 — Con số in-scope (định mức ưu tiên)
- Tập in-scope: **57.957 cặp (hoạt chất × sản phẩm)**; **515 hoạt chất A_k**; **96 sản phẩm HS07–10** (concordance).
- **Khóa trùng (tie):** toàn DB **80.406 khóa** (chất×sp×ngày) bị trùng = **88.337 dòng dư**; **in-scope = 22.195 khóa**.
- **Null (mrl_value_only trống):** toàn DB **30.343**; **in-scope chỉ 579**.

→ Scoping thu nhỏ vấn đề rất mạnh: null in-scope chỉ 579/30.343.

## Bước 2 — Chẩn đoán 88k tie (KẾT LUẬN: không gây mơ hồ MRL)
- Tie sinh ra do **cùng (chất, sản phẩm, ngày) nằm ở nhiều Annex** (chủ yếu **Annex II vs Annex III**, đôi khi V), đôi khi nhiều regulation — với trạng thái applicability khác nhau.
- **Sau lọc `Applicable` + lấy `application_date` mới nhất** (in-scope): còn **11.726 cặp (chất×sp)** có >1 dòng ở ngày mới nhất — NHƯNG **số cặp có giá trị MRL KHÁC nhau = 0**.
- Tức là mọi tie dư đều là **bản ghi trùng across-annex CÙNG một giá trị MRL** (vd `0.01*` ở cả Annex II lẫn III). **Không có xung đột giá trị** → tie-break thế nào cũng ra cùng MRL.
- Ví dụ: hoạt chất id=1 × sản phẩm 0110030 (Lemons), 01/09/2008 — Annex II `0.01*` và Annex III `0.01*` (cùng reg 149/2008).

## Bước 3 — Chẩn đoán 30k null (KẾT LUẬN: trống thật, không phải lỗi parse; ràng buộc chỉ 40 ca)
- Phân biệt: **73.030 dòng "No MRL required" = Annex IV (hợp lệ, KHÔNG phải null cần xử lý)** — đã loại khỏi nhóm null.
- Null in-scope (579) theo applicability: **Applicable 42 | No longer applicable 535 | Not yet applicable 2**. Phần "No longer applicable" là lịch sử (không phải MRL đang ràng buộc).
- **Vấn đề thật:** số (chất×sp) in-scope mà **dòng `Applicable` MỚI NHẤT có MRL null = 40**. Nhiều ca trên Ginger (0840020).
- **Record thô xác nhận TRỐNG THẬT**, không phải parse-error: cả ba trường `mrl_lod`, `mrl_value`, `mrl_value_only` đều null trong record (không có giá trị giấu ở trường khác). Ví dụ: 2,4-DB × Ginger, Reg (EU) 2024/1077, Annex II, Applicable 06/11/2024 — mọi trường giá trị null.
- Các ca null ràng buộc đều thuộc **regulation gần đây** (2018–2024) đặt MRL → giá trị thật NẰM trong văn bản pháp lý (CELEX), không ở API.

## Bước 4 — Soi CELEX (xác thực pháp lý)
- `regulation_url` của 40 ca null ràng buộc trỏ tới **các regulation EU MRL có thật, gần đây** (2024/1077, 2022/1363, 2021/1807, 2020/1633, 2023/128, 2018/687, 2023/710…) trên EUR-Lex (CELEX / ELI).
- **Trích xuất trực tiếp giá trị từ EUR-Lex KHÔNG thực hiện được trong môi trường này**: `web_fetch` trả nội dung rỗng (trang EUR-Lex render bằng JavaScript/bảo vệ), và không có trình duyệt Chrome kết nối để render. → Việc đọc đúng ô MRL trong Annex là phần parse nặng, thuộc **task EUR-Lex backfill** hoặc tra cứu thủ công có chọn lọc cho **40 ca**.
- Kết luận khả thi: null **khôi phục được** từ CELEX (giá trị tồn tại trong văn bản), chỉ cần tra 40 ca (nhỏ, làm tay được). Với tie: do không xung đột giá trị, không cần CELEX để chọn dòng — mọi dòng cho cùng MRL.

## Bước 5 — ĐỀ XUẤT QUY TẮC (chỉ đề xuất — chờ xác nhận, CHƯA áp)

### (a) Chọn dòng đang áp dụng
- **Đề xuất:** lọc `applicability_text = "Applicable"`, rồi lấy dòng có `application_date` **mới nhất ≤ mốc-năm-t**, với **mốc-năm-t = 1/1 của năm t** (nhất quán quy ước "regulation áp giữa năm xử lý bằng lag" → MRL có hiệu lực trong năm t là MRL áp dụng tính tới 1/1/t).
- Đánh đổi: mốc 1/1 ⇒ regulation có hiệu lực trong năm t (sau 1/1) tính vào năm t+1 (thiên về lag, bảo thủ). Phương án khác: mốc 31/12/t (bắt cả thay đổi trong năm) — nêu để xác nhận.

### (b) Phá hòa khi còn trùng (sau (a))
- **Bằng chứng:** in-scope **0 xung đột giá trị** ở dòng mới nhất → mọi quy tắc cho cùng MRL; rủi ro với biến treatment = **0**.
- **Khuyến nghị:** dedup theo `mrl_value` trước (bỏ trùng y hệt); nếu vẫn >1 (khác annex cùng giá trị) → ưu tiên **Annex II > III > V** (thứ bậc pháp lý), phụ: regulation mới nhất. Lấy 1 dòng/cặp.
- **Phương án thay thế (bảo thủ):** lấy **MRL thấp nhất** (ngặt nhất). Vì không có xung đột giá trị nên kết quả y hệt phương án trên → không cần thiết, nhưng an toàn nếu sau này mở rộng phạm vi.

### (c) Xử lý null
- Quy mô thật: **40 (chất×sp) in-scope** có MRL Applicable mới nhất null (null là trống thật trong API).
- **Khuyến nghị (ưu tiên chính xác):** **tra CELEX có chọn lọc 40 ca** (regulation_url đã có sẵn) để điền giá trị thật + gắn cờ `source=eurlex_manual`; nếu một (chất×sp) có dòng `Applicable` không-null ở **ngày khác**, dùng giá trị đó (carry) thay vì để null.
- **Phương án thay thế:** loại 40 ca + gắn cờ (ảnh hưởng: 40/57.957 cặp in-scope ≈ **0,07%** — không đáng kể), hoặc impute theo default 0,01 (KHÔNG khuyến nghị vì có thể sai bản chất MRL).
- Đề xuất: **CELEX/ carry trước, drop+cờ chỉ khi không khôi phục được.**

## DỪNG
Đã DỪNG theo yêu cầu — **chưa dựng bảng panel resolved**. Chờ người dùng/Claude xác nhận (a) mốc-năm-t, (b) quy tắc phá hòa, (c) cách xử lý 40 null. Sau khi chốt sẽ ghi vào `analytical_decisions_log.md` và dựng panel ở bước apply.
