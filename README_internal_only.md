# README — Repo nhật ký bàn giao nội bộ (CHỈ DÙNG NỘI BỘ)

## Mục đích
Đây là một **git repository ĐỘC LẬP**, tách khỏi repo/dữ liệu của dự án, chỉ chứa **các file nhật ký bàn giao dạng markdown** mà Cowork và Claude dùng để trao đổi tiến độ. Claude đọc trực tiếp các file `.md` này qua raw URL của GitHub.

## Phạm vi — CHỈ .md
- CHỈ đưa file `.md` vào repo này. **Không** đẩy dữ liệu, code, bản thảo, hay bất cứ thứ gì khác của dự án.
- Đây KHÔNG phải repo của cả dự án; nó chỉ là nội dung thư mục `internal_handoff_log_for_claude/`.
- `.gitignore` được cấu hình "bỏ qua tất, chỉ chừa `*.md`" (và tự bỏ qua chính nó) → repo thuần markdown.

## Mô hình public / private
- **Public** trong lúc làm đề tài, để Claude đọc log qua raw URL.
- **Chuyển private** ngay khi đề tài hoàn thành.

## Cấu trúc thư mục
- `README_internal_only.md` — file này (mục đích + quy tắc + mô hình public/private).
- `handoff_index.md` — mục lục sống, mới nhất trên cùng.
- `handoff_log_template.md` — mẫu chuẩn cho mỗi handoff.
- `handoff_YYYY-MM-DD_<ten_task>.md` — các file nhật ký theo từng task.

## QUY TẮC THƯỜNG TRỰC — sau MỖI task hoàn thành, Cowork phải:
1. Viết MỘT file handoff mới `handoff_YYYY-MM-DD_<ten_task_ngan>.md` theo `handoff_log_template.md`.
2. Thêm MỘT dòng vào ĐẦU `handoff_index.md`: `YYYY-MM-DD | <ten_task> | <ten_file> | <1 câu tóm tắt>`.
3. Nếu git khả dụng: `git add -A` rồi `git commit` với thông điệp rõ ràng (commit **local**, không cần mạng).
4. **NHẮC NGƯỜI DÙNG push** thư mục log lên repo public — in nổi bật ở cuối báo cáo task. *Cowork KHÔNG tự push* (không có quyền xác thực).

## Người dùng làm tay (one-time) — Cowork KHÔNG làm bước này
Cowork không tạo repo GitHub và không thể push. Người dùng tự thực hiện:
1. Tạo một repo **public** rỗng trên GitHub (ví dụ tên `eu-mrl-handoff-log`), không thêm sẵn README.
2. Trong thư mục `internal_handoff_log_for_claude/`, đặt remote và push lần đầu:

   ```bash
   git remote add origin https://github.com/<user>/<repo>.git
   git branch -M main
   git push -u origin main
   ```
3. Các lần sau, sau khi Cowork đã commit local, chỉ cần:

   ```bash
   git push
   ```

## Lưu ý bảo mật
- Vì repo **public**, tuyệt đối không ghi thông tin nhạy cảm vào `.md` (khóa API, dữ liệu cá nhân, nội dung bản thảo chưa công bố).
- Chỉ ghi tiến độ / quyết định / cấu trúc để bàn giao; với phát hiện thực chất thì **link** sang `11_audit_findings_and_issues_log/issues_log.md`, không chép lại.

## Lưu ý môi trường (git qua cầu nối sandbox↔Windows)
`git init` chạy trực tiếp trong thư mục này (qua cầu nối) có thể lỗi ghi `.git/config`. Repo hiện tại đã được khởi tạo bằng cách dựng trên ổ local của sandbox rồi sao chép `.git` vào. **Sau khi `.git` đã tồn tại, `git add` / `git commit` chạy bình thường** — nên quy tắc commit-sau-mỗi-task ở trên vẫn áp dụng được. Nếu cần khởi tạo lại từ đầu: đừng `git init` thẳng ở đây — dùng git bản gốc (native) trên Windows, hoặc build `.git` ở nơi khác rồi copy vào.

## review_artifacts/ — bản sao .md cho Claude rà (refresh sau mỗi task)
Thư mục `review_artifacts/` chứa bản sao chỉ-đọc của các file `.md` quan trọng trong dự án (validation reports, `issues_log.md`, `analytical_decisions_log.md`, `data_sources_and_provenance.md`) để Claude đọc qua raw URL. **Sau MỖI task:** nếu bất kỳ file nguồn nào đổi, hoặc có validation report mới → **refresh bản sao tương ứng** trong `review_artifacts/` (và thêm raw URL report mới vào khối "ARTIFACTS ĐỂ RÀ" ở `handoff_index.md`), rồi commit + nhắc push cùng handoff. Mục tiêu: `review_artifacts/` luôn phản ánh bản mới nhất để Claude không đọc nhầm bản cũ. (Copy bằng shell để git thấy đúng nội dung host mới nhất; nếu file nguồn vừa sửa bằng công cụ ghi-host, đọc lại bản host trước khi copy.)
