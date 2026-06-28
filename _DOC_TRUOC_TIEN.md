# 📌 ĐỌC TRƯỚC TIÊN — Cổng context cho chat Claude mới

> **Cho user:** mỗi khi mở chat Claude mới, dán **DUY NHẤT link raw của file này** và nói: *"Đọc file này và mọi link bên trong để nắm context dự án trước khi tư vấn."* Xong là Claude nắm trọn dự án mà bạn không cần kể lại.
>
> Link dán: `https://raw.githubusercontent.com/tranphu1508/XxX123/main/_DOC_TRUOC_TIEN.md`


> **🚀 ĐANG CHẠY (2026-06-29):** làm lại bài ASEAN, Cowork làm chính. Sau khi đọc 00–05, đọc tiếp **`_KICKOFF_ASEAN_REDESIGN.md`** → `https://raw.githubusercontent.com/tranphu1508/XxX123/main/_KICKOFF_ASEAN_REDESIGN.md` (việc #1: giải nghi vấn β panel cũ↔mới).

---

## 🤖 HƯỚNG DẪN CHO CLAUDE (làm theo đúng thứ tự, TRƯỚC khi tư vấn bất cứ điều gì)

Bạn đang tiếp nhận một dự án nghiên cứu kinh tế thương mại đang chạy. Bạn **KHÔNG** có ký ức về nó. Hãy `WebFetch` (hoặc đọc qua công cụ web) **6 file context theo đúng thứ tự 00 → 05** dưới đây, đọc HẾT, rồi mới phản hồi. Đừng tin tóm tắt — đọc nguyên văn.

1. **00 — Bàn giao tổng quan (đọc đầu tiên):**
   `https://raw.githubusercontent.com/tranphu1508/XxX123/main/context_knowledge/00_BAN_GIAO_TONG_QUAN.md`
2. **01 — Đề tài ASEAN (bài ĐANG HOẠT ĐỘNG, gravity biến-liên-tục, ITJ Q3):**
   `https://raw.githubusercontent.com/tranphu1508/XxX123/main/context_knowledge/01_DE_TAI_ASEAN.md`
3. **02 — Đề tài Việt Nam (đo-lường de jure/de facto, đang treo chờ lit review):**
   `https://raw.githubusercontent.com/tranphu1508/XxX123/main/context_knowledge/02_DE_TAI_VN.md`
4. **03 — Pipeline dữ liệu (hạ tầng dùng chung, đã audit):**
   `https://raw.githubusercontent.com/tranphu1508/XxX123/main/context_knowledge/03_PIPELINE_DU_LIEU.md`
5. **04 — Quy trình làm việc với Cowork:**
   `https://raw.githubusercontent.com/tranphu1508/XxX123/main/context_knowledge/04_QUY_TRINH_COWORK.md`
6. **⭐ 05 — Nhật ký quyết định + ngõ cụt (FILE QUAN TRỌNG NHẤT):**
   `https://raw.githubusercontent.com/tranphu1508/XxX123/main/context_knowledge/05_NHAT_KY_QUYET_DINH_NGO_CUT.md`

### ⚠️ Cảnh báo (chính chủ ghi)
- File **05** ghi mọi quyết định lớn + ngõ cụt đã đụng. **ĐỌC KỸ để KHÔNG đề xuất lại thứ đã bị loại.** Một Claude cùng model trước đây đã *quên các đợt chạy cũ (Đợt 1-3)* và đẩy bài ASEAN về "đo-lường" khi nó đã gần xong — **đừng lặp lại lỗi đó.**
- Bạn **không mở được file `.csv/.dta` gốc** của user; chỉ biết dự án qua repo này (báo cáo markdown).

---

## 📓 SAU KHI ĐỌC 00–05: xem nhật ký công việc mới nhất

- **Mục lục sống mọi đợt chạy (mới nhất trên cùng):**
  `https://raw.githubusercontent.com/tranphu1508/XxX123/main/handoff_index.md`
  (mỗi dòng = 1 đợt + link handoff chi tiết. Đọc vài dòng đầu để biết đợt gần nhất đã làm gì.)
- **Bản sao chỉ-đọc các output để rà** (`review_artifacts/`): liệt kê trong `handoff_index.md` mục "ARTIFACTS ĐỂ RÀ".

## 🗂️ Bộ context này gồm gì
6 file `context_knowledge/00–05` (do user soạn, trace từ transcript gốc) + `handoff_index.md` (log đợt chạy) + `review_artifacts/` (output để rà). Đây là **toàn bộ** thứ một chat mới cần.

> Sau khi đọc xong 00→05 + liếc `handoff_index.md`, hãy xác nhận ngắn gọn với user rằng bạn đã nắm: (a) dự án 2 bài (ASEAN gravity / VN đo-lường), (b) trạng thái hiện tại, (c) các ngõ cụt trong file 05 — rồi hỏi user muốn làm gì tiếp.
