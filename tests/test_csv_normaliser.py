"""Exercise the existing offline CLI; dry-run remains a workshop exercise."""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "csv_normaliser.py"


class CsvNormaliserTests(unittest.TestCase):
    def test_fixture_is_normalised_without_modifying_input(self) -> None:
        source = ROOT / "fixtures" / "in.csv"
        original = source.read_bytes()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "clean.csv"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(source), str(output)],
                check=True, capture_output=True, text=True, timeout=10,
            )
            with output.open(encoding="utf-8", newline="") as stream:
                rows = list(csv.reader(stream))
            self.assertEqual(rows, [
                ["first name", "last_name", "email", "signup_date"],
                ["ada", "Lovelace", "ADA@example.com", "2024-01-02"],
                ["linus", "torvalds", "linus@example.com", "2024-02-03"],
                ["grace", "hopper", "grace@example.com", "2024-03-04"],
                ["margaret", "hamilton", "margaret@EXAMPLE.com", "2024-04-05"],
            ])
            self.assertIn("wrote 4 rows", result.stdout)
        self.assertEqual(source.read_bytes(), original)

    def test_empty_input_creates_no_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "empty.csv"
            source.write_text("\n  , , \n", encoding="utf-8")
            output = Path(directory) / "clean.csv"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(source), str(output)],
                check=True, capture_output=True, text=True, timeout=10,
            )
            self.assertIn("input was empty", result.stdout)
            self.assertFalse(output.exists())

    def test_missing_arguments_fail_with_usage(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("usage:", result.stdout)


if __name__ == "__main__":
    unittest.main()
