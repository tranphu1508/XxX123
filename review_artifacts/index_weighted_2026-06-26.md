# Cắm ω vào chỉ số (weakest-link membership filter) + banned-but-used + re-validate — 2026-06-26

> Cắm rổ ω crop-level 2016 vào biến thể thắng (weakest-link × RASFF-18 × level) như **bộ lọc thành viên** (min MRL chỉ trên chất VN đăng ký cho cây đó). Xử banned-but-used thành kênh riêng. Re-validate RASFF. DỪNG trước BACI. Quy tắc bằng chứng nguyên văn.

## BƯỚC 0 — Đối chiếu xuyên chuỗi 2013–2024 (14 thông tư)
**Ca khả nghi đối chiếu nhiều bản, KHÔNG chỉ tin 03/2016:**

### 6 mã gap (kết luận: 2 lỗi-khớp-tên thu hồi được, 4 gap-thật)
- **bưởi (0110010), chanh (0110030): KHÔNG phải gap thật — lỗi khớp tên.** 03/2016 không có đăng ký TRỰC TIẾP trên 'bưởi'/'chanh' cho chất RASFF, NHƯNG có trên nhóm rộng **`cây có múi`** (citrus group): `cây có múi 03/2016 → dithiocarbamates, imidacloprid`. Nhóm 'cây có múi' áp cho MỌI cây có múi → thu hồi membership cho bưởi/chanh (= dithiocarbamates, imidacloprid). `omega_source=broad-citrus`.
- **đậu bắp (0231040), chanh leo (0162030), parsley (0256040), basil (0256080): GAP THẬT** (không có chuỗi tên cây riêng ở BẤT KỲ bản nào). Chỉ phủ qua nhóm RẤT rộng: `rau 03/2016 → carbendazim, dithiocarbamates` (đậu bắp/herbs); `cây ăn quả 03/2016 → dithiocarbamates` (chanh leo). → national/broad fallback, `omega_source=broad`.

### Chất "rớt" — mốc chính xác (dán chuỗi present)
```
carbendazim : 2013 2015 2016 2018 · · · · ·   → LOẠI sau 03/2018 (≈2019)
acephate    : 2013 2015 2016 2018 · · · · ·   → LOẠI sau 03/2018 (≈2019)
chlorpyrifos: 2013 2015 2016 2018 2019 2020 · · ·  → LOẠI sau 10/2020 (≈2021)
fipronil    : 2013 2015 2016 2018 2019 2020 · · ·  → LOẠI sau 10/2020 (≈2021)
```
→ KHÔNG phải "rớt 2023" đồng loạt — carbendazim/acephate rớt ~2019, chlorpyrifos/fipronil ~2021. Mốc cho biến "phản ứng đăng ký".

### banned-but-used xác nhận
`carbofuran` = **0 dòng** trong toàn bộ 14 thông tư; `methamidophos` = **0 dòng** → cấm SUỐT (không phải chỉ thiếu 03/2016). ✓

## BƯỚC 1 — ω-2016 crop-level → weakest-link (membership filter)
`S_lvl_max_omega2016[k,t] = −ln( min{ MRL_EU(a,k,t) : a ∈ membership^2016(k) } )` — min CHỈ trên chất VN đăng ký (loại ràng buộc ma). Membership mỗi mã (2016):

| mã VN | nguồn ω | #chất | chất trong weakest-link (membership) |
|---|---|---|---|
| Gạo | crop | 16 | (gần đủ RASFF: tricyclazole, chlorpyrifos, fipronil, carbendazim…) |
| Cà phê | crop | 15 | tương tự gạo |
| Vải/nhãn | crop | 13 | carbendazim, chlorpyrifos, fipronil, propiconazole… |
| Cam | crop | 6 | carbendazim, fipronil, hexaconazole, dithiocarbamates, imidacloprid, dinotefuran |
| Xoài | crop | 5 | acephate, carbendazim, dinotefuran, dithiocarbamates, hexaconazole |
| Chè | crop | 3 | acephate, dinotefuran, dithiocarbamates |
| Ớt, Thanh long, Sầu riêng | crop | 2 | carbendazim, dithiocarbamates |
| Quýt | crop | 2 | dithiocarbamates, imidacloprid |
| Chôm chôm, Chanh leo | crop/broad | 1 | dithiocarbamates |
| **Bưởi, Chanh** | **broad-citrus** | 2 | dithiocarbamates, imidacloprid (qua 'cây có múi') |
| **Đậu bắp, Parsley, Basil** | **broad-rau** | 2 | carbendazim, dithiocarbamates |
- Xuất song song bản ĐỀU `S_lvl_max_equal` (mọi RASFF-18) để so. Cột `omega_source` per mã.

## BƯỚC 2 — banned-but-used = KÊNH RIÊNG (không trộn)
- Chỉ số CHÍNH (ω2016) CHỈ chất đăng ký hợp pháp → carbofuran/methamidophos (ω=0) KHÔNG vào chính (giữ ngoại sinh sạch).
- `banned_used[k,t]` = số vụ RASFF carbofuran+methamidophos của cây k: **ớt 7, thanh long 3, trái-cây-khác 1, 'other' 10** (rau ăn lá: rau muống, đậu đũa…). + biến robustness `S_lvl_max_omega_plusbanned` (membership + 2 chất, gắn cờ).

## BƯỚC 3 — ω-2023 (phản ứng đăng ký)
`S_lvl_max_omega2023`: membership 2023 LOẠI các chất VN đã bỏ → vd **gạo: fipronil/chlorpyrifos/carbendazim/acephate rớt** → ω2023 thấp hơn ω2016 ở các năm chất đó là binding. Đây là biến phát hiện "VN siết DM theo áp lực EU/XK". (ω chính = 2016; 2023 = robustness + phân tích phản ứng.)

## BƯỚC 4 — RE-VALIDATE vs RASFF (Poisson 8 nhóm × 2015–2024, 200 vụ)
| biến thể | coef | p | AIC | pseudo-R² | ΔLL vs FE |
|---|---|---|---|---|---|
| **S_equal (weakest-link, mọi RASFF-18)** | +0,904 | 0,004 | **386,1** | 0,364 | +4,57 |
| S_omega2016 (ω-filter) | +0,284 | 0,076 | 391,9 | 0,353 | +1,69 |

**→ ω-filter (2016) KHÔNG cải thiện fit RASFF — fit YẾU hơn bản đều.** Lý do (trung thực): bộ lọc ω loại (a) ràng buộc-ma VÀ (b) chính carbofuran/methamidophos (banned-but-used, gây ~17 vụ ở ớt/rau) → mất tín hiệu. Bản đều fit tốt hơn vì gồm cả phantom + de-facto.

### CAVEAT CỨNG (đọc kỹ)
Hồi quy RASFF = **chọn + đo lường chỉ số, KHÔNG nhân quả** (đã double-dip: chọn chỉ số trên RASFF). Việc ω2016 fit RASFF kém hơn **KHÔNG** có nghĩa ω2016 sai cho phân tích thương mại: ω2016 là trọng số **ngoại sinh, tiền-định** (đúng nhận dạng); RASFF fit kém hơn là **đúng kỳ vọng** vì RASFF chứa banned-but-used + nội sinh cường-độ-kiểm-tra mà ω cố tình loại. **Outcome nhân quả chế độ 1 = biên mở rộng BACI, KHÔNG lặp RASFF.**

## Verdict (chờ Claude quyết)
1. **6 mã gap:** bưởi/chanh = lỗi-khớp-tên → **thu hồi crop-level qua nhóm 'cây có múi'**; đậu bắp/chanh leo/parsley/basil = **gap-thật → broad-rau/cây-ăn-quả fallback** (ghi cờ).
2. **ω-filter vs đều:** ω2016 fit RASFF KÉM hơn (kỳ vọng) — nhưng ngoại sinh sạch hơn. Đề xuất: **ω2016 = chính cho BACI nhân quả** (loại ràng buộc ma), bản đều = robustness, banned_used = kênh riêng.
3. **Membership 2016 vs 2023:** carbendazim/acephate rớt ~2019, chlorpyrifos/fipronil ~2021 → biến phản ứng đăng ký.

## DỪNG — CHƯA chạy hồi quy thương mại BACI. Chờ Claude: (a) ω-filter giữ hay đổi, (b) 6 mã gap OK chưa.
