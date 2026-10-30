# Recipes

Four ways of working, assembled from
the parts the previous chapters
proved or documented. Where a step
needs the model, it is the documented
workflow of chapter 8; where a step is
a command the lab ran, the transcript
is named. Each recipe assumes a clean,
committed repository — chapter 10
explains why that is the entry fee.

## 1. The failing-test fix loop

*For: a bug you can state as a test.*

1. Write the failing test yourself, in
   your editor, and commit it. A test
   you wrote is a specification the
   model cannot talk its way around.
2. Start Aider with the code and the
   test: `aider garden.py test_garden.py`,
   or `/add` both in the session.
3. Set the test command once:
   `--test-cmd "python3 -m unittest"`
   (chapter 11), then `/test`.
4. The failing output — and only the
   failing output — enters the chat,
   and the model works against the
   real error, not your summary of it.
5. Repeat `/test` until it passes
   silently. Read the diff before you
   believe the silence.

The manual version of step 3 is
lab-verified: `/run python3 -m unittest`
executed the suite in the chat and
kept its output there (transcript
t08).

## 2. The read-only review

*For: code you must judge before you
trust — a dependency, a contribution,
your own old work.*

1. `aider --model <your model>` in the
   repository, then
   `/read-only <files>` for everything
   under review (chapter 6).
2. `/ask` mode, and ask the questions
   a reviewer asks: what does this
   assume about its inputs? Where does
   it fail silently? Which parts would
   break first under change?
3. Nothing can be edited in this
   shape — read-only files and ask
   mode fence the session twice — so
   the output is a report, not a diff.
4. If the review earns changes, switch
   to `/code` and make them
   deliberately, in the same session,
   with the findings in context.

## 3. The two-model refactor

*For: a change too wide for one
request — a rename everywhere, a
module split, a new layer.*

1. Put the standing rules in
   `CONVENTIONS.md` first (chapter 11):
   the refactor's invariants belong in
   writing, not in one message.
2. Start in `/architect` mode with
   your strongest model as architect
   and a fast one as editor:
   `aider --architect --editor-model <model>`.
3. Describe the end state, not the
   steps: "split the watering logic
   into its own module; every caller
   keeps working." Read the plan as a
   reviewer. Argue with it — plans are
   cheap; edits are commits.
4. Approve, and let the editor apply
   it. Run the suite (`/test`) and
   read `git log`: a wide change
   should land as several small
   commits, each one a place you can
   stop.

## 4. The guided tour of a new project

*For: inheriting code — yours from
three years ago counts.*

1. Clone, then run the one command
   that needs no model at all:
   `aider --show-repo-map` (transcript
   t11). The skeleton — files, classes,
   signatures — is the fastest honest
   overview there is.
2. Start a session, `/ask` mode, and
   tour with questions: where does
   execution start? What is the data?
   Which file would a change to X live
   in? The map plus the files answer
   from the code, not from a README's
   hopes.
3. Keep the session's history:
   `.aider.chat.history.md` (chapter
   11) is now the beginnings of the
   documentation the project never
   had.
