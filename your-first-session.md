# Your First Session

By the end of this chapter you can
start Aider on a project, read
everything it prints before the
prompt, and drive the parts of a
session that need no model at all.
The check is the session itself,
reproduced below from the lab: the
same commands on your own project
should produce the same shapes of
answer, with your files in place of
the lab's.

Start Aider inside a project, naming
the file you most care about:

```bash
cd garden-planner
aider garden.py
```

## The banner, line by line

Before the prompt, Aider introduces
itself (from the lab's transcript
t08, with the warning lines chapter 4
explained removed):

```text
Aider v0.86.2
Model: ollama/llama3.2 with whole edit format
Git repo: .git with 3 files
Repo-map: using 1024 tokens, auto refresh
Added garden.py to the chat.
```

Each line is a part from chapter 2,
reporting for duty. The **version** —
quote it in any bug report. The
**model and its edit format** — if
this names the wrong model, nothing
after it is worth doing; chapter 4 is
the fix. The **git repository** and
its file count — Aider found the repo
and counted what the map must cover.
Leave the folder unversioned and this
line becomes a question instead: Aider
offers to create a repository, because
its whole safety story depends on one.
The **repo map** and its token budget
— chapter 7. And the **files added**:
the command line's files start in the
chat, editable.

The prompt itself shows the state of
the chat as you work:

```text
garden.py
>
```

Files in the chat are listed above the
`>`; as you add and drop files the
list changes. It is the cheapest
status display there is, and chapter 6
is about driving it.

## What a model session is made of

With a connected model — this part is
documented, from Aider's own manual,
because the lab had no model to hold
the conversation — a working session
is a rhythm of four moves:

1. **Add the files** the change
   touches (chapter 6).
2. **Ask in plain words.** One change
   per request reads better in the
   history than five: "Add a
   `sowing_date` function that returns
   the date a crop goes in, N days
   before its harvest window."
3. **Read what happened.** Aider
   prints the edits as they are
   applied; `git diff` shows them
   again in your own tools. Run the
   tests — or let `/test` run them,
   chapter 11.
4. **Accept or undo.** A good change
   is already committed; a bad one is
   one `/undo` away (chapter 10, with
   its caveat).

## The parts that need no model

The lab drove a real session against
an endpoint that could not answer, and
everything except the conversation
worked. That session (transcripts t07
and t08) is the spine of the next
three chapters: `/ls` listed the
project's files, split into "in the
chat" and "not in the chat"; `/map`
printed the real repo map; `/tokens`
accounted for every token in the
context; `/add` and `/drop` moved
files in and out; and `/run` executed
the project's test suite inside the
chat and kept the output:

```text
> /run python3 -m unittest
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
Added 5 lines of output to the chat.
```

Notice what that last line means:
command output becomes part of the
conversation, so the model sees the
same test results you do. That single
mechanism is most of how Aider debugs.

`/help` inside the chat lists every
command with a one-line description —
43 of them in 0.86.2, captured whole
in transcript t07 — and `/help`
followed by a question is answered
from Aider's documentation (that part
does use the model). `/exit` or
`/quit` ends the session; the history
stays behind in `.aider.chat.history.md`
(chapter 11), and the repository keeps
every commit.
