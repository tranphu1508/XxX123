# Đối chiếu 15+ mã VN với Annex I PHÁP LÝ (ground truth) — 2026-06-26

> Nguồn ground-truth: **Reg (EU) 2018/62** (thay Annex I của Reg 396/2005), bản nguyên văn EUR-Lex CELEX 32018R0062, người dùng cung cấp. Mạnh hơn catalogue máy-đọc vì là **văn bản pháp lý** với cấu trúc sub-entry `mã-NNN | loài | tên khoa học`. Áp quy tắc bằng chứng nguyên văn: mỗi mã VN dán **dòng Annex I nguyên văn**.

## Bước 1 — Đóng băng
- File: `01_raw_data_frozen/eu_annex1_legal/L_2018018EN.01000101.xml.html` (read-only).
- SHA-256: `c4cb8987f2d7c7e604b5de87fde24ce2bae47e98baaabe1c7c8c37f295de578f`
- Provenance đã ghi `data_sources_and_provenance.md` (CELEX 32018R0062, vai trò = ground-truth pháp lý mã sản phẩm EU).

## Bước 2 — Parse → bảng tra loài→mã
- Script bóc XHTML EUR-Lex (`oj-tbl-cod`/`oj-tbl-txt`/`oj-italic`), gộp 2 bảng (overview + chi tiết), bắt cả sub-code nằm trong ô txt.
- Output: `01_.../eu_annex1_legal/annex1_species_to_code.csv` — **381 nhóm mẹ + 924 sub-entry** (mọi mã, dùng lại cho ASEAN).

## Bước 3 — Đối chiếu 17 mã VN lá × Annex I (dòng nguyên văn)

**KẾT QUẢ: 17/17 KHỚP. KHÔNG mã nào sai loài/sai nhóm.**

| # | Mã VN | Sản phẩm VN | Dòng Annex I NGUYÊN VĂN | Khớp |
|---|---|---|---|---|
| 1 | 0110010 | Bưởi/pomelo | grp `0110010 Grapefruits` (Citrus paradisi); **`0110010-002 Shaddocks/pomelos \| Citrus maxima ; syn: Citrus grandis`** | ✅ (pomelo = sub-002) |
| 2 | 0110020 | Cam | `0110020 Oranges \| Citrus sinensis` | ✅ |
| 3 | 0110030 | Chanh | `0110030 Lemons \| Citrus limon` | ✅ |
| 4 | 0110050 | Quýt | `0110050 Mandarins \| Citrus reticulata ; syn: Citrus deliciosa` | ✅ |
| 5 | 0231020 | Ớt cay | grp `0231020 Sweet peppers/bell peppers` (Capsicum annuum); **`0231020-001 Chili peppers \| Capsicum annuum var. annuum; C. baccatum; C. chinense; C. frutescens; C. pubescens`** | ✅ (chili = sub-001) |
| 6 | 0231040 | Đậu bắp | `0231040 Okra/lady's fingers \| Abelmoschus esculentus` (không sub) | ✅ |
| 7 | 0162020 | Vải (+nhãn) | grp `0162020 Litchis/lychees \| Litchi chinensis` (=vải); **`0162020-001 Longans \| Dimocarpus longan`** (=nhãn) | ✅ |
| 8 | 0162030 | Chanh leo | `0162030 Passionfruits/maracujas \| Passiflora edulis ; syn: Passiflora laurifolia` | ✅ |
| 9 | 0162040 | **Thanh long** | grp `0162040 Prickly pears/cactus fruits` (Opuntia ficus-indica); **`0162040-001 Pitayas/dragon fruits \| Hylocereus undatus`** | ✅ |
| 10 | 0163030 | Xoài | `0163030 Mangoes \| Mangifera indica` (không sub) | ✅ |
| 11 | 0163060 | **Chôm chôm** | grp `0163060 Cherimoyas` (Annona cherimola); **`0163060-006 Rambutans/hairy litchis \| Nephelium lappaceum`** | ✅ XÁC NHẬN tách khỏi 0162020 |
| 12 | 0163100 | Sầu riêng | `0163100 Durians \| Durio zibethinus` (không sub) | ✅ |
| 13 | 0500060 | Gạo | `0500060 Rice \| Oryza sativa` (sub là African/wild rice) | ✅ |
| 14 | 0620000 | Cà phê | `0620000 Coffee beans \| Coffea arabica; Coffea canephora ; syn: Coffea robusta; Coffea liberica` | ✅ |
| 15 | 0610000 | Chè | `0610000 Teas \| Camellia sinensis` (không sub) | ✅ |
| 16 | 0256040 | Parsley | grp `0256040 Parsley \| Petroselinum crispum`; sub `0256040-001 Root parsley leaves` | ✅ |
| 17 | 0256080 | Basil/rau thơm | grp `0256080 Basil and edible flowers \| Ocimum basilicum`; gồm `‑025 Vietnamese mint \| Persicaria odorata`, `‑024 Thai basil`, `‑022 Rice paddy herb/phak ka yaeng`, `‑013 Lizard tail/dap ca` | ✅ |

### Bốn điểm prompt yêu cầu — XÁC NHẬN nguyên văn
- **Thanh long** → `0162040-001 Pitayas/dragon fruits | Hylocereus undatus` ✅ (mã mẹ 0162040 Prickly pears/cactus fruits)
- **Rambutan** → `0163060-006 Rambutans/hairy litchis | Nephelium lappaceum` ✅ (mã mẹ 0163060 Cherimoyas) → **XÁC NHẬN tách khỏi 0162020** (Bước 0 trước đúng)
- **Longan** → `0162020-001 Longans | Dimocarpus longan` ✅
- **Ớt cay** → `0231020-001 Chili peppers` (Capsicum spp.) ✅ — KHÁC: prompt nói "mã mẹ 0231020 Sweet peppers" → đúng, chili là sub-001.

### Phát hiện phụ (lệch nhỏ — không phải lỗi concordance, chỉ tinh chỉnh)
- **Bưởi VN = pomelo** chính xác là sub `0110010-002 Shaddocks/pomelos` (*Citrus maxima*), KHÔNG phải grapefruit thật (*Citrus paradisi*, mã mẹ). HS6 080540 vẫn đúng (gồm cả pomelo). MRL: pomelo dùng MRL nhóm 0110010 (sub không có MRL riêng). → giữ 0110010, ghi rõ pomelo=sub-002.
- **Herbs:** concordance dùng mã nhóm `0256000`; Annex I tách parsley=0256040, basil=0256080. → annex1_legal_ref ghi cả nhóm mẹ + 2 lá.

## Bước 4 — Gắn cột `annex1_legal_ref`
Đã thêm cột `annex1_legal_ref` vào `concordance_final_vn_2026-06-26.csv` (27 dòng) — mỗi dòng có mã sub-entry Annex I pháp lý. Concordance nay có **nguồn pháp lý**, không chỉ catalogue. (Backup `.bak_before_annex1ref_2026-06-27`.)

## DỪNG
17/17 mã VN khớp Annex I pháp lý — **không lệch nghiêm trọng** (thanh long/ớt/gạo đều khớp). Chỉ tinh chỉnh ghi chú (pomelo=sub-002, herbs leaf codes). Chờ Claude đọc đối chiếu.
