# How Edits Are Written

By the end of this chapter you can
read the second line of the banner —
the **edit format** — and know what
the model is about to send and why.
The check is free: start Aider with
different models and compare that
line. The lab's three sightings
(transcript t13):

```text
Model: ollama/llama3.2 with whole edit format
Model: gpt-4o-mini with whole edit format
Model: anthropic/claude-sonnet-4-5 with diff edit format, infinite output
```

## The problem a format solves

The model cannot touch your disk. It
produces text; Aider must turn that
text into file changes exactly —
every line, every indent — or refuse.
The edit format is the contract that
says what shape the text arrives in.
Aider ships several contracts, and
picks per model, because models differ
in how reliably they can keep a strict
shape.

**Whole.** The model returns the
complete new contents of each changed
file, and Aider writes them over the
old. The simplest contract there is —
nothing to misalign — and the one the
lab's banners show for the local model
and for a smaller cloud model. Its
costs are plain: a one-line change to
a long file re-sends the whole file
(tokens, time, money), and a model
that truncates or quietly drops a
section while "rewriting" damages the
file in ways a diff makes obvious.
Whole is the format of trust-but-verify
on small files.

**Diff.** The model returns
**search-and-replace blocks**:

```text
garden.py
<<<<<<< SEARCH
def water_litres(plants):
=======
def water_litres(plants, dry_days=1):
>>>>>>> REPLACE
```

Aider finds the exact text after
SEARCH and swaps in the text after
REPLACE. Nothing else in the file is
re-sent or at risk, the blocks double
as a readable description of the
change, and if the search text does
not match the file — because the model
misremembered it — Aider says so and
asks the model to try again, rather
than guessing. This is the format the
banner gave the frontier model:
strong models keep the contract
effortlessly, and it is the cheapest
per change. A fenced variant
(**diff-fenced**) wraps the blocks for
models that handle code fences better.

**UDiff.** A standard unified diff,
the format `git diff` prints, offered
for models trained heavily on patches.
Same virtues as diff, harder for some
models to keep line-accurate.

**Editor formats.** In architect mode
(chapter 8) the *editor* model works
under **editor-diff** or
**editor-whole** — the same contracts,
tuned for carrying out a plan written
by another model rather than
originating the change.

## Choosing

Let the default ride, almost always:
Aider's registry knows which models
handle which contracts, and the banner
tells you the choice. Override when
you have evidence — `--edit-format
whole` (or `AIDER_EDIT_FORMAT`, or the
config file, chapter 11) for a local
model that keeps mangling search
blocks; the lab verified the override
lands in the banner (transcript t13):

```text
Model: ollama/llama3.2 with diff edit format
```

— the same model, wearing the contract
it was told to wear. When edits fail
to apply repeatedly, the failure is
nearly always a contract problem, and
chapter 15 treats it as one: simplify
the format before blaming the model.
