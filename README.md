# Aider for Mere Mortals

Most AI help with code lives in a chat
window: you paste code in, the answer
comes back as text, and you paste the
changed pieces back into your files by
hand, one careful block at a time.
**Aider removes the pasting.** It is a
program that runs in your terminal,
inside your project. You tell it what
you want in plain words — "add a
function that works out watering days"
— and it edits the files itself, shows
you the change, and commits it to
**git** with a message, all without
leaving the terminal. When it gets
something wrong, the commit is right
there to undo. It is pair programming
where the other programmer types very
fast and keeps perfect notes, and you
stay the one who decides.

Aider brings no model of its own. You
connect it to a large language model —
a cloud service with an **API key**, or
a model running on your own machine
through a tool such as Ollama — and
Aider handles everything around the
model: which files the model can see,
a map of your whole project so it can
find its way around, the exact format
its edits must arrive in, and the git
bookkeeping afterwards. Choosing and
reaching that model is a real part of
the setup, and this guide treats it as
one.

This guide is also honest about a
thing most guides hide: **the lab that
wrote it had no model at all.** No API
key, no local model server, and a rule
against creating accounts to get one.
So everything that can be checked
without a model was checked for real —
the install, the full command list,
the configuration files, the repo map
built from a practice project, the
session commands, the commit machinery
— and the transcripts in `aider-lab/`
are the evidence. The conversation
with the model itself — the actual
pair programming — is taught from
Aider's own documentation and from the
tool's own help text, and is labelled
as documented-only wherever it
appears. `criteria.md` keeps the full
ledger. A guide that pretended to show
you chats it never had would be
teaching you to trust exactly the kind
of made-up output Aider's git commits
exist to protect you from.

One safety fact belongs before
everything else, because everything
else depends on it: Aider writes to
your files and commits to your
repository. That is the point of it,
and it means the guardrail is git
itself — work in a repository, commit
before you start, read the diffs, and
keep your API keys in your environment
or a `.env` file, never in the chat.
Chapter 11 shows the settings; chapter
14 is plain about the limits.

## What this guide covers

- [**What Aider is**](what-aider-is.md) —
  the mental model: a chat in your
  terminal that ends in edited files
  and git commits, not in text to copy
- [**The moving parts**](the-moving-parts.md) —
  the chat, the model, the files in
  context, the repo map, the edit
  formats and git — and which part does
  what
- [**Installing Aider**](installing-aider.md) —
  the official routes, the Python
  packaging refusal the lab met on the
  way, and the version check that
  proves it runs
- [**Connecting a model**](connecting-a-model.md) —
  API keys, local models through
  Ollama, what Aider does when there is
  no model at all, and the exact errors
  a dead endpoint produces
- [**Your first session**](your-first-session.md) —
  the startup banner read line by line,
  and what a working session is made of
- [**Files in and out of context**](files-in-context.md) —
  `/add`, `/drop`, `/read-only` and
  `/ls`: choosing what the model can
  see and what it may touch
- [**The repo map**](the-repo-map.md) —
  the signature-level map of your whole
  project that Aider builds and keeps
  current, measured on a real project
- [**Ask, code, architect**](ask-code-architect.md) —
  the chat modes: questions that change
  nothing, edits that change files, and
  the two-model architect pattern
- [**How edits are written**](edit-formats.md) —
  whole files, search-and-replace
  blocks and diffs — and why Aider
  picks a different one per model
- [**Git does the bookkeeping**](git-does-the-bookkeeping.md) —
  auto-commits, commit messages,
  `/commit`, and what `/undo` will and
  will not undo — with the lab's
  surprise included
- [**Steering Aider**](steering-aider.md) —
  the config file, the `.env` file,
  `CONVENTIONS.md`, lint and test
  commands: saying it once instead of
  every session
- [**Recipes**](recipes.md) — a fix
  loop driven by failing tests, a
  read-only review of code you do not
  trust yet, and a two-model refactor
- [**The neighbours**](the-neighbours.md) —
  the editor assistants, the other
  terminal agents, and plain chat with
  copy and paste: what each does that
  Aider doesn't, and vice versa
- [**Limits**](limits.md) — no model,
  no edits; quality bounded by the
  model you bring; undo narrower than
  it looks; and the rest, stated plainly
- [**Troubleshooting**](troubleshooting.md) —
  the packaging refusal, the prompt
  that hangs a script, the refused
  connection, and the traps this
  guide's lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Reaching a model on your behalf. The
lab created no accounts and held no
keys, so signing up with a provider,
judging which cloud model writes the
best code, and comparing costs on real
work are outside this guide — chapter
4 shows every route and every error,
and stops where the account begins.
Training or fine-tuning a model is
likewise out; Aider uses models other
people built. Running a model on your
own machine is a guide of its own —
the Ollama and Local AI at Home guides
in this series cover it, and chapter 4
shows the one environment variable
that connects the two.

## How to use this guide

Read chapter 1 for the model of the
tool, and chapter 2 before installing
anything — knowing which part does
what turns later surprises into named
problems. Chapters 3 and 4 get you an
installed Aider and a connected model;
chapter 5 walks the first session.
Chapters 6 to 8 are the daily craft:
what the model sees, the map it
navigates by, and the modes you steer
with. Read chapter 10 slowly even if
you know git — the bookkeeping is
where Aider earns its keep, and where
its one sharp edge (chapter 10's
`/undo` result) lives. The lab's
transcripts live in
`aider-lab/transcripts/`; its practice
project is `aider-lab/garden-planner/`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Ollama for Mere Mortals](https://paulsullivan33-dev.github.io/ollama-for-mere-mortals/)
- [Local AI at Home for Mere Mortals](https://paulsullivan33-dev.github.io/local-ai-for-mere-mortals/)
- [Git for Mere Mortals](https://paulsullivan33-dev.github.io/git-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/aider-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/aider-for-mere-mortals/blob/main/LICENSE-CODE).
