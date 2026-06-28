# Handoff — 2026-06-29 — Audit HS-revision EU↔BACI + tính đúng concordance

## 1. Metadata
- Ngày: 2026-06-29 | Thực thi: Cowork (đọc trực tiếp file, không qua tóm tắt)
- Task: việc (1) trong scorecard — chốt cờ HS-revision (ảnh hưởng mọi merge) + "chắc concordance chuẩn".
- Trạng thái: **HOÀN TẤT audit. Cờ HS-revision GIẢI (khớp). Phát hiện 2 lỗi map → 1 nhiễm panel. Chờ user chốt phạm vi + rebuild.**

## 2. Đã kiểm gì (bằng chứng trực tiếp)
- Universe chuẩn: `product_codes_HS12_V202601.csv` = **5.202 mã HS2012** (từ BACI frozen, đã verify SHA cùng inventory).
- Đối chiếu mọi HS6 concordance: **136/137 mã atomic ∈ HS2012**; **panel ước lượng 125/125 KHỚP**; lumped-target 59/59 khớp.
- Quét semantic nhóm Annex I ↔ chương HS (pad eu_code 7 số — đã sửa bug bỏ-sót do mất số 0 đầu): 6 ca lệch chương, 4 là melon/dưa hấu/cucurbit (nhóm 02→chương 08 ĐÚNG theo HS), **2 là lỗi thật**.

## 3. Kết quả cốt lõi
**Cờ HS-revision: KHỚP.** Concordance dùng đúng HS2012 → merge với BACI HS12 căn đúng. Giải cờ Giai đoạn 0 (issues_log).

**2 lỗi ánh xạ (cùng nguồn `auto_sci_name / needs_review_noanchor`):**
| eu_code | mô tả EU | gán SAI | vấn đề | đúng (HS2012) | tác động panel |
|---|---|---|---|---|---|
| 0402020 | Oil palm kernels | **151010** | không tồn tại trong HS2012 | **120710** | analysis 0 dòng (rớt) → vô hại |
| 0401090 | Cotton **seeds** | **520100** | =xơ bông, chương **52 NGOÀI 07–12** | **120721** | **analysis 2.340 dòng = 0,12% KN (0,031% đi-EU) → NHIỄM** |

- Cotton: nhỏ về trọng số (khó lay β value-weighted) nhưng **sai bản chất + ngoài phạm vi + reviewer dễ bắt**.
- **Phát hiện hệ thống:** cả 2 lỗi từ `auto_sci_name` (khớp tên khoa học không neo). Đây là rổ yếu nhất: **22 mã auto_sci_name + ~95 mã needs_review** chưa soi semantic từng mã → đó là "việc (2)" để thật sự nói "concordance chuẩn".

## 4. Đề xuất (CHỜ user)
1. **Sửa concordance:** 151010→120710, 520100→120721 (bản vá: `12_audit/concordance_hs_revision_fixes_2026-06-29.csv`).
2. **Quyết phạm vi:** hạt bông/hạt cọ (oilseed, chương 12) có thuộc bài ASEAN rau-quả-nông-sản không? → nếu KHÔNG: chỉ **loại 520100** khỏi panel; nếu CÓ: thay bằng 120710/120721 và rebuild từ BACI.
3. **Soi rổ auto_sci_name (22) + needs_review (~95)** — việc (2), trước khi chốt concordance "chuẩn".

## 5. Cờ review
- KHÔNG ảnh hưởng kết luận diagnostic same-sample (đó là panel CŨ, mã khác). Đây là panel MỚI.
- Cần user: (a) chốt phạm vi oilseed; (b) cho rebuild panel sau sửa; (c) duyệt mở việc (2).

## 6. Con trỏ (12_audit/)
- `concordance_hs_revision_fixes_2026-06-29.csv` — 2 bản vá + bằng chứng.
- Universe: `01_raw_data_frozen/.../product_codes_HS12_V202601.csv` (5.202 mã).
