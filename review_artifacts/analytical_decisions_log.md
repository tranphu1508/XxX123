> Bản sao chỉ-đọc của eu_maximum_residue_level_asean_export_study/00_project_documentation/analytical_decisions_log.md, cập nhật 2026-06-26.

# Nhật ký quyết định phân tích (analytical decisions log)

Đây là nhật ký các **quyết định phương pháp / phân tích** của dự án (chốt cách làm, định nghĩa, phạm vi dữ liệu, đặc tả mô hình…). KHÁC với `issues_log.md` — vốn dành cho **lỗi & phát hiện audit**. Mỗi quyết định một mục, append-only, ghi ngày bên trong.

## 2026-06-26 — Cửa sổ mẫu: 2015–2023 (chính) + 2024 (chỉ robustness)
- Quyết định: Mẫu chính (main sample) dùng giai đoạn **2015–2023**. Năm **2024 chỉ dùng làm kiểm định bền (robustness)**; KHÔNG để bất kỳ kết luận chính nào phụ thuộc vào năm 2024.
- Lý do: Trong BACI release **202601**, năm cuối (2024) là **tạm/provisional** — CEPII tải nguồn COMTRADE vào tháng 1/2026 nên nhiều dòng năm 2024 chưa đầy đủ hoặc chỉ một chiều báo cáo, dễ tạo "số 0 giả" (false zeros) và giá trị hụt. Mà 2024 lại là năm **giàu cú sốc MRL nhất** → rủi ro nhầm "dữ liệu chưa về" thành "xuất khẩu giảm sau khi MRL siết", tức thổi phồng hiệu ứng rào cản một cách giả tạo. Trong bản 202601, năm 2023 đã được sửa ít nhất một lần nên ổn định hơn.
- Hệ quả (ảnh hưởng bước/thư mục nào):
  - `01_raw_data_frozen/` — vẫn TẢI và ĐÓNG BĂNG đủ cả 2024 (không bỏ dữ liệu), chỉ gắn cờ provisional/robustness, không đưa vào mẫu chính.
  - `04_maximum_residue_level_panel/` — dựng panel theo cửa sổ 2015–2023; 2024 tách riêng, gắn cờ.
  - `07_main_estimation_stata/` — ước lượng chính chạy trên 2015–2023.
  - `08_robustness_checks/` — 2024 là một mục robustness riêng.
  - `00_project_documentation/` — đã cập nhật `data_sources_and_provenance.md` (dòng BACI) và `audit_master_checklist.md` (Giai đoạn 0) theo quyết định này.
- Trạng thái: ĐÃ CHỐT

## 2026-06-26 — BACI Giai đoạn 0: chốt release 202601 + HS revision = HS12
- Quyết định: Đóng băng dữ liệu thương mại từ BACI (CEPII) **release 202601**, **HS revision = HS12** (phủ 2012–2024).
- Lý do: HS12 phủ TRỌN cửa sổ 2015–2024 (HS17 chỉ từ 2017, mất 2015–2016); release 202601 là bản hiện hành (cập nhật 2026-01-22); bản đã tải sẵn trên máy (Version 1/Version 2) đúng release/revision này và đã qua kiểm định 3 nhóm (ĐẠT).
- Hệ quả: 01 (đóng băng zip HS12 V202601 + CSV); 02 (script tải tái lập + báo cáo kiểm định `baci_validation_2026-06-26.md`); 03 concordance phải dùng HS6 theo **revision HS2012** để khớp BACI.
- Chỗ chưa chắc / cần người dùng xác nhận (Bước 6): folder 03 (concordance product_code→HS6) chưa dựng trong khung mới; cần bảo đảm concordance phía EU dùng HS6 revision 2012 để khớp BACI HS12. Nếu phía EU dùng HS2017/HS2022 → phải bắc cầu revision. CHƯA phát hiện mâu thuẫn (chỉ HS12 hiện diện) nên đi tiếp + gắn cờ.
- Trạng thái: ĐÃ CHỐT (release + HS12); CHỜ XÁC NHẬN ràng buộc revision phía concordance EU.

### Cập nhật Bước 6 (2026-06-26, sau xác nhận người dùng)
- Năm 2024: GIỮ robustness-only (mẫu chính 2015–2023) VÀ chạy thêm **sensitivity cả hai cách** (có/không 2024) ở bước ước lượng (07/08) để bổ sung thông tin. (Trước đây chỉ robustness-only.)
- HS revision concordance EU: người dùng chọn **"tính sau"** → giữ cờ trong `11_/issues_log.md` (TRUNG BÌNH), quyết khi dựng folder 03.
- Đóng băng: người dùng chọn **Cowork chép qua cầu nối** → copy zip canonical (1.27 GB) vào `01_/trade_data_baci/` + verify SHA-256 khớp manifest.
