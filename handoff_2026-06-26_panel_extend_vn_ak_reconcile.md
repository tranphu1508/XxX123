# Handoff — 2026-06-26 — Mở rộng panel MRL lát VN (7 mã) + Bảng đối chiếu A_k×RASFF

## 1. Metadata
- Ngày giờ: 2026-06-26
- Task: PROMPT "Mở rộng panel MRL cho lát VN + bảng đối chiếu A_k (đầu vào quyết định)" (A cơ học + B quyết định + C cẩm nang)
- Trạng thái: HOÀN TẤT — DỪNG chờ Claude/người dùng quyết định nghĩa A_k

## 2. Đã làm gì
- **Bước 0:** Sửa concordance rambutan: tách khỏi 0162020, thêm **0163060 'Cherimoyas'** → HS6 081090 (bằng chứng synonym nguyên văn 'Rambutans/hairy litchis'). Lát VN 16 mã/27 dòng.
- **Phần A (đụng 04_, chỉ đọc 01_):** Mở rộng panel ràng buộc cho **7 mã VN** (0231040, 0162020, 0162030, 0162040, 0163060, 0256040, 0256080) bằng đúng hàm bậc thang đã chốt, tập **A_k 515 chất**. Builder dựng lại được **kiểm chứng 50.750 ô vs panel hiện hành (10 mã) → 0 sai khác**. Kết quả: cả 7 mã = **489 chất × 10 năm** (ngang 9 mã OK); **thanh long ĐỦ phủ**. Khóa (chất,sp,năm,reference) 0 trùng; referential từ snapshot frozen. Output: `04_/outputs/eu_mrl_binding_panel_vn_extended_{jan01,dec31}_2026-06-26.csv`.
- **Phần B (KHÔNG khóa A_k):** `05_/ak_rasff_reconciliation_2026-06-26.csv` (18 chất RASFF T5). **acetamiprid MISSING_FROM_A_k** (21 rejection; snapshot chỉ có def REVISED 'Acetamiprid (R)' id=10, record 2025+ → 0 MRL in-window). dinotefuran trong A_k nhưng null. 17/18 T5 ∈ A_k; **498/515 chất A_k không gây rejection VN**.
- **Phần C:** Thêm **CHUẨN THƯỜNG TRỰC — Quy tắc bằng chứng nguyên văn** vào `Cam_Nang…md` (đầu Phần 3) + bullet checklist Giai đoạn 0 (cả `audit_master_checklist.md`); ghi `analytical_decisions_log`.

## 3. Thay đổi thư mục
- 03_/outputs/concordance_final_vn_2026-06-26.csv (SỬA +0163060; backup .bak_before_rambutan_2026-06-27); vn_product_x_mrl_coverage (cập nhật, +chôm chôm).
- 04_/outputs/eu_mrl_binding_panel_vn_extended_{jan01,dec31}_2026-06-26.csv (MỚI, 7 mã × 515 chất × 10 năm × 2 ref).
- 04_/panel_extend_vn_ak_reconcile_report_2026-06-26.md (MỚI, báo cáo + verbatim).
- 05_/ak_rasff_reconciliation_2026-06-26.csv (MỚI, đầu vào quyết A_k).
- 00_/Cam_Nang…md + audit_master_checklist.md + analytical_decisions_log.md (quy tắc nguyên văn).
- 11_/issues_log.md (rambutan RESOLVED, 6-vàng RESOLVED cơ học, acetamiprid PHÁT HIỆN-CHỜ).
- KHÔNG đụng 01_ frozen.

## 5. Quyết định & chỗ chưa chắc
- Builder panel gốc không lưu script → DỰNG LẠI + kiểm chứng 0 sai trước khi áp (an toàn tái lập).
- A_k membership KHÔNG tự sửa: acetamiprid (CAO) cần Claude quyết thêm vào A_k + khôi phục MRL in-window.

## 6. Cờ cần review
- **acetamiprid MISSING_FROM_A_k** (issues_log CAO) — quyết trước khi thiết kế chỉ số.
- dinotefuran null (pending_celex) — cần CELEX recovery.
- 498 chất A_k không gây rejection VN — ứng viên weight/validation.

## 7. Con trỏ bằng chứng
- 04_/panel_extend_vn_ak_reconcile_report_2026-06-26.md (báo cáo chính, verbatim)
- 05_/ak_rasff_reconciliation_2026-06-26.csv | 04_/outputs/eu_mrl_binding_panel_vn_extended_*.csv
- review_artifacts/ (bản .md để Claude rà)
