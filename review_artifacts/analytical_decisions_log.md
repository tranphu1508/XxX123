# Nhật ký quyết định phân tích (analytical decisions log)

Đây là nhật ký các **quyết định phương pháp / phân tích** của dự án (chốt cách làm, định nghĩa, phạm vi dữ liệu, đặc tả mô hình…). KHÁC với `issues_log.md` — vốn dành cho **lỗi & phát hiện audit**. Mỗi quyết định một mục, append-only, ghi ngày bên trong.

## 2026-06-26 — Cửa sổ mẫu: 2015–2023 (chính) + 2024 (chỉ robustness)
- Quyết định: Mẫu chính (main sample) dùng giai đoạn **2015–2023**. Năm **2024 chỉ dùng làm kiểm định bền (robustness)**; KHÔNG để bất kỳ kết luận chính nào phụ thuộc vào năm 2024.
- Lý do: Trong BACI release **202601**, năm cuối (2024) là **tạm/provisional** — dễ tạo "số 0 giả" và giá trị hụt; 2024 lại giàu cú sốc MRL nhất → rủi ro thổi phồng hiệu ứng rào cản giả tạo.
- Trạng thái: ĐÃ CHỐT

## 2026-06-26 — BACI Giai đoạn 0: chốt release 202601 + HS revision = HS12
- Quyết định: Đóng băng BACI (CEPII) **release 202601**, **HS revision = HS12** (phủ 2012–2024).
- Lý do: HS12 phủ TRỌN 2015–2024; release 202601 hiện hành; bản đã tải sẵn đúng release/revision, kiểm định ĐẠT.
- Trạng thái: ĐÃ CHỐT (release+HS12); CHỜ XÁC NHẬN ràng buộc revision phía concordance EU.

### Cập nhật Bước 6 (2026-06-26, sau xác nhận người dùng)
- 2024 robustness-only + sensitivity cả hai cách (07/08). HS revision concordance EU: "tính sau" (cờ issues_log). Đóng băng: Cowork chép qua cầu nối + verify SHA-256.

## 2026-06-26 — [Apply] EU MRL quy tắc (a): MRL ràng buộc theo HÀM BẬC THANG trên TOÀN BỘ bản ghi
- Quyết định: MRL ràng buộc (chất, sản phẩm) năm t = bản ghi `application_date` mới nhất ≤ **1/1 năm t** từ TOÀN BỘ bản ghi (bậc thang); robustness mốc **31/12**.
- Lý do: KHÔNG lọc trước theo nhãn `applicability` (phản ánh trạng thái NGÀY SNAPSHOT 2026, không phải năm t); lọc nhãn sẽ mất lịch sử ở đúng chất có MRL thay đổi.
- Trạng thái: ĐÃ CHỐT

## 2026-06-26 — [Apply] EU MRL quy tắc (b): phá hòa khi cùng application_date
- Quyết định: dedup `mrl_value` trước; nếu còn >1 → **Annex II>III>V**, phụ regulation mới nhất. 1 dòng/(chất,sp,năm).
- Lý do: 0 xung đột giá trị in-scope → quy tắc vô hại, chỉ để khóa duy nhất.
- Trạng thái: ĐÃ CHỐT

## 2026-06-26 — [Apply] EU MRL quy tắc (c): xử lý 40 null ràng buộc
- Quyết định: khôi phục từ CELEX + ghi sổ điền tay; KHÔNG carry; KHÔNG impute 0,01; cờ `mrl_status=pending_celex_recovery`, không chặn panel.
- Lý do: null là TRỐNG THẬT trong API, giá trị nằm ở văn bản pháp lý.
- Trạng thái: ĐÃ CHỐT

## 2026-06-26 — [Concordance Phase 3] FINALIZE lát VN (VN-first, giữ ASEAN) + one-to-many + RAC
- Quyết định: hoàn thiện concordance EU→HS6 LÁT VN (status finalized_vn, neo loài/heading); residual ASEAN parked_asean. Sửa lỗi phổ quát: Melons 0233010→080719, Wheat 0500090→1001.xx…
- Quy tắc: ONE-TO-MANY giữ tất cả con; RAC (ớt khô/cà phê nhân/chè khô) giữ mẫu chính, KHÔNG processed.
- Trạng thái: ĐÃ CHỐT (lát VN — chờ Claude verify); residual parked.

## 2026-06-26 — [Concordance Phase 3b] GIẢI 2 cờ VN + FINAL lát VN
- Quyết định: GỌI FINAL lát VN (15 mã EU). Giải qua synonyms: ớt cay=0231020, thanh long=0162040, nhãn/longan=0162020; cà phê rang→processed.
- Hệ quả: ⚠ CỜ VÀNG 6 mã VN có MRL snapshot nhưng chưa vào A_k/panel → bước chỉ số phải MỞ RỘNG A_k.
- Trạng thái: ĐÃ CHỐT (FINAL lát VN); A_k extension chờ bước sau.

## 2026-06-26 — [Panel extend + A_k reconcile] Mở rộng panel 7 mã VN; bảng đối chiếu A_k×RASFF; + CHUẨN bằng chứng nguyên văn
- Quyết định: (A) Mở rộng panel ràng buộc cho **7 mã VN** (0231040, 0162020, 0162030, 0162040, 0163060, 0256040, 0256080) bằng đúng hàm bậc thang đã chốt (jan01+dec31, tie Annex II>III>V), tập **A_k 515 chất**. (B) `05_/ak_rasff_reconciliation` (18 chất RASFF T5) = đầu vào quyết định, KHÔNG khóa A_k. (Bước 0) rambutan tách 0162020 → **0163060 'Cherimoyas'** (HS6 081090, nguồn MRL khác).
- Kiểm chứng: builder dựng lại **đối chiếu 50.750 ô vs panel hiện hành → 0 sai khác**; 7 mã đều **489 chất×10 năm** (ngang 9 mã OK); thanh long ĐỦ. Khóa 0 trùng; referential từ snapshot frozen.
- Phát hiện: **acetamiprid MISSING_FROM_A_k** (21 rejection; snapshot chỉ có def REVISED 'Acetamiprid (R)' id=10 record 2025+ → 0 MRL in-window). dinotefuran trong A_k nhưng null. 17/18 T5 ∈ A_k; **498/515 chất A_k không gây rejection VN**.
- Thay đổi Cẩm nang: thêm **CHUẨN THƯỜNG TRỰC — Quy tắc bằng chứng nguyên văn** (đầu Phần 3) + bullet checklist Giai đoạn 0.
- Trạng thái: ĐÃ CHỐT (panel + reconciliation + quy tắc). **A_k membership CHỜ Claude/người dùng quyết** (đặc biệt acetamiprid) trước khi thiết kế chỉ số.
