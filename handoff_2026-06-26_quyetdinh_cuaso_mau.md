# Handoff — 2026-06-26 — Quyết định cửa sổ mẫu (2015–2023 chính, 2024 robustness)

## 1. Metadata
- Ngày giờ: 2026-06-26 (giờ phiên Cowork)
- Task / prompt tương ứng: "Ghi nhận quyết định: cửa sổ mẫu 2015–2023 (chính) + 2024 (robustness)".
- Trạng thái: HOÀN TẤT.

## 2. Đã làm gì (tóm tắt)
- Mục tiêu task: Ghi nhận (durable + lan tỏa tới nơi có hiệu lực) quyết định đã chốt về cửa sổ mẫu phân tích.
- Kết quả: Đã tạo `00_project_documentation/analytical_decisions_log.md` với mục quyết định đầu tiên; cập nhật provenance (dòng BACI), pointer trong overview, 3 README downstream (04/07/08), và đánh dấu mục "2024 provisional — ĐÃ GIẢI QUYẾT" trong `audit_master_checklist.md` (Giai đoạn 0).

## 3. Cấu trúc thư mục sau cập nhật
- Cấu trúc thư mục KHÔNG đổi so với handoff trước (xem `handoff_2026-06-26_thiet_lap_repo_log.md`); chỉ thay đổi NỘI DUNG file.
- Thay đổi so với handoff trước (file):
  - THÊM: `00_project_documentation/analytical_decisions_log.md`
  - SỬA: `00_project_documentation/data_sources_and_provenance.md` (thêm dòng BACI + ghi chú cửa sổ mẫu)
  - SỬA: `00_project_documentation/readme_project_overview.md` (mục "Quyết định phương pháp" trỏ tới log)
  - SỬA: `00_project_documentation/audit_master_checklist.md` (Giai đoạn 0: thêm mục `- [x]` 2024 provisional ĐÃ GIẢI QUYẾT)
  - SỬA: `04_maximum_residue_level_panel/readme_04_...md`, `07_main_estimation_stata/readme_07_...md`, `08_robustness_checks/readme_08_...md` (mỗi file thêm dòng quyết định cửa sổ mẫu)

## 4. Agent / sub-agent
- Số agent đã gọi: 0.
- Với từng agent: không có — Cowork làm trực tiếp.

## 5. Lập luận & quyết định của Cowork
- Kế hoạch đã chọn: ghi quyết định vào một nhật ký riêng (`analytical_decisions_log.md`, tách khỏi `issues_log.md`), rồi lan tỏa một dòng pointer tới các nơi có hiệu lực (provenance, README downstream 04/07/08, checklist Giai đoạn 0, overview).
- Quyết định / giả định:
  - Tách `analytical_decisions_log.md` (quyết định phương pháp) khỏi `issues_log.md` (lỗi & audit) đúng theo prompt.
  - Dòng BACI trong provenance: điền `release 202601` + ghi chú; các ô ngày/URL/checksum để "(điền khi tải)" vì dữ liệu CHƯA đóng băng (sẽ điền ở task BACI Giai đoạn 0).
  - `audit_master_checklist.md` Giai đoạn 0 chưa có sẵn ô "2024 provisional" → THÊM một mục `- [x]` (đã giải quyết) trỏ tới log, thay vì sửa ô có sẵn.
- Chỗ lệch khỏi prompt (và lý do): không có lệch thực chất. (Ghi nhận provenance sớm dù dữ liệu chưa tải — để quyết định có "địa chỉ" trước khi chạy BACI.)
- Chỗ chưa chắc / cần xác minh: ngày snapshot/URL/checksum BACI sẽ điền khi thực sự tải & đóng băng (task Giai đoạn 0).

## 6. Cờ cần review
- Việc cần Claude/người dùng xem: khi chạy task BACI (Giai đoạn 0), áp dụng quyết định — TẢI & ĐÓNG BĂNG đủ cả 2024 nhưng gắn cờ provisional/robustness; mẫu chính chỉ 2015–2023.
- Đây là QUYẾT ĐỊNH phương pháp (ghi ở `analytical_decisions_log.md`), KHÔNG phải lỗi audit → không ghi vào `issues_log.md`.

## 7. Con trỏ bằng chứng
- Quyết định: `00_project_documentation/analytical_decisions_log.md` (mục 2026-06-26).
- Lan tỏa: `data_sources_and_provenance.md`, `readme_project_overview.md`, `audit_master_checklist.md`, và README của `04_`, `07_`, `08_`.
