# Handoff — 2026-06-26 — EU MRL apply: dựng bảng MRL ràng buộc (chốt a/b/c)

## 1. Metadata
- Ngày: 2026-06-26. Trạng thái: HOÀN TẤT (panel ship được; pending 420 + default-fill chờ bước sau).
- Task: "EU MRL Bước apply — dựng bảng MRL ràng buộc".

## 2. Đã làm gì + SỐ CHÍNH
- Ghi 3 quyết định (a/b/c) vào `analytical_decisions_log.md`.
- Panel **bậc thang trên TOÀN BỘ bản ghi** (KHÔNG lọc applicability), 2 mốc **1/1 (chính)** + **31/12 (robustness)**, 2015–2024.
- In-scope **57.809 cặp × 10 năm = 578.090 cell**; **khóa (chất,sp,năm) DUY NHẤT (trùng=0)**.
- KIỂM CHỨNG Bước 3 ĐẠT: bậc thang đổi đúng năm, **KHÔNG mất lịch sử** (Fenamidone × Spinaches: 2019–2021=60 → 2022+=0.01). 10.837 cặp đổi MRL.
- jan01: ok 437.067 (75,6%) | **not_yet_set 139.699 (24,2%)** | pending 1.324 (0,23%). Độ phủ trong cell có bản ghi = 99,70%. Tie-break (b) xử 909 cell (93 ngày xung đột across-annex).
- **Worklist null = 420** (43 current ≈ 40 cũ, 377 historical) + sổ điền tay trống; cờ `pending_celex_recovery` (không chặn panel).

## 3. Cấu trúc — thay đổi
- THÊM: `04_/outputs/eu_mrl_binding_panel_reference_jan01_2026-06-26.csv` + `_dec31_...csv`; `04_/eu_mrl_apply_report_2026-06-26.md`; `eu_mrl_null_worklist_2026-06-26.md`; `manual_entry_ledger_eu_mrl_2026-06-26.md`.
- SỬA: `00_/analytical_decisions_log.md` (+3 quyết định); `11_/issues_log.md` (+1 mục apply).
- review_artifacts: +apply_report, +worklist, +ledger; refresh analytical_decisions_log + issues_log.

## 4. Agent / sub-agent
- 0.

## 5. Lập luận & quyết định của Cowork
- Rule (a) bậc thang TOÀN BỘ bản ghi (không lọc applicability) — kiểm chứng cho thấy giữ ĐÚNG lịch sử (điểm mấu chốt; nếu lọc applicability sẽ mất giá trị các năm giữa).
- Hai phát hiện: (1) worklist **420 ≠ 40** (lộ null lịch sử); (2) **not_yet_set 24%** → fill default 0,01 (Art 18 Reg 396/2005) ở bước treatment.
- KHÔNG tự fetch EUR-Lex (trả rỗng); để cờ pending + worklist cho người dùng tra tay.

## 6. Cờ cần review
- issues_log: mục apply 2026-06-26 (tie xử xong; null pending 420; default-0.01 fill).
- Bước sau (treatment/merge 04→06): fill `not_yet_set` = default 0,01; tra CELEX 420 ca (ưu tiên 43 current) điền ledger; HS2012 concordance (folder 03) vẫn mở.

## 7. Con trỏ bằng chứng
- `04_/eu_mrl_apply_report_2026-06-26.md`, `eu_mrl_null_worklist_2026-06-26.md`, `manual_entry_ledger_eu_mrl_2026-06-26.md`; `04_/outputs/*.csv`; `00_/analytical_decisions_log.md`; `11_/issues_log.md`.
