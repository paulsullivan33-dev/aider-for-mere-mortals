# What Aider Is

You are working on a program. It is
nearly right, but the harvest dates are
wrong, or a function needs to handle
one more case, or half the names want
changing. The familiar way to get AI
help is a chat window in a browser:
describe the problem, paste in some
code, read the answer, then find the
places in your files where the
answer's pieces belong and type them
in. The pasting is slow, and it is
where mistakes breed — a block pasted
one line off, a file half updated.

**Aider is that conversation moved
into your terminal, with the pasting
removed.** You start it inside your
project folder:

```bash
cd my-project
aider
```

and you get a prompt, right there among
your files. You type what you want in
ordinary words:

```text
> Make days_to_harvest accept a sowing
> date instead of a day count
```

Aider shows the request to a language
model — along with the files you have
given it and a map of the rest of the
project (chapters 6 and 7) — takes the
model's answer, and **applies the edits
to your files itself**. Then, because
your project is a git repository, it
**commits the change** with a message
describing it. You read the result with
the tools you already trust: `git diff`,
the test suite, the program itself. If
the change is wrong, one `/undo` in
the chat — or any git command you like
— puts the files back. Chapter 10
covers the bookkeeping in full,
including where `/undo` stops.

Three things follow from that design,
and they are the reasons to choose
Aider over a chat window.

First, **the model sees the real
project**, not the fragments you
remembered to paste. You choose the
files it may edit; it always sees a
map of everything else, so "the
function that works out watering" is
something it can look up, not
something you must quote.

Second, **every change lands as a
commit**. A session with Aider leaves
a trail of small, labelled steps in
your history, each one reviewable and
reversible on its own. That trail is
the safety system, and chapter 1 of
your habits should be: start Aider in
a clean, committed repository, and
the worst case is always one undo
away.

Third, **the model is your choice and
your account**. Aider itself is free,
open-source software. The model can be
a cloud service you pay per token, or
a model running on your own machine
that costs nothing per question and
never sees your code leave the house.
Chapter 4 covers both routes — and
what happens when there is no model at
all, which is the first thing this
guide's lab found out.

## What it is not

Aider is not an editor: it has no
window of its own, and the files stay
in whatever editor you already use —
Aider changes them on disk, and your
editor notices. It is not a model: it
contains no AI of its own and can do
nothing until you connect one; chapter
14 is blunt about that dependency. It
is not autonomous: it works one
request at a time, in a session you
are sitting in, and the committing is
deliberate, not a background process
wandering your disk. And it is not
magic about quality — it is exactly as
good a programmer as the model you
connect, plus the context you give it.
Chapters 6 and 11 are about improving
the second half of that sentence.

## Who it is for

The solo programmer whose project has
grown past what fits in a chat paste.
The maintainer of a small tool who
wants boilerplate, tests and renames
done at dictation speed. The learner
who wants to watch an experienced
hand — the model — make changes in a
real repository, with every step saved
and reversible. And the privacy-minded
builder who pairs it with a local
model, so the whole partnership —
code, questions, answers — stays on
one machine. The common thread is one
person, one repository, and work they
want done *in* the files, not
described at them.

## The honest catch, up front

Aider's quality ceiling is the model,
and its floor is your review habit.
A strong model with clear requests
and a passing test suite is a genuine
accelerant. A weak model, a vague
request and no tests will produce
commits just as efficiently — wrong
ones. The tool cannot tell the
difference; you and your tests do
that. This guide therefore spends as
much time on the checking machinery —
context, maps, diffs, commits, tests —
as on the asking. That is deliberate.
It is also why the lab's missing model
matters less than it might: everything
in the checking machinery was present
and testable, and this guide tested
it. Where the telling reaches the
conversation itself, it says so.
