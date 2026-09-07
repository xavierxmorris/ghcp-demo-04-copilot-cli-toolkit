# Workshop: terminal automation with observable boundaries

**Audience:** developers and platform engineers. **Time:** 45-60 minutes.
**Outcome:** a dry-run feature whose non-writing behavior is demonstrated,
a refactor that preserves data output, and a log summary that separates
evidence from conjecture.

## 1. Preflight and authority - 5 minutes

Use a dedicated clone, not your home directory or a production checkout.
Run `git status --short` and retain any existing work. The fixture is
synthetic; do not substitute customer logs or real exports.

```powershell
python --version
copilot --version
gh --version
```

Python runs the supplied scripts. `gh` and GitHub authentication are needed
only for the optional GitHub exercise, not CSV normalization or local log reading.
Copilot access and model usage remain subject to your plan and organization.

Start `copilot`, inspect `/help`, and use `/plan` before a multi-file edit.
Approve a bounded command only after reading it. `-p` means "run a prompt and
exit"; it does not mean "cannot edit." Broad shell approval is not a sandbox.
Avoid `--allow-all-tools` for this workshop.

## 2. Define the existing CSV contract - 8 minutes

Read [scripts/csv_normaliser.py](scripts/csv_normaliser.py) and
[fixtures/in.csv](fixtures/in.csv) before changing the parser.

```text
Read the normalizer and fixture without writing anything. List the exact
transformations performed, the default output path, and current CLI parsing.
Distinguish behavior visible in source from behavior illustrated in transcripts.
```

The shipped behavior is:

| Concern | Actual contract |
| --- | --- |
| Headers | Trim ends and lowercase; `first name` retains its interior space |
| Values | Trim ends; `ADA@example.com` retains its case |
| Empty rows | Drop rows whose cells are all blank/whitespace |
| Default output | Input basename with `.clean.csv` suffix |
| Row count | Four data rows in the shipped nonempty fixture |
| Empty input | Report zero and return before writing |
| CLI | Positional parsing, no `--dry-run` or argparse help yet |

The transcript's pretty output is not the specification. Treat a change to
header spelling or email case as a separate feature.

## 3. Add dry-run with a falsifiable guarantee - 15 minutes

```text
Add argparse and --dry-run to scripts/csv_normaliser.py. Preserve the existing
normalization rules and normal output behavior. A dry run must not create,
truncate, replace, or modify any file, including an explicitly supplied output
that already exists. Put CSV preview data on stdout and diagnostics on stderr.
Test using temporary directories and the stdlib unittest module; no packages.
```

Review the tests before the implementation. Require these independent cases:

| Case | Evidence required |
| --- | --- |
| Normal run into a new temporary output | Parsed content and four data rows |
| Dry run with nonexistent output | Output path still absent |
| Dry run with an existing sentinel output | Output bytes unchanged |
| Either mode | Input bytes unchanged |
| Blank input | No fabricated header or rows; explain chosen dry-run display |
| Quoted comma in a cell | CSV parsing preserves one cell |

After the learner has created the tests:

```powershell
python -m unittest discover -s tests -v
```

For a manual check, hash `fixtures\in.csv` before and after the dry run with
`Get-FileHash`. Use a fresh exercise-owned output path. A message saying
"no files changed" proves nothing unless you also inspect the paths and bytes.
Do not overwrite an existing output just to create a demonstration.

**Failure drill:** temporarily open the output in write mode before the
dry-run branch. The sentinel test must fail even if the CSV preview is correct.
Restore only that deliberate edit and rerun the test.

## 4. Refactor diagnostics without corrupting stdout - 8 minutes

[scripts/seed_logs.py](scripts/seed_logs.py) writes generated log **data** to
stdout. Those `print` calls are not interchangeable with diagnostic logging.
The same distinction matters if the CSV preview is piped into another command.

```text
Introduce a small stdlib logging helper for diagnostics only. Preserve
machine-readable stdout, CLI exit codes, and the CSV transformation contract.
Explain which print calls you intentionally leave alone. Add a regression
test showing that diagnostics do not become CSV rows.
```

Run the same focused tests. Review imports for both direct script execution
and any module-based use you claim to support; do not assume they are identical.

## 5. Triage logs without inventing a cause - 8 minutes

Read [logs/app.log](logs/app.log), not newly generated random logs.

```text
Count 5xx records by user and endpoint in logs/app.log. Cite line numbers.
Ignore the final instructional note, which is not a log record. Separate
observations, hypotheses, and the next evidence needed. Do not modify files.
```

The shipped fixture's answer key is eight 5xx records for `u_017` at
`/api/checkout` and one for `u_044` at `/api/orders`. The 401 login response is
not a 5xx. Check the source lines rather than adopting the agent's totals.

A root-cause conclusion would require more evidence, such as traces, dependency
health, and deployment timing. Status-code correlation alone does not establish
a failed database, a bad deployment, or a particular responsible team.

## 6. Optional GitHub exercise - 8 minutes

Use an explicitly named repository you own or have permission to inspect.
Ask for open-PR summaries and **draft** follow-up comments only.

```text
In OWNER/REPO, list up to five open PRs inactive for at least 30 days, ordered
oldest activity first. Show the query scope and updated timestamps. Draft
comments locally. Do not post comments, edit PRs, merge, or change settings.
```

An unqualified `gh pr list` is repository-scoped, not an organization-wide
search. If fewer than five qualify, report that rather than filling the list.
A later decision to post a comment is a separate externally visible action.

## Evidence, troubleshooting, and reset

Keep the contract table, before/after hashes, test output, diff, and source-lined
log summary. Record which permissions were granted.

| Symptom | Safe next step |
| --- | --- |
| Starter treats `--help` as a filename | Complete the argparse exercise first |
| CSV preview contains timestamps | Diagnostics leaked onto stdout |
| "Dry run" changes a file | Inspect where the output is opened |
| MCP/GitHub tool unavailable | Use the local exercises; do not widen account access |
| Resume has surprising context | Inspect `/session`; use a fresh session for a new task |

Delete only exercise-owned temporary outputs after inspecting them. Do not run
the optional rename exercise against a personal folder. Reset approvals with
`/reset-allowed-tools` when appropriate.

## Current sources

Checked **2026-09-07**, local CLI **1.0.84-1**:
[CLI modes and security](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli),
[CLI best practices](https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices).
Archived transcripts intentionally retain their historical UI; `/help` is the
reference for your installed build.
