# Handoff — 2026-06-26 — RASFF VN density scan (kiểm tra khả thi) — đã DỪNG

## 1. Metadata
- Ngày: 2026-06-26. Trạng thái: BÁN PHẦN (Path A blocked); ĐÃ DỪNG chờ Route B + quyết hướng.
- Task: "Quét mật độ RASFF VN — đủ dày cho Poisson/PPML không?".

## 2. Đã làm gì + SỐ CHÍNH
- **Path A (lập trình) BỊ CHẶN:** EU Open Data .xlsx (proxy 403 / web_fetch trả binary), RASFF Window SPA POST-session, không có Chrome — nhất quán lần quét trước (thư mục cũ) + giới hạn web phiên này. **KHÔNG có raw data.**
- **Path B:** hướng dẫn export tay (`ROUTE_B_export_instructions.md`) + script parse sẵn (`scripts/parse_rasff_vietnam.py`) → 6 bảng đếm khi có file.
- **VERDICT SƠ BỘ: BIÊN GIỚI.** VN hạng trung pesticide-RASFF (top India/Turkey/China); tập trung số ít sản phẩm nóng (ớt/đậu bắp/thanh long/rau thơm; mới: sầu riêng/chanh leo/gạo); border ~½. → đủ cho mô hình đếm **GỘP có kiểm soát**, KHÔNG đủ trụ độc lập chi tiết; border-only quá thưa.
- **Khuyến nghị:** RASFF = biến đếm **thứ cấp/bổ trợ** trên nhóm nóng (+ cờ enhanced-control) + minh hoạ định tính.

## 3. Cấu trúc — thay đổi
- THÊM: `02_/rasff_feasibility_scan/` (scan report + ROUTE_B_export_instructions + `scripts/parse_rasff_vietnam.py` + raw/ + outputs/ trống). KHÔNG đụng 01_ (không đóng băng).
- review_artifacts: +scan report.

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Lần quét trước (thư mục gốc cũ `Dữ liệu pháp lý ASEAN`) đã test Path A rất kỹ + viết script/hướng dẫn → tái dùng, đặt deliverable ở vị trí mới; xác nhận block độc lập phiên này (EUR-Lex rỗng, FAO timeout, no Chrome).
- Verdict SƠ BỘ (literature) — chốt khi có Route B export.
- DỪNG — không đóng băng, không dựng phân tích.

## 6. Cờ cần review
- Caveat **nội sinh cường-độ-kiểm-tra** (enhanced-control Reg 2019/1793) — bắt buộc kiểm soát/offset nếu dùng RASFF làm biến đếm.
- Lệch HS4-vs-HS6; đa-hazard; đứt gãy độ phủ 2020. Chốt verdict cần Route B.

## 7. Con trỏ bằng chứng
- `02_/rasff_feasibility_scan/rasff_vietnam_density_scan_2026-06-26.md` + `ROUTE_B_export_instructions.md` + `scripts/parse_rasff_vietnam.py`.
