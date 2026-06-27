# Handoff — 2026-06-26 — Rổ trọng số ω từ thông tư MARD (Danh mục thuốc BVTV)

## 1. Metadata
- Ngày: 2026-06-26 | Task: parse thông tư MARD → rổ ω | Trạng thái: HOÀN TẤT — DỪNG (chưa cắm ω vào chỉ số)

## 2. Đã làm
- **Thông tư lấy được:** ĐỦ — bản parse kiểm-chứng-số-lượng sẵn (MASTER_pesticide_crop, 14 thông tư). ω chính = **03/2016** (Nguyen "MARD 2016"); alt = 03/2015; robustness = 09/2023. Đóng băng 01_/vn_mard_circulars/ (MASTER SHA-256 7361eb9f…) + source PDF/doc.
- **Granularity = CROP-LEVEL (theo cây)** ✅ lý tưởng (hoạt chất × cây). Intensity = #tên-thương-phẩm. GAP: 6/17 mã (bưởi, chanh, đậu bắp, chanh leo, parsley, basil) không có ω crop-level cho chất RASFF → national fallback.
- **Map RASFF-18 → Danh mục (nguyên văn): 16/18 thấy**; loại false-positive (permethrin⊄cypermethrin, chlorpyrifos⊄methyl); dithiocarbamates = 5 component.
- **banned_but_rejected: carbofuran (15 vụ), methamidophos (10 vụ)** — KHÔNG trong DM, ω=0, vẫn chặn hàng EU.

## 3. Phát hiện then chốt
- carbofuran + methamidophos: ω=0 mọi kỳ (cấm) nhưng 25 vụ RASFF → điểm mù ω + bằng chứng đăng-ký lệch sử-dụng-thực.
- carbendazim/chlorpyrifos/acephate/fipronil: đăng ký 2016 nhưng LOẠI ở 2023 → bản 2023 nội sinh; ω-2016 (tiền-định) là đúng.

## 4. Output
- 05_/omega_vn_registration_basket.csv (918 dòng = 18 chất × 17 mã × 3 kỳ; binary + intensity + share + banned flag).
- 05_/omega_vn_national_fallback.csv (54 dòng; ω quốc-gia cho 6 mã gap + robustness).
- 05_/mard_registration_omega_2026-06-26.md (báo cáo).

## 5. Cờ review (DỪNG chờ)
- (a) Xác nhận granularity ω = crop-level (gap 6 mã → fallback).
- (b) Quyết xử banned_but_rejected (biến phụ không-trọng-số hay ω tối thiểu) TRƯỚC khi cắm ω.
- Chưa cắm ω vào chỉ số, chưa chạy hồi quy.
