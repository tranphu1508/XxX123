# Handoff — 2026-06-26 — Đóng băng Annex I pháp lý + đối chiếu 15 mã VN (ground truth)

## 1. Metadata
- Ngày: 2026-06-26 (đóng băng file 2026-06-27)
- Task: Đóng băng Annex I pháp lý (Reg (EU) 2018/62) + đối chiếu 15+ mã VN làm ground truth
- Trạng thái: HOÀN TẤT — DỪNG chờ Claude đọc đối chiếu

## 2. Đã làm gì
- **Bước 1:** Đóng băng `L_2018018EN.01000101.xml.html` (người dùng cung cấp) → `01_raw_data_frozen/eu_annex1_legal/`, read-only, SHA-256 `c4cb8987…de578f`; provenance ghi CELEX 32018R0062.
- **Bước 2:** Parse XHTML → `annex1_species_to_code.csv` (**381 nhóm + 924 sub-entry**, mọi mã, dùng lại ASEAN).
- **Bước 3:** Đối chiếu **17 mã VN lá** với Annex I pháp lý (dán dòng nguyên văn). **17/17 KHỚP, 0 lệch nghiêm trọng.** Báo cáo `03_/annex1_groundtruth_crosscheck_2026-06-26.md`.
- **Bước 4:** Thêm cột `annex1_legal_ref` vào `concordance_final_vn` (27 dòng) → concordance có nguồn pháp lý.

## 3. Xác nhận 4 điểm prompt
- Thanh long → `0162040-001 Pitayas/dragon fruits | Hylocereus undatus` ✅
- Rambutan → `0163060-006 Rambutans/hairy litchis | Nephelium lappaceum` ✅ (XÁC NHẬN tách 0162020, Bước 0 trước đúng)
- Longan → `0162020-001 Longans | Dimocarpus longan` ✅
- Ớt cay → `0231020-001 Chili peppers` (Capsicum spp.) ✅

## 4. Lệch nhỏ (không phải lỗi concordance)
- Bưởi VN = pomelo = sub `0110010-002 Shaddocks/pomelos` (Citrus maxima), không phải grapefruit thật. HS6 080540 vẫn đúng → giữ, ghi chú.
- Herbs: concordance dùng nhóm 0256000; Annex I tách parsley 0256040 + basil 0256080 (gồm Vietnamese mint, Thai basil, rice paddy herb, dap ca). annex1_legal_ref ghi cả nhóm + lá.

## 5. Thay đổi thư mục
- 01_/eu_annex1_legal/ (file đóng băng + annex1_species_to_code.csv) — MỚI.
- 03_/concordance_final_vn (+cột annex1_legal_ref; backup .bak_before_annex1ref_2026-06-27).
- 03_/annex1_groundtruth_crosscheck_2026-06-26.md — MỚI.
- 00_/data_sources_and_provenance.md (+dòng Annex I pháp lý).

## 6. Cờ cần review
- Claude đọc bảng 17 mã (đặc biệt pomelo=sub-002, herbs leaf). Không lệch nghiêm trọng → không cần sửa mã quan trọng.

## 7. Con trỏ bằng chứng
- 03_/annex1_groundtruth_crosscheck_2026-06-26.md (báo cáo, verbatim 17 mã)
- 01_/eu_annex1_legal/annex1_species_to_code.csv | concordance_final_vn (cột annex1_legal_ref)
