# Git Does the Bookkeeping

By the end of this chapter you know
how a session with Aider reads in your
git history — and you know the one
sharp edge the lab found, before it
finds you. The check is `git log
--oneline` in any project you have
used Aider on: a session should appear
as a trail of small commits, each
describable in a line.

## Why git is not optional

Aider requires a repository. Start it
in an unversioned folder and it offers
to create one on the spot; start it
scripted, where nobody can answer, and
it waits (chapter 15). This is not
bureaucracy. The repository is the
undo system, the audit trail and the
review surface, all in one, and Aider
leans on it for all three.

## What gets committed, and when

From Aider's documentation — the
commits that follow *model edits* are
documented-only for this guide, since
the lab had no model to make one:

- **After each set of model edits**,
  Aider commits them as their own
  commit. The message is written by the
  **weak model** (chapter 2) unless you
  supply the style yourself, and it
  describes the change, not the chat.
- **Before editing a file with
  uncommitted changes**, Aider commits
  those first — the so-called **dirty
  commit** — so its own work never
  mixes with yours in one commit. Your
  work and its work stay separable,
  which is what makes either undoable.
- **Attribution is configurable**: by
  default commit messages record that
  Aider made the change (the flags are
  `--attribute-commit-message-author`
  and its kin, in transcript t03's
  help). Teams that want an honest
  history leave it on.

Turn the whole machinery off with
`--no-auto-commits` when you would
rather commit by hand — some do, on
shared branches.

## The parts the lab proved

`/commit` commits changes you made
**outside** the chat — your own edit,
made in your editor while Aider was
open. Give it a message and no model
is needed at all; the lab did exactly
that (transcript t15):

```text
> /commit Add a watering note to garden.py
Commit 1f3460b Add a watering note to garden.py
You can use /undo to undo and discard each aider commit.
```

and `git log` showed the commit, one
line added to one file. Without a
message, the weak model writes one —
that path is documented-only here.

Then the sharp edge. The obvious next
step is `/undo` — `/help` describes it
as "Undo the last git commit if it was
done by aider". The lab tried it in a
fresh session, and then, corrected,
in the *same* session as the `/commit`
itself (transcripts t16 and t17). Both
times, verbatim:

```text
The last commit was not made by aider in this chat session.
You could try `/git reset --hard HEAD^` but be aware that
this is a destructive command!
```

Read that carefully, because it
refines the sales pitch: **`/undo`
covers commits Aider made from model
edits during the session you are in.**
A commit you asked for with `/commit`
— even seconds earlier, even in this
session — is not one of those, and
neither is anything from a previous
session. The refusal at least points
at the manual route (`/git` runs git
commands from the chat, or use your
own terminal) and labels it
destructive, which it is. The habit
this produces: undo promptly, in the
session that made the change, and
treat `git log` — not memory — as the
record of what can still be unwound.

## The diff is the review

`/diff` shows the changes since your
last message, inside the chat; plain
`git diff HEAD~1` shows the last
commit in your own tools. The routine
worth building is unglamorous: after
any change you did not watch happen,
read the diff before the next request.
Aider's commits make that cheap — each
is small, labelled, and one command
from inspection. The pair-programming
bargain only holds while the senior
partner — you — actually reviews.
