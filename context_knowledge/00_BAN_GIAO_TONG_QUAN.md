# 00 — BÀN GIAO TỔNG QUAN (đọc file này TRƯỚC)

> **Mục đích:** Bộ tài liệu này để mỗi khi mở chat Claude mới, đưa link git đã push các file 00–05 này, Claude đọc lại là nắm trọn dự án mà không cần kể lại. Viết ngày 2026-06-28, sau một chuỗi phiên dài đã trace lại từ transcript gốc + project knowledge.
> **Cảnh báo cho Claude tương lai:** chat tạo ra bộ này rất dài và Claude (cùng model) đã từng *bỏ sót* các đợt chạy cũ (Đợt 1-2-3) đến khi user nhắc. ĐỪNG tin trí nhớ tóm tắt; mọi quyết định lớn nằm trong file 05. Đọc đủ 00→05 trước khi tư vấn.

---

## 1. DỰ ÁN LÀ GÌ

Nghiên cứu thực nghiệm kinh tế thương mại quốc tế: **tác động của việc EU thắt chặt MRL (Maximum Residue Level — giới hạn dư lượng thuốc bảo vệ thực vật) lên xuất khẩu nông sản**. Bối cảnh: EU siết MRL mạnh thời Green Deal; nông sản các nước đang phát triển (ASEAN, đặc biệt Việt Nam) chịu rào cản.

Dự án đã **tách thành HAI bài** dùng chung hạ tầng dữ liệu:

| | **Bài ASEAN** | **Bài Việt Nam** |
|---|---|---|
| Loại | Nhân quả-yếu / gravity (tương quan có điều kiện) | Đo lường / phương pháp + mô tả |
| Câu hỏi | EU siết MRL → thương mại nông sản ASEAN thế nào (rào cản, hình-dạng-cong, tái phân bổ) | Đo "độ ràng buộc thực" của MRL EU lên VN đúng cách nào (de jure vs de facto) |
| Nhận diện | Gravity biến-liên-tục đa phương (KHÔNG event-study) | Cắt-ngang trong-EU + validate RASFF (không nhân quả) |
| Tạp chí mục tiêu | **The International Trade Journal (Q3)** | Agri-food (Food Policy/ERAE/Agri Economics), Q2/Q3 |
| Trạng thái | Gần xong (Đợt 1-3 đã chạy), khôi phục framing cũ | Treo chờ literature review nghiêm túc |
| Chi tiết | **file 01** | **file 02** |

**Điểm mấu chốt:** hai bài KHÔNG cạnh tranh. Hạ tầng dùng chung (concordance EU→HS6, panel MRL EU, BACI, A_k). Phần ω-rổ-đăng-ký + RASFF + weakest-link là VN-only (đào sâu). Phần gravity đa phương + phi tuyến + tái phân bổ là ASEAN.

---

## 2. HAI PHA CỦA DỰ ÁN (quan trọng để hiểu lịch sử)

**PHA A — Gravity ASEAN gốc (trong project knowledge: NhatKy P1–P34, BaoCao_Nhom*).**
Xây panel ASEAN-5 (388.500 dòng), chạy **Đợt 1-2-3** ước lượng. Đã có kết quả chính (β=−2,077***), phi tuyến (inverted-U), tái phân bổ (TQ +6,06), event-study→phụ lục (pre-trends fail, đã xử lý đúng cách). **Đây là LÕI bài ASEAN — gần publication.** Quyết định 43 (P32): pilot "chỉ số song phương theo rổ đăng ký" cho VN trước khi tái cấu trúc → đẻ ra Pha B.

**PHA B — Re-audit + pivot VN (5 transcript 2026-06-26→28).**
Re-audit toàn pipeline trên hạ tầng sạch hơn (concordance pháp-lý-hóa, GitHub handoff log). Đọc bài đối thủ Nguyen (2026) → pivot sang bài VN-methods. Xây VN deep-dive: RASFF density, concordance lát VN pháp-lý, rổ ω crop-level, chỉ số weakest-link validated. **Rồi event-study (VN-only, sau đó ASEAN đa phương) FAIL pre-trends** → điều tra Homologa (bất khả với VN institutions) → **khôi phục framing gravity-liên-tục cũ cho ASEAN** (vì Đợt 2 đã chứng minh event-study nhị phân không hợp cho treatment liên tục).

**Bài học lớn nhất của Pha B:** dữ liệu MRL EU có **biến thiên nhận diện mỏng** (cross-section bó-sàn LOD 100%; theo-thời-gian ~54% tĩnh). Nên *nhận diện nhân quả sạch (event-study) bất khả* ở mọi khung (VN-only, đa phương, cắt-ngang). Lối đi đúng = gravity biến-liên-tục framing "tương quan có điều kiện" (Pha A đã làm) + đo-lường (bài VN).

---

## 3. TRẠNG THÁI HIỆN TẠI (2026-06-28)

- **Bài ASEAN:** quay về thiết kế gravity-liên-tục cũ (Đợt 1-3). Còn: Đợt 3 robustness (COVID, heterogeneity nhóm sản phẩm, placebo), quyết định *chạy lại trên hạ tầng mới hay giữ kết quả cũ*, và VIẾT. Nộp ITJ Q3.
- **Bài VN:** treo. Đã có: chỉ số validated, RASFF, ω, de jure/de facto. Thiếu: literature review nghiêm túc (lý do treo), khử-nội-sinh-kiểm-tra cho RASFF, hồi quy biên-mở-rộng-trong-EU, CELEX recovery acetamiprid/dinotefuran, và VIẾT.
- **Hạ tầng dữ liệu:** ĐÃ AUDIT (inventory sạch, tái lập chéo DuckDB↔pandas khớp). Chi tiết file 03.
- **Bước kế đề xuất:** trình đồng nghiên cứu (cho bài ASEAN) + chia việc; bài VN quay lại sau khi xong lit review.

---

## 4. CÁCH LÀM VIỆC (tóm tắt — chi tiết file 04)

User chạy **Cowork** (công cụ agentic desktop) trên thư mục Windows. **Claude KHÔNG mở được file .csv/.dta của user** — chỉ review qua **repo GitHub handoff-log markdown**: `https://github.com/tranphu1508/XxX123`. Quy trình: Claude viết prompt .md → user đưa Cowork chạy → Cowork push handoff .md + report → user đưa link `handoff_index.md?v=N` → Claude đọc review. **Claude chỉ fetch được URL đã xuất hiện** (phải fetch index trước, rồi fetch URL trong đó).

**Hai kỷ luật vàng (đừng bỏ):**
1. **Quy tắc bằng chứng nguyên văn:** mọi quyết định tra-cứu phải dán dòng nguồn nguyên văn (đã bắt lỗi rambutan, lá-dâu-tây). Cowork không đáng tin qua summary.
2. **Prompt có cổng:** chẩn đoán/kiểm TRƯỚC khi ước lượng; DỪNG sau mỗi chặng để Claude review. (Đã cứu nhiều lần: cổng nhận-diện ASEAN bắt bó-sàn trước khi dựng panel lớn.)

---

## 5. CHỈ MỤC BỘ TÀI LIỆU

| File | Nội dung |
|---|---|
| **00** (file này) | Tổng quan, hai bài, hai pha, trạng thái |
| **01_DE_TAI_ASEAN.md** | Bài ASEAN: thiết kế gravity-liên-tục, kết quả Đợt 1-3, xử lý pre-trends, còn gì |
| **02_DE_TAI_VN.md** | Bài VN: đo-lường, chỉ số, RASFF, ω, de jure/de facto, còn gì |
| **03_PIPELINE_DU_LIEU.md** | Hạ tầng dữ liệu: mọi artifact, vị trí file, trạng thái audit |
| **04_QUY_TRINH_COWORK.md** | Quy trình GitHub handoff, review, ràng buộc công cụ |
| **05_NHAT_KY_QUYET_DINH_NGO_CUT.md** | Quyết định lớn + ngõ cụt (ĐỪNG tái-tranh-luận) |

---

## 6. CẢNH BÁO "ĐỪNG TÁI-TRANH-LUẬN" (đầy đủ ở file 05)

- **ĐỪNG đề xuất lại event-study nhân quả cho MRL.** Đã fail pre-trends ở VN-only (+1,04), ASEAN đa phương (−1,51, ngược dấu), và cắt-ngang (bó-sàn). Lý do gốc: treatment liên tục + biến thiên mỏng. Framing đúng = gravity-liên-tục "tương quan có điều kiện".
- **ĐỪNG đề xuất ω động theo thời gian.** User đã thử, nội sinh nặng, loại. ω giữ tĩnh kỳ-gốc 2016.
- **ĐỪNG đề xuất cross-sectional VN cần Homologa** trừ khi user báo đã có license (AGU gần như chắc không có; đối thủ Nguyen lấy qua ANU).
- **ĐỪNG nhầm The World Economy là mục tiêu.** Đó là mục tiêu CŨ của bài ASEAN-nhân-quả. Giờ: ASEAN→ITJ Q3, VN→agri-food.
