# QUEUE — queue-test

One queue, four lanes, one opener command each. Copy this file to
`Documentation/planning/QUEUE.md` (or the repo root if the project has no `Documentation/` tree; in a
monorepo, a project folder such as `apps/web/QUEUE.md`, worked by launching Claude Code in that folder)
and delete the example items.

**How it works**
- `/queue:build` reads `## Build`, `/queue:spec` reads `## Spec`, `/queue:meta` reads `## Meta`, `/queue:audit` reads `## Audit`.
- Anyone adds lines to `## Inbox`; only `/queue:spec` turns them into rows, so every new row is packed
  into the right build group.
- `## Build` is packed into `**Session N — ...**` groups, each with a Files line. One `/queue:build`
  terminal claims one group (by creating a git worktree named after it), so several terminals
  can build at once without touching the same files.
- Finished rows are deleted in the commit that finishes them (no `[done]` rows); the commit
  message is the record.
- The handoff for the next session lives in the `## ▶ NEXT SESSION` block at the top. `/queue:end` rewrites it.
- `[HEAD]` marks the item `/queue:build` builds next; `/queue:end` advances it once the gate passes.
- A `**Parallel wave:**` line groups file-disjoint items that `/queue:build` can hand to several
  subagents at once. Wave members add `Owns` / `Interface` / `Test`; shared "hub" files go to one
  item or to the main session; anything dependent waits for a later wave.
- **Names.** A task is its lane word plus a number: `Build 1`, `Spec 1`, `Meta 1`, `Audit 1`.
  A number is given once and never reused, because commit messages cite it; a task split into
  parts takes decimals, `Build 2.1`.

## ▶ NEXT SESSION — START HERE (written 2026-11-01 12:00)

**The one thing:** Build Session 1 — the todo store (Build 1), then the CLI (Build 2).
**Why:** Spec session turned the Inbox item into two serial rows; the repo is otherwise empty.
**Blocked on:** nothing.

**Actions:**
1. Take `QUEUE.md` `## Build` `[HEAD]`; its Files, Guardrails and Done when are the build.

**Runs unattended through:** all of Session 1. No row needs a person.

**Recommended model:** Sonnet — small stdlib code, decisions already made.

## Settled

<!-- One dated line per decision, append-only: `YYYY-MM-DD — decision, reason`. -->
2026-11-01 — Todo app is a Python 3 stdlib CLI with JSON file storage, reason: repo is empty, Python is installed, no dependencies keeps phase 1 small and reversible.

## Inbox

<!-- Untagged captures land here. Any session adds lines; /queue:spec moves each one to a lane,
     does it, or drops it, and leaves this section empty. -->

## Build

<!-- Packed into `**Session N — packed by file:** Files ...` groups by /queue:spec. Row shape:
- [HEAD] Build 1 — <one sentence>
  - **Files:** `path`
  - **Guardrails:** <condition to hold>
  - **Done when:** <observable gate>
-->

**Session 1 — packed by file: `todos.py`, `test_todos.py`, `README.md`** (Build 2 reads what Build 1 writes, so serial, no wave)

- [HEAD] Build 1 — Todo store: `add_todo(path, text)` and `list_todos(path)` over a JSON file.
  - **Files:** `todos.py`, `test_todos.py`
  - **Guardrails:** Python 3 stdlib only, no dependencies. Todo is `{"id": int, "text": str, "done": false}`; `id` = max existing id + 1 (1 when empty). Missing file means empty list. Reject empty or whitespace-only text with `ValueError`. Write the file whole, UTF-8. Phase 1 only: no done, delete or edit.
  - **Done when:** `python -m unittest test_todos` passes. Tests cover add, list, id increment, missing file, empty text.
- Build 2 — CLI over the store: `python todos.py add "text"` and `python todos.py list`.
  - **Files:** `todos.py`, `test_todos.py`, `README.md`
  - **Guardrails:** `argparse` subcommands only. Store path is `todos.json` in the current directory, overridable with `--file`. `list` prints `<id>. [ ] <text>` per line, and `No todos.` when empty. Empty text exits non-zero with the error on stderr. README gets a short usage block.
  - **Done when:** In a temp dir, `add "a"`, `add "b"`, `list` prints `1. [ ] a` then `2. [ ] b`; `python -m unittest test_todos` passes.

Burn-down: 1 session to done, carrying Build 1 and Build 2. Nothing blocked.

## Spec

<!-- - [ ] Spec 1 — <a decision that has to be made before something can be built> -->

## Meta

<!-- - [ ] Meta 1 — <friction in how the work gets done> -->

## Audit

<!-- - [ ] Audit 1 — <something to verify> -->
