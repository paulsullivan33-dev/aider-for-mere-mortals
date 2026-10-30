# Ask, Code, Architect

By the end of this chapter you can
choose how a request is handled —
discussed, applied, or planned and
then applied — and switch modes
without restarting. The check is
Aider's own: `/chat-mode` lists where
you are, and each mode's commands
below are quoted from the real `/help`
the lab captured (transcript t07).

Everything you type at the prompt is
either a slash command for Aider, or a
message to the model. Messages are
handled in one of four **chat modes**,
and the mode is the difference between
"the model talked" and "the model
changed my files". This layer of the
tool is documented rather than
lab-run — the lab had no model to
answer in any mode — but the modes
shape every claim in the chapters
around this one, so they are set out
carefully from Aider's own manual.

## Code mode: the default

```text
/code   Ask for changes to your code.
```

In code mode a request is an
instruction to edit: the model answers
with changes in the session's edit
format (chapter 9), Aider applies
them, and git records them
(chapter 10). This is where the pair
programming happens, and where a vague
request does the most damage — code
mode takes you literally.

## Ask mode: questions only

```text
/ask    Ask questions about the code base
        without editing any files.
```

Ask mode fences the model off from
your files entirely: it can read
everything in context and the map, and
answer — "where is the watering total
computed?", "what would break if this
function changed its return type?" —
but it cannot edit, whatever you say.
It is the mode for exploring a project
you have inherited, and for the
read-only review recipe in chapter 12.
If an ask-mode conversation turns into
a change you want made, `/code` with
the same request performs it, with the
whole discussion already in context.

## Context mode: gathering

```text
/context   Enter context mode to see
           surrounding code context.
```

Context mode is ask mode with a
narrower job: finding and showing the
code relevant to a topic, so you can
see what the model sees and decide
what belongs in the chat. Think of it
as the librarian between chapters 6
and 7 — it works the map on your
behalf before any editing starts.

## Architect mode: two models

```text
/architect   Enter architect/editor mode
             using 2 different models.
```

Architect mode splits the job between
two models. The **architect** — your
main, strongest model — receives the
request and replies with a plan in
plain language: what will change,
where, and why. An **editor** model —
often a cheaper or faster one, set
with `--editor-model` — turns the plan
into the actual edits. You approve the
plan before anything is applied
(`--auto-accept-architect` skips the
approval, for the brave). The split
buys two things: the expensive brain
is spent on thinking, not on the
mechanical formatting of edits; and
the plan is a checkpoint a human can
read — the closest thing Aider has to
"show me what you are about to do".

Switching is free and frequent: type
`/ask`, `/code`, `/architect` or
`/context` with a request attached —
`/ask why does the summary sort its
output?` — and the request is handled
in that mode; type the command alone
and the mode sticks for what follows.
The everyday pattern this produces:
ask first, read the answer, then code
— two commands, one conversation, and
no edit you did not see coming.
