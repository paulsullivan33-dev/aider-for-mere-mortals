# Files In and Out of Context

By the end of this chapter you control
what the model can see and what it may
change — the single biggest lever on
the quality of its work. The check is
`/ls`, run before and after the moves
below: it should show your files
crossing between its two lists exactly
when you tell them to.

A model reads what it is given, all of
it, every time you speak. Files in the
chat are re-sent with each request,
priced in tokens (chapter 5's `/tokens`
shows the bill). So context is a
budget and an attention span at once:
too little, and the model guesses at
code it cannot see; too much, and the
important file drowns in the tenth
unrelated one — while everything slows
and costs more. Aider gives you three
states for a file, and commands to
move files between them.

## The three states

**In the chat, editable.** Named on
the command line, or added:

```text
> /add garden.py
Added garden.py to the chat
```

The model sees the file's full
contents and may edit it.

**In the chat, read-only.** Reference
material — an interface the model must
respect, a test file it must satisfy,
a data file it must not "fix":

```text
> /read-only test_garden.py
```

Aider's own description, from `/help`:
"Add files to the chat that are for
reference only, or turn added files to
read-only." The model can read every
line and change none of them.

**Not in the chat.** The model still
knows the file exists — it is in the
repo map (chapter 7) as a skeleton —
but it sees no contents until you add
it or it asks you to. Remove a file
you are done with:

```text
> /drop test_garden.py
Removed test_garden.py from the chat
```

## Seeing the states

`/ls` prints the whole picture. From
the lab's real session (transcript
t08), with `garden.py` in the chat:

```text
> /ls

Repo files not in the chat:

  README.md
  test_garden.py

Files in chat:

  garden.py
```

That split is the habit to build:
before each request, glance at `/ls`
(or at the prompt's own file list) and
ask two questions. Can the model see
everything this change touches? Can it
edit anything it shouldn't? A test
file the model may edit can be made to
pass by editing the test — read-only
tests and a suspicious eye are the
defences, in that order.

## Practical rules

Add the file you want changed, the
file that defines what it talks to,
and the tests that prove it — usually
two to four files, not twenty. Add
whole folders only when the change
really is everywhere (a rename, a new
convention); `/add` accepts the same
globs your shell does, like
`/add src/*.py`. Drop files the moment
a sub-task finishes, especially long
ones; `/reset` drops everything and
clears the history when the session
has wandered and a fresh start is
cleaner than tidying. And when the
model asks for a file — it can, when
the map shows it something it needs in
full — Aider will ask *you* whether to
add it. That prompt is a design
decision, not a nuisance: you stay the
gatekeeper of what leaves the disk and
enters the conversation.
