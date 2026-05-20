# Transcript — Scenario 1 (one-shot)

```text
$ copilot -p "Show me the git command to delete every local branch already merged into main, but never delete main or develop."

▌ I can do that. Here is a safe one-liner:

  git branch --merged main | grep -vE '^\*|main$|develop$' | xargs -n 1 git branch -d

  • --merged main      : only branches fully merged into main
  • grep -v ^\*        : skip the currently-checked-out branch (the * marker)
  • grep -vE 'main$|develop$' : never delete main or develop
  • xargs -n 1 git branch -d : delete one branch at a time (safe: -d refuses
    branches with un-merged work; use -D only if you really mean it).

  Want me to run it now? (y/N)

> N
```
