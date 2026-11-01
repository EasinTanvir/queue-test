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

**The one thing:** Run `/queue:spec` to turn the Inbox item (todo app phase 2) into Build rows.
**Why:** Phase 1 shipped (Build 1, Build 2; 7 tests pass); `## Build` is empty.
**Blocked on:** nothing.

**Actions:**
1. Inbox holds 1 item — the next free session runs `/queue:spec` to turn it into rows and pack them before claiming a build group.

**Runs unattended through:** the spec pass. No row needs a person.

**Recommended model:** Sonnet — small scope, decisions already made.

## Settled

<!-- One dated line per decision, append-only: `YYYY-MM-DD — decision, reason`. -->
2026-11-01 — Todo app is a Python 3 stdlib CLI with JSON file storage, reason: repo is empty, Python is installed, no dependencies keeps phase 1 small and reversible.

## Inbox

<!-- Untagged captures land here. Any session adds lines; /queue:spec moves each one to a lane,
     does it, or drops it, and leaves this section empty. -->
- (2026-11-01) Todo app phase 2: mark a todo done and delete a todo — `todos.py` already stores `done`, so this unblocks a usable app.

## Build

<!-- Packed into `**Session N — packed by file:** Files ...` groups by /queue:spec. Row shape:
- [HEAD] Build 1 — <one sentence>
  - **Files:** `path`
  - **Guardrails:** <condition to hold>
  - **Done when:** <observable gate>
-->

## Spec

<!-- - [ ] Spec 1 — <a decision that has to be made before something can be built> -->

## Meta

<!-- - [ ] Meta 1 — <friction in how the work gets done> -->

## Audit

<!-- - [ ] Audit 1 — <something to verify> -->
