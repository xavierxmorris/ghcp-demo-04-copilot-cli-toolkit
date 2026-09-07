# Demo 04 — Copilot CLI Toolkit 💻

> **Difficulty:** ⭐⭐⭐
> **GHCP surface:** **GitHub Copilot CLI** — the terminal agent (`copilot`).
> **Stack:** Python + Bash + `gh` CLI (works on macOS / Linux / Windows / WSL)
> **Time:** ~30 minutes

This demo gets you out of the IDE and into the terminal. The GitHub Copilot CLI
is an **agentic** assistant: it can plan, run shell commands (with your
approval), edit files, and call MCP tools.

This repo is intentionally a little messy — you'll use Copilot CLI to **clean
it up, write a script from scratch, refactor a function, and bulk-rename files**.

**Go deeper:** [WORKSHOP.md](WORKSHOP.md) adds a permission-aware lab,
byte-level dry-run checks, a log-analysis answer key, failure drills, and
safe reset guidance. Commands and session guidance were checked with
**Copilot CLI 1.0.84-1 on 7 September 2026**; use `/help` for your build.

---

## What you'll learn
1. Installing & authenticating the GitHub Copilot CLI.
2. The single-shot prompt vs the interactive `copilot` REPL.
3. Letting Copilot run commands safely (allow / allow-once / deny).
4. Using Copilot CLI for **multi-step refactors** that span several files.
5. When the CLI beats the IDE (CI scripts, log analysis, ops glue).
6. Combining `gh` + `copilot` for everyday GitHub chores.

## Prerequisites

```bash
# 1. The official GitHub CLI (already on this machine for most devs)
gh --version

# 2. Install the Copilot CLI (one-time)
npm install -g @github/copilot   # or: brew install --cask github-copilot-cli

# 3. Sign in (uses your GitHub Copilot subscription)
copilot   # the first run walks you through device-code auth
```

> Don't have a Copilot subscription? A free / trial seat is enough.

## Setup
```bash
git clone https://github.com/xavierxmorris/ghcp-demo-04-copilot-cli-toolkit.git
cd ghcp-demo-04-copilot-cli-toolkit
```

The repo has a few intentionally rough scripts under `scripts/` and a sample
log file under `logs/`.

---

## Scenario 1 — One-shot answer ("how do I…?")

Use the `-p` flag for a single prompt, no REPL:

```bash
copilot -p "Explain how to list local branches already merged into main. Do not execute commands, delete branches, or modify files."
```

Review the proposed command and explanation. `-p` selects programmatic mode,
not a read-only sandbox: permissions still determine what tools can run.

🎯 **Lesson:** Treat single-shot Copilot CLI as "Stack Overflow for the
current millisecond" — context-aware, with citations to the commands.

---

## Scenario 2 — Interactive REPL for multi-step work

```bash
copilot
```

Then, inside the REPL:

```
> Inspect scripts/csv_normaliser.py, then add a --dry-run flag that prints what
  would change without writing anything. Run the test fixture in fixtures/in.csv
  to verify.
```

What happens:
1. Copilot reads `scripts/csv_normaliser.py` within the trusted workspace.
2. Inspect the proposed change with the diff view or `/diff`.
3. Wants to run `python scripts/csv_normaliser.py --dry-run fixtures/in.csv`.
   Choose **allow once** or **allow always for this command**.
4. Reports results.

🎯 **Lesson:** The CLI is a **conversational, tool-using agent**. You stay in
control via the permission prompts — you can audit every command before it
runs.

---

## Scenario 3 — Refactor across multiple files

Inside the REPL:

```
> Across scripts/, replace diagnostic `print(...)` calls with `log.info(...)`
  from a new module `scripts/loglib.py` that wraps the stdlib logging module
  with a sensible format. Preserve CSV and generated log records as data on
  stdout; send diagnostics to stderr. Don't break the existing CLIs.
```

✅ Watch Copilot:
- Create `scripts/loglib.py`.
- Distinguish data output from diagnostics before editing either script.
- Check fixture output as well as CLI behavior. The starter does not yet
  implement argparse or a `--help` option.

🎯 **Lesson:** Cross-file refactors in the CLI are great when the change is
**mechanical but pervasive** — exactly where IDE refactor tools fall short
because they only understand syntax, not intent.

---

## Scenario 4 — Log triage

Inside the REPL:

```
> Read logs/app.log and tell me: which user IDs hit the most 5xx errors,
  what endpoints are involved, and what is the most likely root cause?
  Show me your evidence (line numbers).
```

Require a citation-backed summary and verify the counts. This log contains
status codes and endpoints, not enough evidence to establish a root cause.
Any explanation of *why* checkout failed must be labelled a hypothesis.

🎯 **Lesson:** Log spelunking is repetitive command-fu (grep, awk, sort,
uniq -c, sort -nr…). The CLI is excellent at this and remembers what it
already learned.

---

## Scenario 5 — GitHub housekeeping (with `gh`)

```
> Use the gh CLI to list my 5 oldest open PRs in this org that haven't had
  activity in 30 days. For each one, draft a polite nudge comment I can review
  before posting.
```

Copilot will run `gh pr list … --json …`, parse it, and draft comments. You
approve each `gh pr comment` call individually.

🎯 **Lesson:** `gh` + `copilot` is the modern "ops glue" combo — automate the
admin work that doesn't deserve a real script.

---

## Scenario 6 — Generating a fresh script from a prompt

Quit the REPL. Then:

```bash
copilot
```

Ask it to draft `scripts/bulk_rename.py` with a dry-run mode, a refusal to
overwrite existing targets, and tests in a temporary directory. Review the
write and execution permissions interactively. Do not point a first run at
your photo library.

---

## Transcripts

See `transcripts/` for **archived, illustrative walkthroughs**. Their UI and
sample output are not a current command reference or a golden fixture.
For example, the current CSV script trims/lowercases headers but does not
replace interior spaces or lowercase email values.

## Try it yourself

1. Have Copilot CLI **bisect** a flaky test in any of your other demos.
2. Ask: *"Find every hard-coded API key pattern in this repo and tell me where
   to move them."* (Then verify with `gitleaks` or similar.)
3. Pipe data in: `cat logs/app.log | copilot -p "summarise the top 3 issues"`.
4. Have Copilot write a **PowerShell** version of a Bash script you have — the
   CLI handles cross-platform translation well.

## Talking points
- The CLI has access to your **whole shell** — that's powerful and dangerous.
  Use a clean working directory; review every command; never blanket-allow.
- Sessions can be resumed; use `/resume` and `/session`. Keep unrelated tasks
  in separate sessions and record important decisions in repository artifacts.
- Pair the CLI with **shell aliases** (e.g., `alias ?='copilot -p'`) to lower
  the friction of one-shot questions.
- The Copilot CLI honours the same content-exclusion and policy controls as
  the IDE — Enterprise / Business admins can configure both centrally.

## Next demo →
[Demo 05 — Customising Copilot with AGENTS.md](https://github.com/xavierxmorris/ghcp-demo-05-agents-md-customization)
— teach Copilot your conventions so it stops fighting your style guide.
