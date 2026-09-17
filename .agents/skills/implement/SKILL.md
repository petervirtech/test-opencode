---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Commit your work to the current branch.

Review happens in a new session, not this one: the implementation context makes an in-session /code-review unmanageable. Close by telling the user to run /code-review in a fresh session, naming the commit range you implemented (fixed point = the commit before your first implementation commit).
