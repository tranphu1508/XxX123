# Round 007 — GPT repo check on `57f0722`

## Verdict

The latest pushed repo is materially improved and the main `TRADE_COVERAGE_PRIMARY` concordance is close to usable. I do **not** see the previous P0 data blockers (`Durians`, `Pumpkin seeds`, `Strawberries`, `Potatoes`) remaining in `concordance_release_long.csv`.

However, I do **not** recommend declaring the repo final yet. The remaining issues are mostly governance/pipeline consistency, plus one small mapping/policy consistency item.

## What is fixed

1. `concordance_release_long.csv` now includes terminal commodities that had been accidentally excluded:
   - `0163100 Durians -> 081060`
   - `0401100 Pumpkin seeds -> 120799`
   - `0152000 Strawberries -> 081010`
   - `0211000 Potatoes -> 070110;070190`
   - `0234000 Sweet corn -> 070999`
   - `0244000 Kohlrabies -> 070490`
   - `0254000 Watercresses -> 070999`
   - `0253000 Grape leaves -> 070999`
   - `0255000 Witloofs/Belgian endives -> 070521`

2. Trade-coverage policy is now reflected in the release:
   - Nuts: in-shell + shelled for major tree nuts.
   - Spices: whole + crushed/ground for most spices with paired HS2012 codes.
   - Rice: includes paddy, husked, milled, broken.
   - Coffee: green/not-roasted only.
   - Hops: 121010 only.
   - Cherry: 080929 parent-only.
   - Coconut: 080119 + 080112 + 080111.
   - Cinnamon: 090619 + 090611 + 090620.

3. `concordance_final_asean.csv` has `release_policy` and `release_reason`.

4. `build_release_long.py` and `validate_release_long.py` are self-contained within `concordance_review_package`.

5. Literature artifacts are present:
   - `reviews/literature_inventory.csv`
   - `reviews/literature_policy_matrix.csv`
   - `reviews/round_006_cowork_literature_synthesis.md`

## Remaining issues

### P1 — update audit logs

`ROUND_LOG.md` currently stops at Round 005. It does not yet record Round 006, even though the latest commit message says Round 6 is complete.

`agent_rounds_log.csv` currently stops at Round 004. It does not include Round 005 or Round 006.

Required fix:
- Add Round 006 to `ROUND_LOG.md`.
- Add Round 005 and Round 006 to `agent_rounds_log.csv`.

### P1 — update adjudication statuses

`adjudication_decisions.csv` still has many rows marked as `fix_proposed`, `USER pending`, or `cowork/USER pending`, even though the current release appears to have implemented them. Examples:
- coconut
- cinnamon
- potatoes
- strawberries
- sweet corn
- cashew
- nuts
- spices
- coffee
- hops
- cherry

Required fix:
- Add explicit final rows or revise statuses to `accepted_applied`.
- Include `applied_commit = 57f0722` if adding a new column is acceptable.

### P1 — allspice/pimento coverage consistency

Current `release_long` has:

```csv
0820010 Allspice/pimento -> 090421
```

Under the adopted spices policy, Capsicum/Pimenta products should generally include both whole and crushed/ground codes when HS2012 provides paired codes. HS2012 has:

```text
090421 = fruits of Capsicum or Pimenta, dried, neither crushed nor ground
090422 = fruits of Capsicum or Pimenta, crushed or ground
```

Recommended action:
- Add `090422` for `0820010 Allspice/pimento`, or document why allspice is deliberately whole-only.
- This is P1, not P0, because `090421` itself is not wrong.

### P1 — validator still heuristic

`validate_release_long.py` now catches some `EXPORT_CHILDREN_ONLY` misfires by checking whether `eu_code` ends in `000`. This catches prior cases like durian/pumpkin, but it remains a heuristic. It may miss terminal commodity rows whose EU code does end in `000`.

Recommended action:
- Replace the suffix heuristic with an explicit check:
  - a row may be `EXPORT_CHILDREN_ONLY` only if there are actual child rows in `concordance_final_asean.csv` that are exported.
  - do not infer from `eu_code` suffix or from Annex subitems alone.

### P2 — literature synthesis cleanup

`round_006_cowork_literature_synthesis.md` first says Nguyen 2026 should be downloaded, then later says Nguyen 2026 was read and is decisive. This is likely because the file was appended after the fulltext was obtained.

Recommended action:
- Clean the section title so it no longer says Nguyen is still pending.
- Add page/section references to the quote matrix where possible, not only short excerpts.

### P2 — missing CORE_RAC_ONLY output

The repo now justifies `TRADE_COVERAGE_PRIMARY` as the main release. That is fine. But the robustness file promised in the logs is not present yet.

Recommended action:
- Add `data/concordance_release_core_rac_only.csv`, or explicitly mark it as planned for estimation-stage robustness.

## Suggested final acceptance condition

Do not call this repo final until:

1. `validate_release_long.py` passes.
2. `adjudication_decisions.csv` statuses are updated.
3. `ROUND_LOG.md` and `agent_rounds_log.csv` include Round 006.
4. `0820010 Allspice/pimento` is adjudicated for `090422`.
5. The terminal-commodity validator no longer depends only on EU-code suffix.
6. The literature synthesis is cleaned so it has no obsolete “please download Nguyen” wording.

After these are fixed, the main `TRADE_COVERAGE_PRIMARY` release can be treated as substantially ready for estimation.
