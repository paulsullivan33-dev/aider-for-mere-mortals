# The Repo Map

By the end of this chapter you
understand the map Aider builds of
your project — what is in it, what it
costs, and how to resize it. The check
needs no model: run this in any
repository and you get the map itself,
printed whole:

```bash
aider --show-repo-map
```

## What the map is

Chapter 6's problem was attention: the
model cannot hold every file in full.
The **repo map** is Aider's answer — a
skeleton of the whole repository,
small enough to ride along with every
request. Here is the lab's practice
project through the map's eyes
(transcript t11, complete):

```text
garden.py:
⋮
│def days_to_harvest(crop, days_since_sowing):
⋮
│def water_litres(plants):
⋮
│def bed_summary(plants, days_since_sowing):
⋮

test_garden.py:
⋮
│class TestGarden(unittest.TestCase):
│    def test_days_to_harvest(self):
│        self.assertEqual(days_to_harvest("lettuce", 45), 0)
⋮
```

Each file keeps its shape — the
function signatures, the class names,
a telling line here and there — and
loses its body. The `⋮` marks are
elisions: *more exists here, in this
order*. From this skeleton the model
can tell that `water_litres` exists,
what it takes, and that a test expects
eleven litres from four tomatoes and
ten lettuces — without spending the
tokens the full files would cost. When
it needs the body, it asks for the
file to be added (chapter 6).

In a live session `/map` prints the
current map, and it arrives with its
own framing (transcript t08):

```text
Here are summaries of some files present in my git repository.
Do not propose changes to these files, treat them as *read-only*.
If you need to edit any of these files, ask me to *add them to the chat* first.
```

Aider builds the map by parsing the
code — the tree-sitter grammars in the
install (chapter 3) cover most common
languages — and by analysing which
names are defined where and referenced
from everywhere else. On a big project
the whole skeleton still will not fit,
so Aider ranks: files and symbols that
the rest of the project leans on most
are kept first, and the map is trimmed
to its token budget from the top.
"Auto refresh" in the banner means it
is rebuilt as files change.

## The budget

The map is not free; it spends tokens
on every request. The lab measured the
moving parts with `/tokens`
(transcript t08):

```text
$ 0.0000      450 system messages
$ 0.0000      129 repository map  use --map-tokens to resize
$ 0.0000      361 garden.py       /drop to remove
==================
$ 0.0000      940 tokens total
```

The budget itself is chosen per model
— the lab's banner said **1024 tokens**
for the unknown local model and
**4096** for a cloud model whose
context window Aider knows — and you
can set it yourself, as chapter 11's
config file proved: with
`map-tokens: 512` the banner obeyed,
and `/tokens` showed the map growing
into the smaller allowance differently
(184 tokens used of 512; transcript
t09). Rules of thumb: the default is
sane; raise it (`--map-tokens 2048`)
when the model keeps asking for files
it should have found, on a project
with many small files; lower it when
money or a small context window makes
every token count. Setting it to 0
turns the map off, which on anything
bigger than a script is flying blind.

The map's working data lives in a
cache folder, `.aider.tags.cache.v4/`,
in the repository (transcript t12) —
one of the housekeeping files Aider
adds to `.gitignore` for you. Delete
it freely; it is rebuilt on the next
run, and `/map-refresh` forces a
rebuild inside a session when the map
looks stale.
