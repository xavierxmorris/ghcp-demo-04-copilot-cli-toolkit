#!/usr/bin/env python3
"""Normalise a CSV: trim whitespace, lower-case headers, drop blank rows.

Intentionally lacks a --dry-run flag. The Copilot CLI demo adds it.
"""
import csv
import sys
from pathlib import Path


def normalise(in_path: Path, out_path: Path) -> int:
    with in_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [r for r in reader if any(cell.strip() for cell in r)]
    if not rows:
        print("input was empty")
        return 0
    rows[0] = [h.strip().lower() for h in rows[0]]
    rows[1:] = [[c.strip() for c in r] for r in rows[1:]]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
    print(f"wrote {len(rows) - 1} rows to {out_path}")
    return len(rows) - 1


def main(argv):
    if len(argv) < 2:
        print("usage: csv_normaliser.py <input.csv> [output.csv]")
        return 1
    in_path = Path(argv[1])
    out_path = Path(argv[2]) if len(argv) > 2 else in_path.with_suffix(".clean.csv")
    normalise(in_path, out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
