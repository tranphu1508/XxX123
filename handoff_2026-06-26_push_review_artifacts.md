# Handoff — 2026-06-26 — Đẩy review_artifacts (.md) cho Claude rà

## 1. Metadata
- Ngày: 2026-06-26
- Task: "Đẩy các file .md cần cho Claude rà vào repo log".
- Trạng thái: HOÀN TẤT.

## 2. Đã làm gì
- Tạo `review_artifacts/` (+ `validation_reports/`) trong repo log + `README_review_artifacts.md`.
- COPY 5 file .md (chỉ .md; chèn header bản-sao + đường dẫn canonical + ngày) từ dự án:
  1. analytical_decisions_log.md
  2. data_sources_and_provenance.md
  3. issues_log.md
  4. validation_reports/baci_validation_2026-06-26.md
  5. validation_reports/eu_mrl_validation_2026-06-26.md
- Thêm khối "ARTIFACTS ĐỂ RÀ" (raw URL từng file) vào `handoff_index.md`.
- Thêm quy tắc thường trực refresh vào `README_internal_only.md`.

## 3. Cấu trúc — thay đổi
- THÊM: `review_artifacts/` (6 file .md). SỬA: `handoff_index.md`, `README_internal_only.md`.
- KHÔNG đổi gì trong dự án (chỉ đọc để copy).

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Copy bằng shell; phát hiện 2 file nguồn (analytical_decisions_log, data_sources_and_provenance) lệch host↔cầu nối (vừa sửa bằng công cụ ghi-host) → ĐỌC bản host (chuẩn) rồi ghi lại bản sao để đúng nội dung mới nhất. Đã verify marker bản mới.
- Chỉ .md; KHÔNG đẩy dữ liệu/script/file lớn (giữ quy tắc repo log).

## 6. Cờ cần review
- Repo public → 5 file world-readable (artifact kiểm định/quyết định — rủi ro thấp). Kết quả ước lượng nhạy sau này: chỉ đẩy tóm tắt, không nguyên số.

## 7. Con trỏ bằng chứng
- `review_artifacts/` + khối "ARTIFACTS ĐỂ RÀ" trong `handoff_index.md`.
