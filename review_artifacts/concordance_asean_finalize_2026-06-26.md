# ASEAN Chặng 1: Un-park + FINALIZE concordance EU→HS6 (phạm vi rau-quả-nông sản) — 2026-06-26

> Un-park 363 `parked_asean` + finalize EU→HS6 cho phạm vi thực phẩm nguồn gốc thực vật rộng. Pháp-lý-hóa chống **Annex I Reg (EU) 2018/62** (đã đóng băng + parse). Quy tắc bằng chứng nguyên văn (mỗi quyết-định-tra-cứu dán dòng Annex I — chính quy tắc bắt lỗi rambutan). Tái dùng sửa-phổ-quát + lát VN. DỪNG sau concordance, chưa panel.

## Bước 1 — Phạm vi (lọc theo nhóm Annex I, KHÔNG theo nước)
| nhóm Annex I | #mã | giữ/loại |
|---|---|---|
| 01 Trái cây (fresh/frozen) + tree nuts | 85 | GIỮ |
| 02 Rau | 115 | GIỮ |
| 03 Đậu/pulses | 6 | GIỮ |
| 04 Hạt có dầu/oil fruits | 24 | GIỮ |
| 05 Ngũ cốc | 11 | GIỮ |
| 06 Chè/cà phê/cacao/thảo mộc | 23 | GIỮ |
| 07 Hoa bia/hops | 1 | GIỮ |
| 08 Gia vị | 41 | GIỮ |
| 09 Cây mía-đường | 5 | GIỮ |
| **TỔNG plant-food** | **311** (→ 304 sau loại 7 n.e.c.) | |
| 10–13 SP động vật | **70** | **LOẠI** (cờ `EXCLUDED_nonfood(animal)`) |

- 7 mã "Others (n.e.c.)" (xxxxx990 catch-all) → `EXCLUDED_nec` (không phải sản phẩm thật).
- **annex1_legal_ref gắn 304/304 mã plant** (mỗi mã có dòng Annex I pháp lý: số + tên + loài).

## Bước 2 — Tự-giải ca rõ (chống Annex I + tái dùng VN)
- **284/304 mã có HS6** (auto): 249 từ phase-2 (verified_high 84 + hs6 present), +18 hạt-dầu/mía (map loài→HS), +13 thảo-mộc-infusion (→1211), + **VN-overlay 16 mã** (authoritative, đã verify pháp lý lát VN).
- Tái dùng sửa-phổ-quát lát VN (melons 0233010→080719, wheat…) + universal_fix (4).

## Bước 3 — Ca KHẢ NGHI (dán dòng Annex I nguyên văn — kiểu rambutan)
| ca | dòng Annex I NGUYÊN VĂN | quyết |
|---|---|---|
| **Thanh long 0162040** | `0162040 Prickly pears/cactus fruits \| Opuntia ficus-indica` + sub `0162040-001 Pitayas/dragon fruits \| Hylocereus undatus` | full_parked cũ **081040 SAI** → **VN-overlay 081090** (đúng pháp lý) |
| **Dâu tây co-name** | quả: `0152000 \| Fragaria × ananassa` (nhóm 0150 berries) **vs** lá: `0632010 Strawberry \| Fragaria × ananassa` (nhóm **0632 'Leaves and aerial green parts'** — lá pha trà) | CÙNG loài, KHÁC bộ phận → **HS6 KHÁC**: quả→081010, **lá→121190** (KHÔNG gộp nhầm) |
| **081090 cluster** | `0162020 Litchis`, `0162030 Passionfruits`, `0162040 Prickly pears`, `0163060 Cherimoyas`… | 6 mã EU CHIA HS6 081090 (tropical n.e.c.) — co-code, khai báo giới hạn nhận diện |

→ Đây chính là loại lỗi quy tắc nguyên văn bắt được (rambutan lát VN; dâu-tây-lá lần này).

## Bước 4 — HS6-gộp (giới hạn nhận diện PHẢI khai báo)
**59 HS6 dùng chung bởi >1 mã EU.** Top:
```
121190 (plants for infusion): 13 mã EU (lá/hoa/rễ thảo mộc pha trà: 0631-0633)
070940 (rau lá khác)        : 11 mã
081040 (berries nhỏ khác)   :  8 mã
070410 (bắp cải)            :  8 mã
090921 (hạt gia vị)         :  7 mã
070970/070920 (rau lá/quả)  :  7/6 mã
081090 (trái nhiệt đới n.e.c): 6 mã (vải/nhãn, chanh leo, thanh long, chôm chôm…)
```
→ Nơi BACI HS6 không tách mịn hơn Annex I — phải khai báo trong bài (đặc biệt 081090 trái nhiệt đới, 121190 thảo mộc).

## needs_review còn lại — 20 mã (đều UMBRELLA GROUP, đúng kỳ vọng)
`0200000 VEGETABLES`, `0500000 CEREALS`, `0800000 SPICES`, `0250000 Leaf vegetables`, `0230000 Fruiting veg`, `0210000 Root/tuber`, `0640000 Cocoa beans`, `0700000 HOPS`, `0290000 Algae`, `0402000 Oil fruits`, `0160000 Misc fruits`, `0639000`… — **mã NHÓM MẸ tổng hợp, KHÔNG map 1 HS6 đơn** (downstream dùng mã lá). Cờ `needs_review`, để Claude xác nhận (không phải lỗi).

## DỪNG
Concordance ASEAN finalized (304 plant, 284 có HS6 + legal ref, 59 lumped, 20 umbrella needs_review, 70 animal + 7 nec excluded). Chờ Claude rà: ca khả nghi (thanh long/dâu-tây-lá) đúng chưa, HS6-gộp ở đâu, 20 umbrella needs_review. (Panel MRL + nhận diện = chặng 2.)
