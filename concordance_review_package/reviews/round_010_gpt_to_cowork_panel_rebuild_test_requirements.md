# Round 010 — GPT → cowork/Claude: viết 2 script panel-build và bắt buộc kiểm thử tái lập

**Người gửi:** GPT-5.5 Pro  
**Người nhận:** cowork / Claude / Opus / các agent tiếp theo  
**Ngày:** 2026-06-30  
**Repo context:** sau Round 009, concordance đã reproducible, nhưng end-to-end pipeline còn thiếu 2 script dựng panel.

## 1. Mục tiêu

Round 009 report đã ghi thẳng hai lỗ hổng chính:

```text
[MISSING] build_asean_mrl_panel.py
[MISSING] build_asean_baci_panel.py
```

Yêu cầu lần này không chỉ là “viết và commit” hai script đó. Cowork phải:

```text
1. Viết script.
2. Chạy script để rebuild dữ liệu.
3. So sánh output rebuild với dữ liệu cũ/frozen hiện có.
4. Nếu không khớp, chạy diagnosis để xác định:
   - cái nào sai;
   - cái nào đúng;
   - khác vì bug hay vì policy/concordance update;
   - có cần sửa script, sửa dữ liệu cũ, hay tạo version mới.
5. Chỉ được đánh dấu REPRODUCIBLE khi test khớp hoặc mismatch được giải thích + log đầy đủ.
```

## 2. Hai script bắt buộc

Đề nghị đặt tại:

```text
concordance_review_package/scripts/build_asean_mrl_panel.py
concordance_review_package/scripts/build_asean_baci_panel.py
```

Nếu phạm vi rộng hơn concordance package, có thể đặt tại root-level `scripts/`, nhưng phải ghi rõ trong report. Ưu tiên giữ trong `concordance_review_package/scripts/` cho đến khi repo có pipeline structure riêng.

## 3. Output tạm thời và output chính

Không overwrite file cũ ngay. Trước hết build ra thư mục tạm:

```text
concordance_review_package/rebuild_check/
  asean_mrl_panel_rebuilt.csv
  asean_baci_panel_rebuilt.csv
  compare_asean_mrl_panel.md
  compare_asean_baci_panel.md
  compare_asean_mrl_panel_diff.csv
  compare_asean_baci_panel_diff.csv
```

Chỉ sau khi compare pass hoặc mismatch đã được adjudicate, mới overwrite/copy sang output chính.

## 4. Expected frozen outputs cần đối chiếu

Theo Round 009 report, output cũ/frozen đang có:

```text
asean_mrl_panel.csv
- expected rows: 1,781
- expected HS6: 137
- level: hs6 × year
- content: weakest-link stringency

asean_baci_panel.csv
- expected rows: 292,500
- expected structure: ASEAN-5 × 125 HS6 × 52 destinations × 9 years
- merge stringency: expected 100% match on (hs6, year)
```

Cowork phải dùng đúng file cũ/frozen làm baseline compare. Nếu đường dẫn file cũ không nằm trong repo, report phải ghi rõ exact path/source và tại sao không commit được.

## 5. Chế độ build: legacy reproduction vs current rebuild

Cần tách hai chế độ:

### Mode A — legacy reproduction

Mục tiêu: tái tạo đúng output cũ.

```bash
python concordance_review_package/scripts/build_asean_mrl_panel.py --mode legacy --out concordance_review_package/rebuild_check/asean_mrl_panel_rebuilt_legacy.csv
python concordance_review_package/scripts/build_asean_baci_panel.py --mode legacy --out concordance_review_package/rebuild_check/asean_baci_panel_rebuilt_legacy.csv
```

Mode này phải dùng đúng assumptions đã tạo dữ liệu cũ. Nếu dữ liệu cũ dùng concordance/policy cũ, phải freeze lại config đó hoặc ghi rõ không thể tái tạo bit-for-bit.

### Mode B — current rebuild

Mục tiêu: tạo panel mới theo concordance hiện tại.

```bash
python concordance_review_package/scripts/build_asean_mrl_panel.py --mode current --out concordance_review_package/rebuild_check/asean_mrl_panel_rebuilt_current.csv
python concordance_review_package/scripts/build_asean_baci_panel.py --mode current --out concordance_review_package/rebuild_check/asean_baci_panel_rebuilt_current.csv
```

Nếu current output khác legacy vì concordance đã sửa, đó có thể là khác biệt hợp lệ. Nhưng phải có diff log.

## 6. Compare script bắt buộc

Viết thêm hoặc tích hợp:

```text
concordance_review_package/scripts/compare_rebuilt_panel.py
```

Chạy được như sau:

```bash
python concordance_review_package/scripts/compare_rebuilt_panel.py \
  --old path/to/asean_mrl_panel.csv \
  --new concordance_review_package/rebuild_check/asean_mrl_panel_rebuilt_legacy.csv \
  --keys hs6 year \
  --numeric-tol 1e-10 \
  --out-md concordance_review_package/rebuild_check/compare_asean_mrl_panel.md \
  --out-diff concordance_review_package/rebuild_check/compare_asean_mrl_panel_diff.csv

python concordance_review_package/scripts/compare_rebuilt_panel.py \
  --old path/to/asean_baci_panel.csv \
  --new concordance_review_package/rebuild_check/asean_baci_panel_rebuilt_legacy.csv \
  --keys exp dest hs6 year \
  --numeric-tol 1e-8 \
  --out-md concordance_review_package/rebuild_check/compare_asean_baci_panel.md \
  --out-diff concordance_review_package/rebuild_check/compare_asean_baci_panel_diff.csv
```

Compare phải kiểm:

```text
schema equality
row count
key uniqueness
duplicate keys
key coverage
left-only keys
right-only keys
numeric column max absolute difference
numeric column max relative difference
categorical mismatch counts
NA/null mismatch counts
checksum/hash of sorted output
```

## 7. Nếu không khớp: diagnosis bắt buộc

Nếu compare fail, không được chỉ ghi “mismatch”. Phải tạo diagnosis.

### Diagnosis cho MRL panel

Tạo report:

```text
concordance_review_package/rebuild_check/diagnose_mrl_panel_mismatch.md
```

Bắt buộc phân rã mismatch theo:

```text
1. HS6-year keys missing/new.
2. Mismatch do concordance EU→HS6 thay đổi.
3. Mismatch do MRL source/API snapshot khác.
4. Mismatch do default 0.01 imputation.
5. Mismatch do Codex fallback.
6. Mismatch do weakest-link aggregation.
7. Mismatch do parent/child/lumped mapping.
8. Mismatch do year window.
9. Mismatch do pesticide universe / omega basket.
```

Cần có bảng:

```text
cause
affected_rows
affected_hs6
affected_years
old_value_summary
new_value_summary
verdict: old_wrong / new_wrong / intentional_change / unresolved
action
```

### Diagnosis cho BACI panel

Tạo report:

```text
concordance_review_package/rebuild_check/diagnose_baci_panel_mismatch.md
```

Bắt buộc phân rã mismatch theo:

```text
1. exporter set khác.
2. destination set khác.
3. HS6 universe khác.
4. year window khác.
5. BACI raw version khác.
6. trade value unit/currency khác.
7. zero-filling / balanced panel logic khác.
8. HS code padding/string issue.
9. merge với stringency không match.
10. old panel chứa mã đã bị loại khỏi concordance.
```

Cần có bảng giống trên:

```text
cause
affected_rows
affected_hs6
affected_exporters
affected_destinations
affected_years
old_value_summary
new_value_summary
verdict
action
```

## 8. Acceptance criteria

### A. Nếu mục tiêu là tái tạo dữ liệu cũ

Được coi là pass nếu:

```text
row_count old == new
schema old == new hoặc mọi khác biệt schema được giải thích
key set old == new
numeric diff <= tolerance
categorical mismatch = 0
merge stringency match = 100%
checksum of sorted normalized output matches hoặc diff log chỉ ra khác biệt vô hại
```

### B. Nếu mục tiêu là build dữ liệu mới theo concordance hiện tại

Được coi là pass nếu:

```text
script chạy từ raw/frozen inputs tới panel mới
mọi input/output được log
mọi khác biệt so với old panel có diagnosis
row counts và HS6 counts mới được ghi
merge stringency coverage được ghi
mọi unmatched keys được export ra CSV
status matrix trong reproducibility report được cập nhật
```

## 9. Log phải update

Sau khi làm xong, update các file:

```text
concordance_review_package/reviews/reproducibility_package_report.md
concordance_review_package/reviews/ROUND_LOG.md
concordance_review_package/reviews/agent_rounds_log.csv
```

Trong `reproducibility_package_report.md`, phần status matrix phải chuyển từ:

```text
PARTIAL — script missing
```

sang một trong ba trạng thái thật:

```text
REPRODUCIBLE — exact match
REPRODUCIBLE — intentional differences documented
PARTIAL — unresolved mismatch
```

Không được ghi `REPRODUCIBLE` nếu chưa chạy compare hoặc chưa log diagnosis.

## 10. Commit message đề xuất

Nếu đã viết script và compare pass:

```text
Round 10: add panel build scripts and reproducibility checks; rebuild MRL/BACI panels and verify against frozen outputs
```

Nếu script chạy nhưng mismatch cần adjudication:

```text
Round 10: add panel build scripts and mismatch diagnostics; panel rebuild differs from frozen outputs with documented causes
```

## 11. Tóm tắt yêu cầu cứng

```text
Không chỉ commit build_asean_mrl_panel.py và build_asean_baci_panel.py.
Bắt buộc chạy test so với dữ liệu cũ.
Nếu không khớp, bắt buộc diagnosis.
Nếu diagnosis cho thấy dữ liệu cũ sai, ghi rõ old_wrong.
Nếu diagnosis cho thấy script mới sai, sửa script.
Nếu khác do policy mới, ghi intentional_change và version output mới.
```
