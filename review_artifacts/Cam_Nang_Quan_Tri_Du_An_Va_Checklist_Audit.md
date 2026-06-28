# CẨM NANG QUẢN TRỊ DỰ ÁN & CHECKLIST AUDIT
Đề tài: Tác động của thắt chặt mức dư lượng tối đa của EU (EU Maximum Residue Levels) lên xuất khẩu Đông Nam Á

Mục tiêu: rà soát toàn bộ pipeline → tổng hợp findings → viết Abstract & Introduction → nộp The International Trade Journal (ITJ)

File này là tài liệu chuẩn để Cowork dựng và quản lý thư mục dự án. Gồm ba phần: (1) cấu trúc thư mục, (2) quy ước đặt tên và quản lý phiên bản, (3) checklist audit bốn giai đoạn gắn vào từng thư mục.

## PHẦN 1 — CẤU TRÚC THƯ MỤC

Nguyên tắc: thư mục đánh số theo thứ tự pipeline để tự nó kể được dòng chảy dữ liệu; tách bạch dữ liệu thô (đóng băng, không sửa) khỏi dữ liệu xử lý và kết quả cuối; có một thư mục riêng cho nhật ký audit và một thư mục riêng cho bản thảo.

> Ghi chú vị trí (cập nhật 2026-06-26): thư mục chứa `eu_maximum_residue_level_asean_export_study/` này nằm bên trong một thư mục gốc lớn hơn — `EU standards Effects on ASEAN Agri-food Exports/` — đặt cùng cấp với các thư mục thử nghiệm cũ (`Reading`, `Version 1`, `Version 2`, `Xây dựng biến`, `Ý tưởng ban đầu`). Các thư mục cũ này không thuộc pipeline hiện hành; toàn bộ phần còn lại của cẩm nang giữ nguyên.

```text
eu_maximum_residue_level_asean_export_study/
│
├── 00_project_documentation/
│   ├── readme_project_overview.md                  # bản đồ toàn dự án, đọc trước tiên
│   ├── data_sources_and_provenance.md              # nguồn, phiên bản, ngày snapshot, URL, checksum
│   ├── variable_dictionary.md                       # định nghĩa mọi biến
│   ├── file_naming_conventions.md                   # bản sao Phần 2 của cẩm nang này
│   └── audit_master_checklist.md                    # bản sao Phần 3, dạng tick-off
│
├── 01_raw_data_frozen/                              # CHỈ ĐỌC — không bao giờ chỉnh sửa
│   ├── trade_data_baci/
│   ├── european_union_maximum_residue_level_snapshot/
│   ├── eurlex_backfill/
│   ├── tariff_data_world_integrated_trade_solution/
│   └── pesticide_registration_vietnam/
│
├── 02_data_collection_and_api_scripts/
│   ├── scripts/
│   ├── download_logs/
│   └── readme_data_collection.md
│
├── 03_concordance_product_code_to_harmonized_system_six_digit/
│   ├── scripts/
│   ├── outputs/
│   ├── manual_spot_checks/
│   ├── archive_superseded/
│   └── readme_concordance.md
│
├── 04_maximum_residue_level_panel/
│   ├── scripts/
│   ├── outputs/
│   ├── missing_value_treatment/
│   ├── archive_superseded/
│   └── readme_maximum_residue_level_panel.md
│
├── 05_active_ingredient_set_and_classification/     # tập Aₖ, số đăng ký hóa chất (CAS), phân loại — phần Việt Nam
│   ├── scripts/
│   ├── outputs/
│   ├── archive_superseded/
│   └── readme_active_ingredients.md
│
├── 06_analysis_dataset_merge/
│   ├── scripts/
│   ├── outputs/
│   ├── merge_diagnostics/
│   ├── archive_superseded/
│   └── readme_merge.md
│
├── 07_main_estimation_stata/
│   ├── do_files/
│   ├── results_logs/
│   ├── estimation_tables/
│   └── readme_main_estimation.md
│
├── 08_robustness_checks/
│   ├── do_files/
│   ├── results_logs/
│   ├── robustness_tables/
│   └── readme_robustness.md
│
├── 09_placebo_and_market_expansion_tests/
│   ├── do_files/
│   ├── results_logs/
│   └── readme_placebo_and_market_expansion.md
│
├── 10_final_tables_and_figures/
│   ├── tables/
│   ├── figures/
│   └── readme_final_outputs.md
│
├── 11_audit_findings_and_issues_log/
│   ├── issues_log.md                                # nhật ký lỗi sống, ghi theo ngày bên trong
│   ├── findings_phase_0_data_pipeline/
│   ├── findings_phase_1_estimation/
│   ├── findings_phase_2_robustness/
│   ├── findings_phase_3_placebo_market_expansion/
│   ├── findings_phase_4_magnitude_reporting/
│   └── readme_audit_findings.md
│
├── 12_manuscript_abstract_and_introduction/
│   ├── abstract/
│   ├── introduction/
│   ├── full_draft/
│   ├── references/
│   └── readme_manuscript.md
│
└── 13_submission_international_trade_journal/
    ├── cover_letter/
    ├── data_availability_statement/
    ├── replication_package/
    └── readme_submission.md
```

Mỗi thư mục pipeline (03–09) có cùng bố cục con: scripts/ hoặc do_files/ (mã), outputs/ (kết quả hiện hành), archive_superseded/ (phiên bản cũ đã bị thay), và một file readme_*.md mô tả thư mục + chỉ ra file hiện hành.

## PHẦN 2 — QUY ƯỚC ĐẶT TÊN & QUẢN LÝ PHIÊN BẢN

### 2.1. Quy tắc đặt tên file và thư mục

Tên tiếng Anh, viết thường, dùng dấu gạch dưới (snake_case), không dấu cách, không ký tự đặc biệt, không dấu tiếng Việt. Lý do: Stata và Python dễ vỡ đường dẫn khi gặp dấu tiếng Việt hoặc dấu cách; tên ASCII chạy ổn định trên mọi máy. (Nội dung bên trong file vẫn viết tiếng Việt như quy ước dự án; chỉ tên file dùng tiếng Anh.)

Không viết tắt. Viết đầy đủ: maximum_residue_level chứ không mrl; poisson_pseudo_maximum_likelihood chứ không ppml; harmonized_system_six_digit chứ không hs6. Tên dài hơn nhưng người mới mở folder vẫn hiểu ngay.

Tên mô tả nội dung, không mô tả bước máy móc. trade_data_filtered_asean_to_european_union.csv chứ không output_step3.csv.

Thay nhãn rút gọn nội bộ bằng tên mô tả. Ví dụ bốn cách đo độ ngặt đang gọi M1–M4 phải đặt theo định nghĩa của chúng, ví dụ stringency_index_<định_nghĩa_cụ_thể>_..., không để "M1".

### 2.2. Quy tắc ngày tạo cho file có nhiều phiên bản

File dữ liệu/kết quả có thể tái tạo nhiều lần (concordance, panel, dataset merge, bảng kết quả): bắt buộc gắn ngày tạo dạng ISO YYYY-MM-DD ở cuối tên.

Ví dụ: concordance_product_code_to_harmonized_system_six_digit_2026-06-25.csv

Ví dụ: analysis_dataset_merged_2026-06-25.dta

File tải thô đặt theo ngày tải: baci_trade_raw_download_2026-06-20/.

Tài liệu sống và nhật ký (mọi readme_*.md, issues_log.md): giữ một tên cố định, không gắn ngày vào tên, mà ghi ngày bên trong mỗi mục (append-only). Lý do: log/README cần một địa chỉ ổn định để mọi nơi trỏ tới.

Mã nguồn (.py, .do): tên cố định không gắn ngày (lịch sử do Git/Cowork giữ); nếu chưa dùng version control thì khi sửa lớn mới tạo bản mới có ngày và đưa bản cũ vào archive_superseded/.

### 2.3. Vòng đời file & quản lý phiên bản

01_raw_data_frozen/ là bất khả xâm phạm. Không sửa, không xóa, không tạo file mới ở đây sau khi đã đóng băng. Mọi biến đổi đọc từ đây và ghi ra thư mục khác.

Một "phiên bản hiện hành" duy nhất cho mỗi sản phẩm. Khi tái tạo một file (ví dụ build lại concordance), tạo file mới có ngày hôm nay, di chuyển file cũ vào archive_superseded/ (không xóa — giữ vết audit), và cập nhật dòng "Phiên bản hiện hành" trong readme_*.md của thư mục.

Mỗi readme_*.md của thư mục pipeline có một mục bắt buộc: "Phiên bản hiện hành" (tên file + ngày), "Script tạo ra nó", "Đầu vào lấy từ thư mục nào", "Kiểm tra đã pass" (trỏ tới mục checklist tương ứng).

### 2.4. Vai trò của Cowork khi quản lý thư mục

Khi tạo lại một file output: tự động chuyển bản cũ vào archive_superseded/, đặt tên bản mới có ngày, cập nhật README thư mục.

Khi audit phát hiện một vấn đề: ghi một mục mới vào 11_audit_findings_and_issues_log/issues_log.md với ngày, giai đoạn, file liên quan, mức nghiêm trọng, trạng thái.

Không bao giờ ghi đè file trong 01_raw_data_frozen/.

Khi một mục checklist được xử lý xong: tick trong 00_project_documentation/audit_master_checklist.md và liên kết tới bằng chứng (đường dẫn file kết quả/log).

### 2.5. Mẫu một dòng nhật ký lỗi (issues_log.md)

```text
## 2026-06-25 — [Giai đoạn 1] — Tách biệt vi sai EU vs non-EU
- File liên quan: 07_main_estimation_stata/results_logs/separation_diagnostics_2026-06-25.txt
- Mô tả: EU giữ 26% quan sát, non-EU 45,5% → nghi ảnh hưởng contrast tái phân bổ.
- Mức nghiêm trọng: CAO (rủi ro reject).
- Hành động: chạy test độ nhạy trên tập sản phẩm có dòng EU dương.
- Trạng thái: ĐANG XỬ LÝ
```

## PHẦN 3 — CHECKLIST AUDIT BỐN GIAI ĐOẠN

Định hướng cho ITJ (Q3): mục tiêu không phải chứng minh nhân quả (pre-trends fail, không ép được), mà là (1) không còn lỗi kỹ thuật, (2) trung thực về nhận dạng, (3) robustness đã có và lập bảng gọn, (4) đóng hai phản biện hiển nhiên. Mỗi mục ghi: Kiểm gì → Vì sao → Tiêu chí đạt → Bằng chứng lưu ở đâu.

> ### ⭐ CHUẨN THƯỜNG TRỰC — QUY TẮC BẰNG CHỨNG NGUYÊN VĂN (áp cho MỌI task, mọi giai đoạn)
> Mọi **quyết-định-tra-cứu** — gán mã sản phẩm/chất qua synonym hay tên khoa học, chọn MRL, lấy group-default, lập mapping, hay khớp mờ (fuzzy) — PHẢI kèm **dòng nguồn NGUYÊN VĂN** (dòng CSV / trường API gốc / trích văn bản pháp lý) ngay trong báo cáo. **Kết luận không kèm bằng chứng nguyên văn = CHƯA HOÀN TẤT.**
> *Lý do:* người rà soát (Claude) đọc qua báo cáo và KHÔNG mở được file gốc; bản tóm tắt có thể giấu lỗi. Ví dụ thực: lỗi rambutan bị gán nhầm `0162020` (đúng ra `0163060` 'Cherimoyas') chỉ bị bắt nhờ **grep nguyên văn** trường synonym, không phải nhờ câu kết luận tóm tắt. Tương tự, acetamiprid "có trong snapshot" chỉ lộ ra là **không có MRL in-window 2015–2024** khi dán dòng record (application_date 2025+).
> *Áp dụng:* trước khi gọi bất kỳ kết quả tra-cứu nào là FINAL, dán dòng nguồn; nếu gán MRL cho một sản phẩm, dán CẢ dòng catalogue (định danh) LẪN dòng panel/snapshot (mang giá trị đó).

### GIAI ĐOẠN 0 — Toàn vẹn dữ liệu & pipeline

(Rà trước tiên; sai ở đây thì mọi kết quả vô nghĩa. Bằng chứng: thư mục 01–06.)

- [ ] Xuất xứ & đóng băng (provenance). Cố định phiên bản BACI (năm phát hành, bản HS), ngày snapshot EU Maximum Residue Level Database, ngày backfill EUR-Lex; lưu checksum. → Đạt: 00_project_documentation/data_sources_and_provenance.md đầy đủ và có checksum khớp. → Lưu: 00, 01.

- [ ] Script API — kiểm độ ĐẦY ĐỦ, không chỉ độ đúng. Bản tải MRL (JSON lớn) dễ bị cắt do phân trang/giới hạn tốc độ/thiếu năm. Chạy lại và diff với bản đã lưu; đếm bản ghi theo năm. → Đạt: số bản ghi mỗi năm khớp kỳ vọng, không năm nào trống bất thường. → Lưu: 02/download_logs.

- [ ] Concordance product_code → HS6. Vì bản v2 từng có lỗi build (521 mã nông sản bị bỏ map oan): xác nhận bản hiện hành có tỷ lệ phủ đúng, xử lý nhóm catch-all "n.e.c." (~55 mã thực sự bất khả ánh xạ), gắn cờ EUDR cho ~59 mã cao su, và có quyết định phương pháp tường minh cho ~286 mã chế biến (không bị drop âm thầm). Bốc tay mẫu ngẫu nhiên để soi. → Đạt: spot-check khớp 100% mẫu; coverage giải thích được từng nhóm. → Lưu: 03.

- [ ] Panel Maximum Residue Level (a,k,t) 2015–2024. Kiểm logic backfill; kiểm 5,5% không usable được xử lý thế nào và độ nhạy kết quả với cách impute; xác nhận dấu kết quả chính bền qua cả 4 cách đo độ ngặt. → Đạt: 4 cách đo cùng dấu; impute không đảo kết luận. → Lưu: 04.

- [ ] Tập hoạt chất Aₖ. Soi mẫu ánh xạ hoạt chất×cây; làm sạch đồng nghĩa cây, loại cây cảnh/công nghiệp. → Đạt: mẫu soi đúng; không còn cây ngoài phạm vi. → Lưu: 05.

- [ ] Merge & cross-check. Tỷ lệ khớp panel MRL × BACI; chẩn đoán phần không khớp; chạy lại bộ cross-check 7/7 sau mọi sửa pipeline. → Đạt: 7/7 pass lại. → Lưu: 06/merge_diagnostics.

- [ ] Biến treatment. Xác minh tổng hợp từ cấp hoạt chất lên cấp sản phẩm, và các biến thắt chặt (sai phân, lag, tích lũy, bins, năm sự kiện) tính đúng; Regulation áp giữa năm xử lý bằng lag. → Đạt: tái tạo được vài giá trị bằng tay. → Lưu: 04, 06.

- [ ] **Bằng chứng nguyên văn cho mọi tra-cứu (CHUẨN THƯỜNG TRỰC — xem đầu Phần 3).** Mọi gán mã/chất/MRL qua synonym, tên khoa học, group-default, mapping hay khớp mờ phải kèm **dòng nguồn nguyên văn** (CSV/API/CELEX) trong báo cáo TRƯỚC khi gọi FINAL. → Đạt: mỗi quyết-định-tra-cứu trong report có ≥1 dòng nguồn dán kèm, reviewer tự kiểm được mà không cần mở file gốc. → Lưu: report của task + review_artifacts. → Vì sao: tóm tắt giấu lỗi (vd rambutan 0162020→0163060, acetamiprid không-MRL-in-window) chỉ lộ qua dòng nguyên văn.

### GIAI ĐOẠN 1 — Test reviewer dễ reject (sửa-hoặc-chết)

(Bằng chứng: thư mục 07.)

- [ ] Tách biệt vi sai (differential separation) — CỜ ĐỎ LỚN NHẤT. EU giữ 26% quan sát so với non-EU 45,5%; tổng 67% bị loại. Dù gần 100% dòng dương được giữ, EU thưa hơn khiến contrast tái phân bổ có thể do thành phần. → Hành động: (a) báo cáo chẩn đoán tách biệt; (b) test độ nhạy trên tập sản phẩm có dòng EU dương / trong nhóm sản phẩm giao dịch cả EU lẫn non-EU; (c) ghi vào hạn chế. → Đạt: kết luận tái phân bổ sống sót test độ nhạy.

- [ ] Zero trade flows nằm trong mẫu ước lượng. PPML giữ zeros — xác nhận sample không bị lọc còn dòng dương; báo cáo song song full-sample vs truncated PPML. → Đạt: zeros có mặt; hai phiên bản cùng hướng.

- [ ] Hiệu ứng cố định bắt kháng cự đa phương (multilateral resistance). Cấu trúc αᵢₖₜ + γᵈₜ + δᵢᵈₖ đúng chuẩn structural gravity, tránh "sai lầm huy chương vàng". → Đạt: phát biểu rõ trong bài; treatment không bị FE nuốt.

- [ ] Hiệu chỉnh bias FE ba chiều (Weidner & Zylkin). Đã chạy ppml_fe_bias; lưu ý nó không lưu theo format chuẩn Stata nên phải đọc hệ số/SE hiệu chỉnh trực tiếp từ log. Báo cáo cả hệ số và SE đã hiệu chỉnh. → Đạt: bảng có cột hiệu chỉnh; nêu rõ kết quả nào gần biên mất ý nghĩa sau hiệu chỉnh.

- [ ] Cluster sai số chuẩn. Chốt một cách cluster chính; chứng minh suy luận bền qua các cách thay thế. → Đạt: dấu/ý nghĩa ổn định qua ≥2 cách cluster.

- [ ] Pre-trends / event study — LỖ HỔNG LỚN NHẤT, không giấu. Báo cáo trung thực; bỏ ngôn ngữ nhân quả; truy nguyên vì sao fail (anticipation, EUDR 2023, EVFTA 2020, COVID). Với Tₖ so le dùng estimator robust theo timing (Callaway–Sant'Anna) + dải tin cậy đồng thời. → Đạt: event study có mặt, khung "tương quan có điều kiện" nhất quán toàn bài, có thảo luận confounder.

- [ ] Dạng hàm. RESET đã bác bỏ tuyến tính (biện minh phi tuyến). Xác nhận đặc tả phi tuyến cuối (quadratic + spline + threshold + bins) đã giải quyết. → Đạt: nhiều phương pháp hội tụ về cùng hình dạng.

### GIAI ĐOẠN 2 — Bộ robustness (phần lớn đã chạy; xác minh + gom một bảng)

(Bằng chứng: thư mục 08.)

- [ ] Bỏ năm 2020 (COVID).

- [ ] Kiểm soát thuế quan + biên ưu đãi EVFTA cho Việt Nam–EU.

- [ ] Gộp EU-27 thành một thị trường (tránh nhân rộng cú sốc).

- [ ] Đổi nhóm tham chiếu tái phân bổ (Mỹ vs toàn bộ non-EU vs Nhật+Hàn).

- [ ] Các định nghĩa treatment thay thế (mức, sai phân, tích lũy, lag).

- [ ] Leave-one-out theo HS2 và theo nước.

- [ ] Chạy riêng nhóm sản phẩm (cà phê/chè, gia vị, hạt, trái cây, rau, ngũ cốc).

- [ ] → Đạt: một bảng robustness gọn cho thấy dấu và bước ngoặt ổn định qua tất cả.

### GIAI ĐOẠN 3 — Hai test rẻ-tiền đóng hai phản biện hiển nhiên

(Bằng chứng: thư mục 09.)

- [ ] Placebo hoán vị (tính đặc thù MRL). Sửa cộng tuyến bằng giả-treatment biến thiên theo (sản phẩm×năm) — gán mỗi sản phẩm placebo đường MRL của một sản phẩm thật, lặp ~500 lần (randomization inference). Loại/gắn cờ cao su (≈94% trong phạm vi EUDR). → Đạt: hệ số placebo không có ý nghĩa → hiệu ứng đặc thù MRL.

- [ ] Test mở rộng thị trường — nhập khẩu EU từ TOÀN THẾ GIỚI theo (k,t). Phân định "xúc tác/mở rộng cầu" với "chỉ tái phân bổ". Cần extract BACI mới (EU từ thế giới). → Đạt: kết luận được về kênh cầu vs tái phân bổ, khớp với headline barrier-vs-catalyst.

### GIAI ĐOẠN 4 — Độ lớn & cách báo cáo (tránh bị chê "implausible")

(Bằng chứng: thư mục 10