# 04 — QUY TRÌNH LÀM VIỆC VỚI COWORK

> Cách Claude và user phối hợp. Nắm cái này để vận hành đúng nhịp đã chạy tốt suốt dự án.

---

## 1. PHÂN VAI
- **User** chạy **Cowork** (công cụ agentic desktop, có Python/DuckDB/Stata MP17) trên thư mục Windows dự án. Máy: i7-14700F, 64GB RAM DDR5, RTX 4070 Super.
- **Claude** viết **prompt .md** (trong `/mnt/user-data/outputs/`) cho user đưa Cowork chạy; rồi **review** kết quả Cowork qua repo GitHub.
- **Claude KHÔNG bao giờ** mở được file `.csv/.dta` thật của user. Chỉ thấy *báo cáo markdown* Cowork đẩy lên repo.

## 2. REPO HANDOFF-LOG
- Repo: **`https://github.com/tranphu1508/XxX123`** (standalone git, MARKDOWN-ONLY, public trong lúc làm dự án).
- Raw base: `https://raw.githubusercontent.com/tranphu1508/XxX123/main/`
- Cấu trúc:
  - `handoff_index.md` — mục lục sống (mới nhất trên cùng), mỗi dòng có **full raw URL** + tóm tắt 1 câu.
  - `handoff_<ngày>_<task>.md` — handoff từng task.
  - `review_artifacts/` — bản sao read-only các .md report để Claude rà.
- **Cache-bust:** user luôn đưa link index dạng `handoff_index.md?v=N` (tăng N mỗi lần) để tránh cache. Lần gần nhất khi viết bộ này: **v=22**.

## 3. CÁCH CLAUDE REVIEW (ràng buộc fetch)
- Claude **chỉ fetch được URL đã XUẤT HIỆN** trong hội thoại (web_fetch từ chối URL tự bịa/sửa path). → Quy trình: **fetch `handoff_index.md?v=N` TRƯỚC**, lấy các raw URL trong đó, RỒI fetch URL report cụ thể.
- User đưa link index → Claude fetch index → đọc dòng mới nhất → fetch report tương ứng trong `review_artifacts/` → review.

## 4. RÀNG BUỘC CÔNG CỤ (đã đụng nhiều lần)
- `web_fetch` trả **binary** cho .xlsx/.csv, **rỗng** cho trang JS (EUR-Lex, data.europa.eu, RASFF Window). → không fetch trực tiếp được nhiều nguồn.
- Cowork (máy user) cũng **không render trang JS**; bash/curl bị proxy chặn nhiều domain ngoài.
- **Stata KHÔNG chạy trong môi trường Cowork** → Cowork để lại `.do` cho user chạy tay.
- **MẪU xử dữ liệu bị chặn:** user **tải tay** trong browser → quăng vào thư mục dự án → Cowork parse local → Claude review qua repo. (Đã dùng cho: RASFF, Annex I pháp lý, 14 thông tư MARD.)

## 5. HAI KỶ LUẬT VÀNG (đừng bỏ)

### 5a. Quy tắc bằng chứng nguyên văn
Mọi quyết định **tra-cứu** (mã sản phẩm, hoạt chất, cây trồng, luật) phải **dán dòng nguồn NGUYÊN VĂN** (dòng CSV / field API / text pháp lý). Cowork KHÔNG đáng tin qua summary.
- **Đã bắt lỗi:** rambutan mis-group (0162020 sai → 0163060 đúng, chỉ grep raw mới lộ); lá-dâu-tây 0632010 ≠ quả 0152000 (cùng loài, khác bộ phận).
- Codified trong `00_/Cam_Nang_Quan_Tri_Du_An_Va_Checklist_Audit.md` làm chuẩn dự án.

### 5b. Prompt CÓ CỔNG (gated)
- Chẩn đoán / kiểm TRƯỚC khi ước lượng; **DỪNG sau mỗi chặng** để Claude review trước khi sang chặng sau.
- **Đã cứu nhiều lần:** cổng nhận-diện ASEAN bắt "độ-ngặt bó-sàn" *trước* khi dựng panel BACI lớn; cổng pre-trends lồng (kiểm cohort sạch nhất trước) tránh chạy cả gói lên nền hỏng.
- Cổng + **quy tắc dừng** (stop-rule): cam kết trước "nếu X fail thì dừng nhánh này", rồi nghe nó — chống sunk-cost.

## 6. FOOTER CHUẨN cho mọi prompt Cowork
1. Viết `handoff_<ngày>_<task>.md` (kèm các số chốt).
2. Thêm dòng đầu `handoff_index.md` + **full raw URL**; refresh `review_artifacts/`.
3. `git add` + commit local. **NHẮC USER push** (Cowork commit local, user push tay).
4. Nếu cần file user tải tay → nhắc rõ.

## 7. QUY ƯỚC ĐẶT TÊN
- File: English ASCII snake_case. Ngày ISO (YYYY-MM-DD). Parked không xóa (gắn cờ). Frozen = read-only trong `01_raw_data_frozen/`.
