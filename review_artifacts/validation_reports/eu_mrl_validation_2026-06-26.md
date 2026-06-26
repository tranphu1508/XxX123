> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/02_data_collection_and_api_scripts/validation_reports/eu_mrl_validation_2026-06-26.md, cập nhật 2026-06-26.

# Báo cáo kiểm định EU MRL (API) — 2026-06-26

- Nguồn: **EU Pesticides Database** (UI v3.3), **API v3.0** — datalake SANTE.
- Endpoint bulk MRL: `https://api.datalake.sante.service.ec.europa.eu/sante/pesticides/pesticide-residues-mrls-download?language_code=EN&format=json&api-version=v3.0` (toàn bộ lịch sử + hiện hành + tương lai).
- **NGÀY SNAPSHOT: 2026-05-27** (DB không có mã version → ngày tải = phiên bản; không fetch lại y hệt được).
- Artifact: `eu_mrl_bulkdownload_snapshot_2026-05-27.json` — **NDJSON** (1 record/dòng), 367.899.606 bytes, **519.650 record**. SHA-256 `bc3643ec…a798bb`.
- ⚠ DB **"không có giá trị pháp lý"** → cần đối chiếu EUR-Lex (task backfill kế tiếp). API chỉ là lớp tiện lợi.

## Bước 0 — Endpoint / định dạng / độ phủ
- Endpoint datalake SANTE, API v3.0; 3 file: `pesticide-residues-mrls-download` (MRL, dùng ở đây), `pesticide-residues-products` (cây sản phẩm), `active-substances-download` (metadata hoạt chất). Định dạng JSON (NDJSON) hoặc CSV.
- **Độ phủ thời gian: application_date 2008–2026** → phủ TRỌN 2015–2024. API CUNG CẤP lịch sử (không cần EUR-Lex bù về độ phủ; EUR-Lex chỉ để xác thực pháp lý).
- Bản pull cũ: V1 `PIMS_..._MRL_LANGUAGE.json` (2026-05-22), V2 `EU_MRL_BulkDownload.json` (2026-05-27) — cùng endpoint/format. V2 là snapshot đóng băng.

## A. Độ đầy đủ — ĐẠT
- 519.650 record; **704 hoạt chất** (pesticide_residue_id); **381 sản phẩm** (product_code EU); **229 regulation**.
- Độ phủ năm (application_date): 2008–2026 liên tục; 2015 = 49.790; không năm nào trống.
- Trạng thái áp dụng: Applicable 299.655 | No longer applicable 211.994 (lịch sử) | Not yet applicable 8.001 (tương lai).
- Giao với rổ A_k: tập A_k đã dựng sẵn (`A_k_members.csv`/`A_k_summary.csv` ở Version 2) → đối chiếu được; 704 hoạt chất là toàn bộ tập EU.

## B. Tính toàn vẹn — ĐẠT (1 cờ cấu trúc)
- Schema nhất quán: 0 dòng lệch bộ khóa so với dòng đầu (19 trường).
- `product_code`: **100% là chuỗi 7 ký tự, giữ số 0 đầu** (vd "0110030") — đúng yêu cầu để map sang HS2012 (folder 03).
- Tham chiếu: mỗi dòng có `regulation_number` + `regulation_url` (EUR-Lex CELEX) + hoạt chất + sản phẩm.
- Checksum SHA-256: xem `01_/.../checksums_2026-05-27.txt`.
- **CỜ — khóa (chất × sản phẩm × ngày áp dụng) KHÔNG duy nhất: 88.337 dòng trùng.** Nguyên nhân (không phải hỏng): cùng một (hoạt chất, sản phẩm, ngày) xuất hiện dưới **nhiều regulation / nhiều Annex** với trạng thái khác nhau (vd vừa "Applicable" ở Annex III vừa "No longer applicable" ở Annex II). → Khi dựng panel (folder 04) phải dùng khóa đầy đủ hơn + logic chọn dòng "đang áp dụng".

## C. Chất lượng — ĐẠT (kèm cờ null + cờ pháp lý)
- **Biểu diễn MRL mặc định/LOD (cốt lõi treatment):** default = `mrl_lod="*"`, `mrl_value="0.01*"`, `mrl_value_only="0.01"`. Tổ hợp ở mức mặc định/LOD xuất hiện **TƯỜNG MINH thành dòng** (không vắng mặt). **70,7% số dòng (367.314) ở mức LOD/default** ("*").
- `mrl_value_only`: số hợp lệ 416.277 dòng (min 0,001 — max 1500 mg/kg; **không có ≤0**); "No MRL required" 73.030 dòng (= đúng toàn bộ **Annex IV**, chất miễn MRL); **null 30.343 dòng (CỜ)** — `mrl_value` cũng null, đa phần ở Annex II/III "Applicable" → cần xem ở bước dựng treatment.
- Đơn vị: mg/kg (chuẩn DB; không có trường đơn vị riêng → ngầm định mg/kg).
- Annex: II 234.656 | V 111.367 | III 100.597 | IV 73.030.
- **Cờ pháp lý:** DB "no legal value" → đối chiếu EUR-Lex (task sau).

## Bước 3 — Diff snapshot cũ (2026-05-22) → mới (2026-05-27)
So trên khóa (chất, sản phẩm, ngày áp dụng, regulation, annex):

| Chỉ tiêu | Kết quả |
|---|---|
| Khóa chung khớp giá trị MRL | **100,00%** (đổi giá trị = 0) |
| Thay đổi ở phần **hiện hành** | 0 |
| Thay đổi ở phần **lịch sử** (đính chính hồi tố) | **0** ✓ |
| Mục **chỉ có ở bản mới** (thêm) | 762 — **toàn bộ là "tương lai" (Not yet applicable)** |
| Mục mất ở bản mới | 0 |

→ Khác biệt giữa hai snapshot 5 ngày = chỉ 762 MRL tương lai mới (regulation mới công bố), **không có đính chính hồi tố** phần lịch sử, **không lỗi pipeline**. (Lưu ý: diff trên khóa đã gộp trùng theo last-wins; kết luận "không đổi hồi tố" vẫn vững.)

## Kết luận
Snapshot EU MRL 2026-05-27 ĐẠT 3 nhóm, đủ điều kiện đóng băng làm lớp dữ liệu treatment. Mang theo downstream: (1) khóa panel phải gồm regulation+annex+applicability (88k trùng trên khóa rút gọn); (2) 30.343 MRL null cần xử lý ở bước treatment; (3) đối chiếu EUR-Lex để có giá trị pháp lý; (4) ràng buộc product_code EU → HS2012 (folder 03).
