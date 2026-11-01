## Work queue

All pending work lives in `QUEUE.md`, sorted into lanes. Open a session with
`/queue:build`, `/queue:spec`, `/queue:meta` or `/queue:audit`; close every session with
`/queue:end`.

Git rules (several sessions can share this repo):
- Stage and commit explicit paths: `git commit -m "..." -- <paths>`.
- Avoid `git add .`, `git commit -a` and a bare `git commit`.
- Commit small; `/queue:end` opens the pull request.

## /end in this repo

- Land: pull request against `main`
