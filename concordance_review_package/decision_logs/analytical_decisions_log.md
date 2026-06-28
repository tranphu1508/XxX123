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

## 2026-06-26 — [Apply] EU MRL quy tắc (a): MRL ràng buộc theo HÀM BẬC THANG trên TOÀN BỘ bản ghi
- Quyết định: MRL ràng buộc của (chất, sản phẩm) tại năm t = bản ghi có `application_date` mới nhất ≤ **1/1 năm t**, dựng từ **TOÀN BỘ bản ghi** sắp theo application_date (hàm bậc thang). Biến thể robustness: mốc **31/12 năm t**.
- Lý do: **KHÔNG lọc trước theo nhãn `applicability`** ("Applicable"/"No longer applicable") — nhãn phản ánh trạng thái tại NGÀY SNAPSHOT 2026, không phải tại năm t. Bản "No longer applicable" hôm nay có thể chính là MRL ràng buộc của các năm trước khi bị thay; lọc theo nhãn sẽ **mất lịch sử ở đúng các chất có MRL thay đổi** (chính là treatment).
- Hệ quả: 04 dựng panel theo bậc thang; mốc 1/1 = bản chính, 31/12 = robustness; giữ 2015–2024, 2024 gắn cờ robustness.
- Trạng thái: ĐÃ CHỐT

## 2026-06-26 — [Apply] EU MRL quy tắc (b): phá hòa khi cùng application_date
- Quyết định: dedup theo `mrl_value` trước (bỏ trùng y hệt); nếu còn >1 → ưu tiên **Annex II > III > V**, phụ: regulation mới nhất. Lấy 1 dòng/(chất,sp,năm).
- Lý do: chẩn đoán cho thấy **0 xung đột giá trị** in-scope → quy tắc vô hại, chỉ để khóa duy nhất xác định.
- Hệ quả: khóa (chất, sản phẩm, năm) duy nhất.
- Trạng thái: ĐÃ CHỐT

## 2026-06-26 — [Apply] EU MRL quy tắc (c): xử lý 40 null ràng buộc
- Quyết định: khôi phục giá trị thật từ **CELEX + ghi sổ điền tay**; **KHÔNG carry** giá trị từ ngày khác (null đến từ regulation mới → có thể là thay đổi thật); **KHÔNG impute 0,01**; drop+cờ chỉ khi không khôi phục được. Trong panel: cờ `mrl_status = pending_celex_recovery`, KHÔNG chặn panel.
- Lý do: null là **TRỐNG THẬT** trong API (record thô xác nhận mọi trường value null), giá trị nằm ở văn bản pháp lý.
- Hệ quả: worklist 40 ca + `manual_entry_ledger`; panel ship với cờ pending.
- Trạng thái: ĐÃ CHỐT

## 2026-06-26 — [Concordance Phase 3] FINALIZE lát VN (VN-first, giữ ASEAN) + one-to-many + RAC
- Quyết định: Hoàn thiện concordance EU→HS6 cho **LÁT VN** (14 mã EU, 25 dòng eu×hs6 con, `status=finalized_vn`, có trích dẫn neo loài/heading); residual ASEAN gắn `parked_asean` (KHÔNG xóa/ép/gọi verified). Sửa lỗi phổ quát cả 2 nhánh: **Melons 0233010→080719**, Watermelons 0233030→080711; **Wheat 0500090→toàn bộ 1001.xx**, Barley 0500010→100310+100390.
- Lý do: VN-first nhưng **CỘNG-THÊM**, không phá pipeline ASEAN. Fork: shared fixes (melons/ngũ cốc) lợi cả hai; VN verify từng dòng; ASEAN park.
- Quy tắc: (1) **ONE-TO-MANY** — nhóm/heading nhiều con thương phẩm → GIỮ TẤT CẢ con (gạo 4 con, wheat 4, citrus theo loài). (2) **RAC** — map sang dạng MRL áp: ớt KHÔ (0904), cà phê NHÂN (0901), chè khô (0902) là RAC → GIỮ mẫu chính, KHÔNG `processed`; chỉ `processed` cho đông/đóng hộp/chế biến sâu (0710-0712, 0811-0813).
- Hệ quả: 03_ `concordance_final_vn` + `concordance_full_with_parked`; cờ HS-revision **ĐÓNG cho lát VN** (referential 0; neo HS2012+loài+heading). 2 cờ VN còn mở: thanh long + longan/rambutan KHÔNG có mã EU riêng → Others/081090, cần xác nhận mã.
- Trạng thái: ĐÃ CHỐT (lát VN — chờ Claude verify 14 sản phẩm trước khi gọi 'final'); residual parked.

## 2026-06-26 — [Concordance Phase 3b] GIẢI 2 cờ VN + FINAL lát VN
- Quyết định: **GỌI FINAL lát VN** (15 mã EU, 26 dòng). Giải 2 cờ qua trường **synonyms** catalogue: ớt cay = **0231020** (chung ớt ngọt; synonym "Chili peppers"; MRL Capsicum dùng chung); thanh long = **0162040** "cactus fruits" (synonym "Pitayas/dragon fruits"; MRL từ 0162040, KHÔNG phải "Others"); nhãn/longan = **0162020** (synonym "Longans"). Cà phê rang 090121/090122 → **processed** (nhân xanh 090111/090112 = RAC mẫu chính).
- Lý do: MRL-coverage (đọc 04_): ớt cay #1 đầy đủ trong panel (489 chất×10 năm); thanh long #2 có MRL trong snapshot (691 chất). **KHÔNG có cờ ĐỎ** → đủ điều kiện final.
- Hệ quả: `concordance_final_vn` cập nhật; cờ HS-revision ĐÓNG cho lát VN. ⚠ **CỜ VÀNG:** 6 mã VN (thanh long, vải/nhãn, chanh leo, đậu bắp, parsley/basil) có MRL snapshot nhưng CHƯA vào A_k/panel → bước thiết kế chỉ số phải MỞ RỘNG A_k (đã ghi issues_log).
- Trạng thái: ĐÃ CHỐT (FINAL lát VN concordance); A_k extension chờ bước sau.

## 2026-06-26 — [Panel extend + A_k reconcile] Mở rộng panel 7 mã VN; bảng đối chiếu A_k×RASFF; + CHUẨN bằng chứng nguyên văn
- Quyết định: (A) Mở rộng panel MRL ràng buộc cho **7 mã VN** (0231040, 0162020, 0162030, 0162040, 0163060, 0256040, 0256080) bằng **đúng** hàm bậc thang đã chốt (jan01 + dec31, tie Annex II>III>V, not_yet_set, pending_celex), tập **A_k 515 chất**. (B) Dựng `05_/ak_rasff_reconciliation_2026-06-26.csv` (18 chất RASFF T5) làm **đầu vào quyết định**, KHÔNG khóa A_k. (Bước 0) Sửa concordance: rambutan tách khỏi 0162020 → **0163060 'Cherimoyas'** (HS6 081090 giữ nguyên, nguồn MRL khác).
- Kiểm chứng: builder panel dựng lại được **đối chiếu 50.750 ô** với panel hiện hành (10 mã in-panel) → **0 sai khác** trước khi áp cho 7 mã mới. 7 mã mới đều đạt **489 chất × 10 năm** = ngang 9 mã OK; thanh long ĐỦ phủ. Khóa (chất,sp,năm,reference) 0 trùng; referential từ snapshot frozen.
- Phát hiện (cho bước A_k membership): **acetamiprid MISSING_FROM_A_k** (21 rejection, không trong A_k; snapshot chỉ có định nghĩa REVISED 'Acetamiprid (R)' id=10 với record 2025+ → 0 MRL in-window 2015–2024). **dinotefuran** trong A_k nhưng MRL null (pending_celex). 17/18 chất T5 trong A_k; **498/515 chất A_k không gây rejection VN nào**.
- Thay đổi Cẩm nang: thêm **CHUẨN THƯỜNG TRỰC — Quy tắc bằng chứng nguyên văn** vào đầu Phần 3 `Cam_Nang…md` + 1 bullet checklist Giai đoạn 0 (cả `audit_master_checklist.md`). Lý do: lỗi rambutan & acetamiprid chỉ lộ qua dòng nguyên văn, không qua tóm tắt.
- Hệ quả: 03_ concordance_final_vn (16 mã/27 dòng, +0163060); 04_ panel mở rộng (2 CSV jan01/dec31, +7 mã); 05_ reconciliation CSV (đầu vào quyết A_k). KHÔNG sửa 01_ frozen; KHÔNG dựng chỉ số.
- Trạng thái: ĐÃ CHỐT (panel mở rộng + reconciliation + quy tắc nguyên văn). **A_k membership: CHỜ Claude/người dùng quyết** dựa bảng đối chiếu (đặc biệt acetamiprid) TRƯỚC khi thiết kế chỉ số.
