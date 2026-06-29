#!/usr/bin/env python3
"""
Validation helpers for EU Annex I -> HS2012 concordance.

Place this file in:
  concordance_review_package/scripts/validate_gpt_concordance_rules.py

Run from repo root:
  python concordance_review_package/scripts/validate_gpt_concordance_rules.py

This script intentionally performs structural checks only. It does not auto-apply
GPT row proposals; adjudicated changes should be made through PR review.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path("concordance_review_package")
DATA = ROOT / "data" / "concordance_final_asean.csv"
HS = ROOT / "sources" / "product_codes_HS12_V202601.csv"

GROUP_SUFFIX = "0000"

def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]

def split_hs6(field: str) -> list[str]:
    field = (field or "").strip()
    if not field or field.lower() == "nan":
        return []
    return [x.strip() for x in re.split(r"[;\s,]+", field) if x.strip()]

def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    rows = read_csv(DATA)
    hs_rows = read_csv(HS)
    valid_hs = {r["code"].zfill(6) for r in hs_rows if r.get("code")}

    for i, r in enumerate(rows, start=2):
        eu_code = r.get("eu_code", "")
        hs6_field = r.get("hs6", "")
        status = r.get("phase2_status", "")
        needs_review = r.get("needs_review", "")
        excluded_nonfood = r.get("excluded_nonfood", "")
        hs6_lumped = r.get("hs6_lumped", "")

        if hs6_field.lower() == "nan":
            errors.append(f"row {i} eu_code={eu_code}: hs6 is literal 'nan'; use empty string.")

        codes = split_hs6(hs6_field)

        for code in codes:
            if not re.fullmatch(r"\d{6}", code):
                errors.append(f"row {i} eu_code={eu_code}: invalid HS6 token {code!r}.")
            elif code not in valid_hs:
                errors.append(f"row {i} eu_code={eu_code}: HS6 not found in HS2012 source: {code}.")

        if needs_review == "NO_HS6" and codes:
            errors.append(f"row {i} eu_code={eu_code}: needs_review=NO_HS6 but hs6 is populated.")

        if ("excluded_nec" in status or excluded_nonfood) and codes:
            warnings.append(f"row {i} eu_code={eu_code}: excluded row has hs6; ensure build_release filters it out.")

        if ";" in hs6_field:
            warnings.append(f"row {i} eu_code={eu_code}: multi-HS field; release_long must explode this.")

        if eu_code.endswith(GROUP_SUFFIX) and codes:
            warnings.append(f"row {i} eu_code={eu_code}: group heading has hs6; release_long should generally use child rows only.")

        # stale lumped metadata check: if hs6_lumped names a target code not equal to current hs6 tokens
        m = re.search(r"→(\d{6})", hs6_lumped)
        if m and codes and m.group(1) not in codes:
            warnings.append(
                f"row {i} eu_code={eu_code}: hs6_lumped appears stale ({m.group(1)} not in current hs6 {codes})."
            )

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print("  -", w)

    if errors:
        print("\nERRORS:")
        for e in errors:
            print("  -", e)
        return 1

    print("OK: structural concordance checks passed. Review warnings before release.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
