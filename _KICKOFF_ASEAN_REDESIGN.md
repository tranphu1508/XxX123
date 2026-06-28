# 🚀 KICKOFF — Làm lại bài ASEAN (Cowork làm chính) — chốt 2026-06-29

> **Cho chat Cowork MỚI:** đọc cổng `_DOC_TRUOC_TIEN.md` (00–05 + handoff_index) TRƯỚC, rồi đọc file này để biết việc cần làm. Chat cũ đã quá dài → khởi động sạch ở chat mới.

## Quyết định khung (user chốt 2026-06-29)
- **Cowork là công cụ CHÍNH** (bỏ tầng Claude-web trung gian). Lý do: Cowork đọc dữ liệu thật theo yêu cầu → không bị "mù/skip project knowledge" như web. Tự kiểm bằng subagent + reproduce chéo + bằng chứng nguyên văn.
- **Phạm vi:** *thiết kế lại phân tích*, **GIỮ data đã audit** (KHÔNG dựng lại pipeline từ raw).
- Bài ASEAN: gravity **biến-liên-tục**, khung **"tương quan có điều kiện, KHÔNG nhân quả"**, tạp chí **ITJ (Q3)**. (Event-study chỉ phụ lục — pre-trends đã gãy.) Chi tiết: `context_knowledge/01_DE_TAI_ASEAN.md`.

## Tài sản TÁI DÙNG (đã audit + reproduce khớp — xem `12_audit/`)
| asset | path | trạng thái |
|---|---|---|
| Concordance ASEAN (pháp-lý-hóa Annex I) | `03_.../outputs/concordance_final_asean.csv` | 304 mã plant, annex1_legal_ref 100% |
| Panel MRL stringency | `04_.../outputs/asean_mrl_panel.csv` | 137 HS6×năm, weakest-link, cờ lump_divergent |
| Panel BACI đa phương | `07_.../asean_baci_panel.csv` | 292.500 = ASEAN-5×125 HS6×52 đích×2015–23 |
| Raw đóng băng | `01_raw_data_frozen/` | BACI zip, MRL snapshot, Annex I legal, MARD MASTER (checksum) |
| Inventory + reproduce audit | `12_audit/` | inventory sạch; DuckDB↔pyfixest khớp |

## VIỆC #1 (làm TRƯỚC khi re-design) — giải nghi vấn β panel cũ↔mới
Đã chạy M1 trên panel MỚI (handoff `2026-06-29_asean_beta_oldnew`):
- β_cũ (Đợt1, panel 185 HS6) = **−2,077\*\*\***
- β_mới: S1 = −1,47\*\*\* · **S2 (3-chiều, chính) = +0,15 ĐỔI DẤU** · S3 = −0,88\*\*\* → **STOP-RULE: β KHÔNG ổn định.**

**Diagnostic cần chạy (tách nguyên nhân):**
1. Đối chiếu ĐỊNH NGHĨA cột/treatment 2 panel: panel cũ `regression_panel_FINAL.csv` (`Version 2/Model Run/`) vs mới. Treatment 2 bên có cùng cách dựng (EU_MRL × eu_dummy, cùng đo độ-ngặt) không? Cùng level XK không? 10 năm vs 9, 42 đích vs 52.
2. **Same-sample:** chạy lại panel CŨ **giới hạn 126 HS6 sạch** (mã pháp-lý) → nếu β cũ cũng → ~0 thì chính ~59 mã loại lái kết quả −2,077; nếu vẫn −2 thì khác biệt do CÁCH DỰNG panel (đích/năm/treatment).
3. Báo bảng + **chốt dùng panel nào** cho bài (pháp-lý-sạch vs phủ-rộng-cũ), có biện minh.

## Lộ trình sau khi chốt panel (re-design)
1. Chốt đặc tả chính (S2 3-chiều PPML) + tập robustness (S1/S3 + cửa sổ + cluster).
2. Bảng kết quả M1 (market access) + các M khác nếu khung bài cần (H2/H3).
3. Robustness + shift-share exposure (gia cố cross-nước, không cần ω-theo-nước — ASEAN bất khả ω).
4. Soạn manuscript ASEAN (ITJ) — framing tương quan có điều kiện.

## Kỷ luật vận hành (giữ nguyên)
- Mỗi "đợt" → viết handoff (`handoff_<ngày>_<task>.md`) + prepend `handoff_index.md` + commit; **user push tay** + mở index `?v=N` mới.
- Bằng chứng nguyên văn cho mọi quyết-định-tra-cứu. STOP-RULE: gãy pre-trends / đổi dấu β → DỪNG, báo thẳng, chờ user.
- Stata không có trong Cowork → engine PPML = pyfixest/ppmlhdfe-equivalent; .do cung cấp cho user chạy bản trọng tài.
