# Transcript — Scenario 2 (interactive REPL, multi-step)

```text
$ copilot
GitHub Copilot CLI — type /help for commands. Exit with /quit.

> Inspect scripts/csv_normaliser.py, then add a --dry-run flag that prints
  what would change without writing anything. Run it against fixtures/in.csv.

▌ Reading scripts/csv_normaliser.py … (allow once)
  (read 38 lines)

▌ Plan:
   1. Add `--dry-run` to argparse.
   2. In `normalise()`, when dry-run is set, build the rows but write to
      stdout instead of the output file.
   3. Run `python scripts/csv_normaliser.py --dry-run fixtures/in.csv`.

  Apply edits to scripts/csv_normaliser.py? (review / yes / no) review

  --- diff ---
  - def main(argv):
  -     if len(argv) < 2:
  -         print("usage: csv_normaliser.py <input.csv> [output.csv]")
  ...
  + import argparse
  + def main(argv):
  +     p = argparse.ArgumentParser()
  +     p.add_argument("input")
  +     p.add_argument("output", nargs="?")
  +     p.add_argument("--dry-run", action="store_true")
  ...

  Apply? (y/N) y
  ✓ wrote scripts/csv_normaliser.py

▌ Run python scripts/csv_normaliser.py --dry-run fixtures/in.csv ? (y/N) y
  first_name,last_name,email,signup_date
  ada,Lovelace,ada@example.com,2024-01-02
  linus,torvalds,linus@example.com,2024-02-03
  ...
  ✓ dry-run produced 4 normalised rows (file not modified)

> /quit
```
