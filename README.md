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
copilot -p "Show me the git command to delete every local branch already merged into main, but never delete main or develop."
```

✅ Copilot proposes a one-liner *and* explains each flag. You decide whether
to run it.

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
1. Copilot reads `scripts/csv_normaliser.py` (asks permission first time it
   reads a file).
2. Proposes an edit. Press **Tab** to inspect the diff, **Enter** to accept.
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
> Across scripts/, replace every use of `print(...)` with a `log.info(...)` call
  from a new module `scripts/loglib.py` that wraps the stdlib logging module
  with a sensible format. Don't break the existing CLIs.
```

✅ Watch Copilot:
- Create `scripts/loglib.py`.
- Open each script, rewrite `print` calls, add the import.
- Run a quick sanity check (`python scripts/csv_normaliser.py --help`).

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

✅ Copilot greps / awks the log file (asking permission), groups, and gives
you a citation-backed summary. It will NOT make up endpoints — if uncertain,
it tells you.

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
copilot -p "Write a Python script scripts/bulk_rename.py that renames every .jpeg in a given folder to .jpg, preserving case-sensitivity, with a --dry-run flag. Include a small unit test under tests/."
```

✅ Copilot writes both files. Inspect, accept, run tests.

---

## Transcripts

See `transcripts/` for **annotated copies** of real Copilot CLI sessions for
each scenario, so you can read them before trying yourself.

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
- The agent **remembers across turns** but loses context when you exit the
  REPL. For long-running work, keep one REPL session open.
- Pair the CLI with **shell aliases** (e.g., `alias ?='copilot -p'`) to lower
  the friction of one-shot questions.
- The Copilot CLI honours the same content-exclusion and policy controls as
  the IDE — Enterprise / Business admins can configure both centrally.

## Next demo →
[Demo 05 — Customising Copilot with AGENTS.md](../ghcp-demo-05-agents-md-customization)
— teach Copilot your conventions so it stops fighting your style guide.
