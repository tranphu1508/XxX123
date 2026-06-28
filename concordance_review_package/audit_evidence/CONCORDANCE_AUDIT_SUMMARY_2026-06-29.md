# TỔNG KẾT AUDIT CONCORDANCE EU→HS6 (toàn bộ 381 mã) — 2026-06-29

> Soi 100% concordance (theo yêu cầu user). Bằng chứng nguyên văn = mô tả chính thức HS2012 (product_codes_HS12_V202601, 5.202 mã, đã verify SHA) đặt cạnh sản phẩm EU + loài (Annex I Reg 2018/62).

## 1. Phân loại toàn bộ 381 mã
| Lớp | Số mã | Nghĩa |
|---|---|---|
| **OK** | 168 | Map đúng (khớp tên/loài với mô tả HS2012) — lõi tin cậy |
| NO_HS6 | 97 | Không gán HS6: động vật/nec/ngoài phạm vi (loại hợp lệ) |
| UMBRELLA/multi | 38 | Umbrella hợp lệ (081090 trái cây lạ, 121190 dược thảo) + ô đa-mã |
| **LUMPING** | 53 | Gộp sản phẩm phụ vào 1 mã đại diện (vấn đề PHƯƠNG PHÁP, xem §3) |
| catchall | 20 | Mục "Others (2)" / nhóm (a)(b)(c) — phần lớn excluded_nec |
| **ERROR** | ~12–15 | Lỗi map thật (thay thế sai sản phẩm) — xem §2 |

**Đính chính số trung gian:** con số "130 flag / 112 lỗi" ở bước soi đầu là do detector thô (bỏ sót số nhiều/cùng-từ) → **44 trong đó là FALSE-FLAG, thực ra ĐÚNG** (rye→rye, kiwi→kiwifruit, grapefruit→grapefruit, đậu nành→soya, lạc→groundnut...). Sau lọc: lõi OK lớn, lỗi thật chỉ ~12–15.

## 2. Lỗi map XÁC NHẬN (~12–15) — `concordance_confirmed_errors_2026-06-29.csv`
- **Hạt dầu (auto_sci_name, 8):** mè→thầu dầu, cải dầu→mè, anh túc→cải dầu, rum→bông, borage→rum, camelina→mù tạt, **kapok→óc chó**, **quả cọ→ô liu**. Kim ngạch ~0,08% → β gần như không đổi.
- **Trái/củ (needs_arbitration, ~4–6):** **lựu+mãng cầu→080390 CHUỐI** (8% panel), **su hào→071410 SẮN** (6%), hạt thông→080112 dừa, **nguyệt quế→070992 ô liu**, cải ngựa→091091 hỗn hợp gia vị.
  - Lưu ý: chuối/sắn VẪN map đúng từ verified_high → lỗi **làm bẩn weakest-link stringency** mã chuối/sắn (thêm chất của lựu/su hào), KHÔNG bịa kim ngạch. Mức méo chưa đo.

## 3. Vấn đề PHƯƠNG PHÁP — lumping chọn mã đại diện sai (53 ca, ~19 mã panel)
- Cơ chế: sản phẩm phụ không có HS6 riêng (rau thơm: parsley, chervil, chives, tarragon...) bị **gộp vào HS6 của MỘT thành viên cụ thể** thay vì mã "n.e.c." chung. Ví dụ: parsley/chervil/chives/tarragon/stem-veg **gộp vào 070920 = MĂNG TÂY** (vì asparagus 270010 cũng trong nhóm).
- Hệ quả: stringency + (nếu mã trong panel) thương mại của măng tây/aubergine... bị trộn MRL của rau thơm. **19 mã panel** bị gộp lẫn kiểu này.
- Đây là **lựa chọn thiết kế thô**, không phải bug ngẫu nhiên (cột `hs6_lumped` ghi nhận có chủ đích). Nhưng nên **tái-neo lump về mã "n.e.c." chung** (vd 070999) thay vì thành viên cụ thể (070920). → cần quyết định mô hình của user.

## 4. Trả lời "concordance chuẩn 100% chưa"
**Chưa tuyệt đối, nhưng KHÔNG hỏng nặng như con số thô ban đầu.** Lõi 168 OK + umbrella hợp lệ + loại-đúng-97 là vững (false-flag xác nhận map sạch đúng). Cần làm: (a) sửa ~12–15 lỗi thay-thế; (b) quyết tái-neo 53 ca lumping; (c) rebuild + đo méo stringency chuối/sắn. Lõi giá trị bài (sầu riêng/thanh long/cà phê/gạo/tiêu) thuộc OK/verified → **β chính nhiều khả năng vững**; phần sửa chủ yếu dọn rìa + minh bạch.

## 5. Con trỏ
- `concordance_full_review_classified_2026-06-29.csv` — 381 mã + lớp + in_panel.
- `concordance_confirmed_errors_2026-06-29.csv` — danh sách lỗi + mã đúng đề xuất.
- Backup trước vá: `03_/outputs/concordance_final_asean_pre_hsfix_2026-06-29.csv`.
