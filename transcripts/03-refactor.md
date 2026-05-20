# Transcript — Scenario 3 (cross-file refactor)

```text
> Across scripts/, replace every use of print(...) with log.info(...) calls
  from a new module scripts/loglib.py that wraps stdlib logging.

▌ Plan:
   1. Create scripts/loglib.py with a get_logger(name) helper.
   2. Edit every script under scripts/ to import and use it.
   3. Validate by running `python scripts/csv_normaliser.py --help` and
      `python scripts/seed_logs.py 3`.

  ✓ created scripts/loglib.py
  ✓ patched scripts/csv_normaliser.py  (3 replacements)
  ✓ patched scripts/seed_logs.py       (0 replacements — uses sys.stdout)
        ↑ skipped: this script intentionally pipes to stdout for tooling.

  Run smoke checks? (y/N) y
  ✓ csv_normaliser.py --help                exit 0
  ✓ seed_logs.py 3                          exit 0

  All green. Want me to commit the change? (y/N) N
```
