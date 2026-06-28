# 02 — ĐỀ TÀI VIỆT NAM (đo-lường + de jure/de facto)

> Bài đang TREO chờ literature review nghiêm túc. Loại = đo-lường/phương pháp + mô tả thực chứng. Tạp chí: agri-food (Food Policy / ERAE / Agricultural Economics / JAE), **Q2/Q3 — KHÔNG phải The World Economy**. Framing: **tương quan có điều kiện, KHÔNG nhân quả** (event-study đã fail, xem file 05).

---

## 1. DANH TÍNH & CÂU HỎI
- **Câu hỏi:** *"Rào cản MRL của EU thực sự ràng buộc nông sản VN tới mức nào, và đo nó thế nào cho đúng?"* — đo-lường + mô tả, KHÔNG "MRL ảnh hưởng thương mại bao nhiêu" (không nhận diện được).
- **Trục xuyên suốt:** khoảng cách giữa rào cản **de jure** (trên giấy: chỉ số MRL) và **de facto** (thực thi ở biên: RASFF).
- **17 mã sản phẩm VN** (lát VN của concordance, pháp-lý-hóa chống Annex I): bưởi, cam, chanh, quýt, ớt, đậu bắp, vải+nhãn, chanh leo, **thanh long**, xoài, **chôm chôm**, sầu riêng, gạo, cà phê, chè, parsley, húng/rau thơm.

## 2. ĐỐI THỦ — Nguyen, Nguyen & Kalirajan (2026)
- *Agribusiness*, DOI 10.1002/agr.70107. VN cà phê + gạo, **5 thuốc** (azoxystrobin, chlorpyrifos, chlorantraniliprole, clothianidin, cyhalothrin), 2002–2017, PPML + IV-PPML, **194 nước nhập CẮT-NGANG**. Dữ liệu MRL từ **Homologa (qua ANU, Úc — KHÔNG qua trường VN)** + national + Codex.
- Nguyen **bác chỉ số gộp** (weakest-link/MIN cancel dấu), đòi weighting theo rổ nước-xuất.
- **Khác biệt hóa của ta (PHẢI sắc, vì Nguyen rất gần):** 17 sản phẩm (vs 2); chỉ số weakest-link **được validate bằng RASFF**; rổ ω đăng-ký crop-level; **khung de jure/de facto**. Điểm thắng *duy nhất* = **RASFF validation + de jure/de facto** (Nguyen không có). KHÔNG bán "nhiều sản phẩm hơn".

## 3. BA ĐÓNG GÓP

### Đóng góp 1 — Chỉ số stringency song phương tốt hơn
- **weakest-link** (−ln(min MRL) = chất ngặt nhất = ràng buộc thật) thay vì trung bình. **weakest-link >> mean** (mean dự báo RASFF gần như vô nghĩa).
- **Lọc qua rổ đăng ký VN crop-level (ω) như BỘ LỌC THÀNH VIÊN:** min chỉ lấy trên chất VN đăng ký cho cây đó → loại "ràng buộc ma" (EU ngặt trên chất VN không dùng). *(Không nhân ω vào min — ω chọn TẬP, MRL cho độ cao, min chọn gắt nhất.)*
- Nhắm đúng lỗ hổng văn liệu tự thừa nhận: Li-Beghin BSI/Rn/HIT "giả định trọng số đều cho mọi thuốc". Cải tiến = weighting theo rổ thực dùng.

### Đóng góp 2 — Validate chỉ số bằng RASFF (cái Nguyen KHÔNG có)
- Cho chỉ số dự báo **số vụ từ chối biên giới thực** (RASFF). Horse-race: weakest-link×RASFF-18 THẮNG (**coef +0,90, p=0,004**, Poisson group-FE+year-FE).
- **CAVEAT CỨNG:** đây là *chọn chỉ số + validate đo lường*, KHÔNG nhân quả. (a) một phần CƠ HỌC (MRL ngặt → cơ học dễ vượt → nhiều rejection); (b) N nhỏ (80 obs = 8 nhóm×10 năm); (c) **double-dip** (chỉ số được chọn ĐỂ tối đa dự báo RASFF → không được báo lại hồi quy RASFF như kết quả độc lập). → outcome chế độ 1 nên là **biên-mở-rộng BACI**, không lặp RASFF.

### Đóng góp 3 — Đo khoảng cách de jure/de facto (sắc nhất, độc đáo nhất)
Bốn kiểu lệch, định lượng được:
1. **Ràng buộc ma:** EU ngặt nhưng VN không dùng → 0 rejection. (= cái bộ lọc ω loại.)
2. **Tĩnh-strict-vẫn-bị-từ-chối:** thanh long MRL gần như tĩnh nhưng 61 vụ RASFF → đo "mức ngặt theo giấy" bỏ sót ma sát.
3. **Cấm-nhưng-vẫn-dùng:** carbofuran + methamidophos **bị VN cấm** (ω=0, chưa từng đăng ký) nhưng **vẫn 25 vụ RASFF** (dùng lậu). De jure nói "không có", de facto nói "có và đang chặn hàng". **Minh chứng đắt giá nhất.**
4. **Trễ đăng ký:** VN loại chất *sau* EU — carbendazim/acephate ~2019 (sau EU 2014-16), chlorpyrifos/fipronil ~2021 (sau EU 2020). de jure VN đuổi theo de facto EU, trễ 1-5 năm. (Đo từ đối chiếu xuyên-chuỗi 14 thông tư.)

## 4. KHUNG CHẺ-ĐÔI (bifurcated friction)
Ma sát MRL chia hai chế độ:
- **Chế độ 1 "ngặt-dai-dẳng/level":** carbendazim, trái cây nhiệt đới, tĩnh-strict. → chỉ số level + outcome RASFF/biên-mở-rộng. BACI mù.
- **Chế độ 2 "đang-siết/shock":** tricyclazole×gạo 2018, chlorpyrifos×gạo/chè 2021, fipronil×ớt 2021, propiconazole×citrus 2022. → lẽ ra event-study, **NHƯNG ĐÃ FAIL pre-trends** (xem file 05). Chế độ 2 nhân quả KHÔNG đạt → bài về đo-lường chế độ 1 + mô tả.

## 5. DỮ LIỆU CHÍNH (đã có, đã audit)
- **RASFF:** 328 notification / 180 border rejection, 2002–2026 (dày từ 2013), loại thủy sản. Hot: ớt/tiêu 100, thanh long 61, cà phê/chè 30, trái khác 19, gạo 15, sầu riêng 9. **RASFF-18 substances:** carbendazim 37, permethrin 32, chlorfenapyr 30, chlorpyrifos 28, tricyclazole 23, hexaconazole 21, acetamiprid 21, propiconazole 20, dithiocarbamates 16, imidacloprid 15, carbofuran 15, dinotefuran 13, profenofos 12, cypermethrin 11, acephate 10, methamidophos 10, dimethoate 8, fipronil 8. *(CAVEAT: nội sinh cường-độ-kiểm-tra — hot products dày VÌ trên danh sách Reg 2019/1793.)*
- **MRL identifying-power:** 34% cặp có-bước-trong-cửa-sổ, 41% phẳng-ở-sàn, ~54% không biến thiên thời gian. Top-3 chất (carbendazim/permethrin/chlorfenapyr) KHÔNG biến thiên in-window.
- **ω crop-level (Thông tư 03/2016 = "MARD 2016" Nguyen):** carbendazim 2016 đăng ký 29 cây. Giàu cho gạo (16 chất)/cà phê (15)/vải (13), MỎNG cho marquee fruit (ớt 2, sầu riêng 2). 6 mã gap (bưởi/chanh thu hồi qua 'cây có múi'; đậu bắp/chanh leo/parsley/basil = gap-thật → national fallback). ω chính = 2016 tĩnh (ngoại sinh; bản 2023 nội sinh, chỉ robustness).

## 6. CÒN GÌ PHẢI LÀM
- **Literature review nghiêm túc** (LÝ DO TREO — user tự nhận chưa làm đủ).
- **Khử-nội-sinh-kiểm-tra cho validation RASFF** (partial out cường độ kiểm tra Reg 2019/1793).
- **Hồi quy biên-mở-rộng trong-EU** (across product×substance, FE sản phẩm + FE chất: EU ngặt → VN có hiện diện thị trường không) — chân thực-chứng gợi ý DUY NHẤT không cần Homologa, không vấp pre-trends. *(Vẫn caveat nội sinh — gợi ý, không nhân quả.)*
- **CELEX recovery acetamiprid (MISSING_FROM_A_k) + dinotefuran (null 16/17)** — 2 neonicotinoid, cho chỉ số đủ.
- **VIẾT.** Bảng: chỉ số + horse-race RASFF + bảng 4-kiểu-lệch de jure/de facto + mô tả hai-cửa-sổ.

## 7. ĐỊNH VỊ & CẢNH BÁO
- Khu phố agri-food (Food Policy/ERAE/Agri Economics/JAE), KHÔNG trade-thuần. Q2/Q3.
- **Sức nặng thấp hơn bài nhân quả** — đo-lường + mô tả. Đăng được nếu cái thước *mới + được chứng minh tốt hơn*.
- Đối đầu Nguyen ở phần chỉ số → chỉ thắng nhờ RASFF-validation + de jure/de facto. Hai mảnh đó gánh toàn bộ novelty.
- **Nâng cấp tiềm năng:** nếu lấy được Homologa (MRL đa đích) → thêm chân cắt-ngang (như Nguyen). Nhưng AGU gần như chắc không có license; xem file 05 mục Homologa.
