# Diagnosis — BACI ASEAN-5 panel rebuild vs frozen (Round 010)

**Requirement (GPT Round 010):** rebuild the BACI panel from raw, compare to the frozen `asean_baci_panel.csv`, and diagnose any mismatch. *"Không được ghi REPRODUCIBLE nếu chưa chạy compare hoặc chưa log diagnosis."*

## Build provenance
- **Raw input:** `BACI_HS12_V202601.zip` (SHA-256 `2dd0dd61…`, 1,267,950,839 B — checksum-frozen).
- **Extraction:** `unzip -p … | awk -F',' '$2 ∈ {360,458,608,704,764}'` → ASEAN-5 exporter rows per year → `baci_a5/a5_Y2015.csv … a5_Y2023.csv` (9 files, 5,737,839 rows total).
- **Build script:** `scripts/build_asean_baci_panel.py`. Logic: filter exporter∈ASEAN-5, dest∈52-destination set, hs6∈HS6 universe, year∈window; aggregate `v` over (exp,hs6,dest,year); balance via `itertools.product(ASEAN5 × HS6 × dest × year)` with zero-fill.

## Test 1 — LEGACY mode (reproduce frozen exactly)
HS6 universe = frozen panel's 125 HS6; destinations = frozen's 52; years = 2015–2023.

| Check | Frozen | Rebuilt | Result |
|---|---|---|---|
| Rows | 292,500 | 292,500 | ✅ exact |
| Keys (exp,hs6,dest,year) | — | only-old=0, only-new=0 | ✅ exact |
| Value cells matching (\|diff\|<0.5) | — | 292,500 / 292,500 (100.0%) | ✅ exact |
| max \|diff\| | — | **0.0** | ✅ bit-for-bit |
| Σ value | 204,947,397 | 204,947,397 | ✅ exact |

**Verdict: REPRODUCIBLE — exact (0 difference).** The frozen BACI panel is fully regenerable from frozen raw + script. No mismatch to diagnose.

## Test 2 — CURRENT mode (corrected-concordance HS6 universe)
HS6 universe = current `concordance_release_long.csv` (169 HS6); same 52 dest, 9 years.

| | Frozen (legacy) | Rebuilt (current) |
|---|---|---|
| Rows | 292,500 | 395,460 |
| HS6 | 125 | 169 |

**Difference decomposition (all intentional):**
- **+44 HS6 (125→169):** the corrected concordance + TRADE_COVERAGE policy add dedicated/processed-form codes (shelled nuts, milled rice, crushed spices, green coffee, restored commodity codes, split-out catch-alls). Grounded in EU Reg 396/2005 Art 20 + literature (Nguyen 2026, Drogue 2012, Hejazi 2022) — see `reviews/literature_policy_matrix.csv`.
- **Row count = 5 exp × 169 HS6 × 52 dest × 9 yr − (HS6/year not present)** balanced grid; arithmetic consistent.

**Verdict: intentional_change** — the current panel is a deliberate superset reflecting accepted concordance corrections, not a regression. Legacy mode (Test 1) proves the *machinery* is exact; current mode reflects the *corrected inputs*.

## Files
- `rebuild_check/asean_baci_panel_rebuilt_legacy.csv` (292,500 rows — exact match)
- `rebuild_check/asean_baci_panel_rebuilt_current.csv` (395,460 rows — corrected universe)
- Compare logic: `scripts/compare_rebuilt_panel.py`
