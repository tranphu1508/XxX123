# Handoff — 2026-06-26 — RASFF VN density CONFIRMED (ĐỦ-gộp) — đã DỪNG

## 1. Metadata
- Ngày: 2026-06-26. Trạng thái: ĐÃ CÓ SỐ ĐẾM THỰC; **ĐÃ DỪNG** chờ Claude xác nhận trước khi thiết kế panel.
- Task: "Dọn file RASFF + ghi nhận kết quả đếm (đã xác nhận ĐỦ-gộp)".

## 2. Đã làm gì + SỐ CHÍNH
- Dọn 2 file (pre-2021 EU Open Data ≤2020 + RASFF Window ≥2021) vào `raw/` + `SOURCES.md`.
- **Reproduce KHỚP: TỔNG 328 / border 180**; theo năm khớp từng năm. Top sản phẩm: ớt/tiêu 100, thanh long 61, cà phê/chè 32, trái cây khác 33, gạo 15, sầu riêng 9, đậu bắp 6 (+ other 57). Top hoạt chất: **carbendazim #1**.
- **Verdict: BIÊN GIỚI → ĐỦ (gộp).** RASFF = **trụ định lượng bổ trợ** (1 bảng đếm gộp: product FE + year FE + offset enhanced-control); KHÔNG đủ product×year chi tiết (chỉ 1 ô ≥20).
- **2 phát hiện thiết kế:** (a) carbendazim dẫn đầu (≠ 'bộ 5 Nguyen') → neo A_k/chỉ số MRL theo hoạt chất VN thực tế; (b) nội sinh kiểm tra hiện rõ (ớt 2024, sầu riêng 2023→24 vọt trùng enhanced-control) → offset bắt buộc.
- **Lệch trung thực:** số đếm hoạt chất của tôi cao hơn (window liệt nhiều chất/notification; carbendazim vẫn #1); 'other' 57 vs Claude 81 (gom thêm vào trái-cây/rau-thơm) — **TỔNG không đổi**.

## 3. Cấu trúc — thay đổi
- THÊM: `02_/rasff_feasibility_scan/raw/` (2 xlsx + SOURCES); `outputs/` (T1–T5 + _SUMMARY + all_records); `scripts/parse_rasff_vietnam.py` (cập nhật). KHÔNG đụng 01_ (không đóng băng).
- SỬA: `rasff_vietnam_density_scan_2026-06-26.md` (ĐÃ CÓ SỐ, verdict ĐỦ-gộp); `11_/issues_log.md` (+phát hiện).
- review_artifacts: refresh report + issues_log; +T4 +T5.

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Reproduce mức DÒNG/finding cho pre-2021 (khớp Claude) + mức notification cho window — ra đúng 328/180.
- Verdict ĐỦ-gộp dựa SỐ THỰC (không phải literature như bản scan trước).
- DỪNG — chưa đóng băng, chưa dựng panel (chờ Claude xác nhận).

## 6. Cờ cần review
- issues_log: carbendazim (neo A_k VN) + nội sinh kiểm tra (offset enhanced-control).
- Bước sau (sau khi Claude OK): map sản phẩm→HS4 (+ %UNMAPPED); lấy cờ enhanced-control product-year; thiết kế bảng đếm gộp.

## 7. Con trỏ bằng chứng
- `02_/rasff_feasibility_scan/` (report + outputs T1–T5 + all_records + raw + scripts/parse_rasff_vietnam.py); `11_/issues_log.md`.
