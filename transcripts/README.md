# Annotated Copilot CLI Transcripts

This folder holds **archived, annotated examples** of each scenario so you can
preview the interaction before running it yourself. They are not an executable
baseline or a current CLI reference. Use `/help` for current controls and
compare actual output against the scripts and fixtures in this repository.

Files:
- `01-one-shot.md` — single `-p` prompt.
- `02-repl-multistep.md` — interactive REPL adding a `--dry-run` flag.
- `03-refactor.md` — cross-file `print` → `log.info` refactor.
- `04-log-triage.md` — analysing `logs/app.log`.

Transcripts are illustrative; your exact output will differ.
In particular, the CSV examples show transformations not performed by the
starter, such as `first name` becoming `first_name` and email values becoming
lowercase. The workshop preserves the starter's actual contract unless a
separate change is requested.
