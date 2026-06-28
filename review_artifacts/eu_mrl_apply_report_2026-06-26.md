> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/04_maximum_residue_level_panel/eu_mrl_apply_report_2026-06-26.md, cập nhật 2026-06-26.

# Báo cáo apply — EU MRL binding panel — 2026-06-26

Dựng bảng MRL ràng buộc (hoạt chất × sản phẩm × năm) theo 3 quy tắc đã chốt (a/b/c — xem `00_/analytical_decisions_log.md`). Đọc từ frozen snapshot `01_/.../eu_mrl_bulkdownload_snapshot_2026-05-27.json` (CHỈ ĐỌC). Phạm vi: in-scope A_k (515 hoạt chất) × 96 sản phẩm HS07–10.

## Phương pháp (rule a + b)
- **Hàm bậc thang trên TOÀN BỘ bản ghi** (KHÔNG lọc nhãn applicability): MRL tại năm t = bản ghi có `application_date` mới nhất ≤ mốc-năm-t.
- Hai bảng: **jan01** (mốc 1/1 — chính), **dec31** (mốc 31/12 — robustness). Giữ 2015–2024; 2024 gắn cờ `is_robustness_year`.
- Tie-break (b) khi cùng `application_date`: dedup theo `mrl_value` → ưu tiên Annex II > III > V, phụ regulation mới nhất.

## Bước 3 — KIỂM CHỨNG không mất lịch sử (ĐẠT)
Chuỗi MRL jan01 (mg/kg) của vài cặp có MRL ĐỔI trong cửa sổ (None = chưa có bản ghi ≤ năm đó):

```
Fenamidone × Spinaches:    2015–2018 None | 2019–2021 = 60 | 2022–2024 = 0.01   (rớt về LOD)
Fenamidone × Escaroles:    2015–2018 None | 2019–2021 = 40 | 2022–2024 = 0.01
Fenamidone × Celeries:     2015–2018 None | 2019–2021 = 40 | 2022–2024 = 0.01
Boscalid   × Teas:         2015–2021 None | 2022 = 0.01     | 2023–2024 = 40
```
- Bậc thang đổi ĐÚNG năm; **năm trước khi đổi vẫn giữ giá trị cũ** (60/40), KHÔNG bị rỗng → phương pháp toàn-bộ-bản-ghi **không mất lịch sử**. (Nếu lọc trước theo "Applicable", các năm 2019–2021 sẽ mất giá trị 60/40 vì bản đó nay mang nhãn "No longer applicable".)
- Có **10.837 cặp (chất×sp)** đổi MRL trong 2015–2024 — đúng vùng treatment.

## Bước 5 — Khóa duy nhất & thống kê
- In-scope cặp có dữ liệu: **57.809**; cells = 57.809 × 10 năm = **578.090**.
- **Khóa (chất, sản phẩm, năm) DUY NHẤT: trùng = 0** (cả 2 bảng). ✓
- **jan01 (chính):** `ok` 437.067 (**75,6%**) | `not_yet_set` 139.699 (24,2%) | `pending_celex_recovery` 1.324 (0,23%) | `no_mrl_required` 0. → Độ phủ trong các cell ĐÃ có bản ghi (loại not_yet_set) = **99,70%**.
- **dec31 (robustness):** ok 463.981 | not_yet_set 113.018 | pending 1.091.
- **Xung đột giá trị:** 93 ngày (in-scope) có >1 giá trị MRL cùng `application_date` → ảnh hưởng **909 cell** (jan01), **đã xử bằng rule (b)** (Annex II>III>V). Khác biệt là listing across-annex; khóa vẫn duy nhất.

## Hai cờ quan trọng (cần xử ở bước treatment/merge — KHÔNG phải lỗi panel)
1. **`not_yet_set` = 24,2% cell** (139.699): tổ hợp chưa được liệt kê tường minh tại năm đó. Theo Reg 396/2005 Art 18, **MRL mặc định 0,01 mg/kg áp cho tổ hợp không liệt kê** → ở bước dựng treatment cần fill `not_yet_set` = default 0,01 (đây chính là "thắt chặt" nền). Panel để trạng thái tường minh `not_yet_set`, không tự fill.
2. **Worklist null = 420 bản ghi** (KHÔNG phải 40): phương pháp toàn-bộ-bản-ghi lộ thêm **null lịch sử** (regulation cũ ràng buộc năm cũ), ngoài 43 ca "current" (ràng buộc 2023/2024 ≈ ước lượng 40 trước). Phân loại: **current 43** (ưu tiên), historical 377. Đều để cờ `pending_celex_recovery`; **panel KHÔNG bị chặn**. Xem `eu_mrl_null_worklist_2026-06-26.md` + sổ điền tay.

## Output
- `outputs/eu_mrl_binding_panel_reference_jan01_2026-06-26.csv` (chính, 578.090 dòng).
- `outputs/eu_mrl_binding_panel_reference_dec31_2026-06-26.csv` (robustness).
- `eu_mrl_null_worklist_2026-06-26.md` (420 ca) + `manual_entry_ledger_eu_mrl_2026-06-26.md` (trống, chờ điền).
- Cột panel: pesticide_residue_id, product_code, reference, year, binding_application_date, regulation_number, included_in_annex, mrl_value, mrl_value_only, mrl_mg_kg, is_lod, mrl_status, value_conflict.
