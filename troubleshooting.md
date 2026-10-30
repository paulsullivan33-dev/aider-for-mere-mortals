# Troubleshooting

The failures the lab met, plus the
ones the project's own messages point
at — each with the check that names
it. Start every diagnosis at the
banner (chapter 5): most problems are
visible there before the prompt.

**`error: externally-managed-environment`
from pip.** Not an Aider problem —
PEP 668, your system protecting its
Python (chapter 3 has it verbatim).
Do not reach for
`--break-system-packages`. Install
with pipx, with `aider-install`, or in
a venv, exactly as chapter 3 lays out.

**Aider asks a question and a script
hangs.** Run outside a git repository,
Aider opens with "No git repo found,
create one to track aider's changes
(recommended)?" — and a piped or
scheduled run will wait on that prompt
instead of doing its job; the lab's
first `--models` call sat silently for
minutes this way. Work inside a
repository, pass `--yes-always` to
auto-answer prompts in scripts, and
when output stops mid-startup, check
for a question before assuming a hang.

**The OpenRouter sign-in offer.**
"No LLM model was specified and no
API keys were provided" means exactly
what it says (chapter 4): Aider looked
for keys in the environment, the
`.env` files and the config, and found
none. Either accept the offer (it
creates an account — a human decision,
in a browser), or set the key for the
provider you meant: check the variable
name, check the shell exported it, and
check no stale `.env` is answering
instead.

**`Connection refused` and a ladder of
retries.** The endpoint named by
`OLLAMA_API_BASE` (or your provider
URL) has nothing listening. Nine
retries over about a minute
(transcript t06) is Aider being polite
to a server that may be starting; if
yours was already started, verify the
server (`curl $OLLAMA_API_BASE/api/tags`
for Ollama), verify the model is
pulled, and verify the port matches.
A wrong *model name* looks different:
"Did you mean one of these?" with
nearby names — that one is a spelling
lesson, and `--no-show-model-warnings`
silences the lecture once you have
learned it.

**"Unknown context window size and
costs, using sane defaults."** Aider
could not find the model's registry
entry — common with brand-new or
self-served models, and with the
registry fetch timing out, which the
lab's slow network produced alongside
a `raw.githubusercontent.com` read
timeout. It is a warning, not a fault:
the map budget and cost figures will
be estimates. A `--model-settings-file`
or `--model-metadata-file` (see
`--help`) supplies the facts locally
when it matters.

**Edits that will not apply.** The
model's search blocks do not match the
file — it misremembered the code, or
another change landed underneath it.
Simplify the contract (chapter 9):
`--edit-format whole` for a struggling
model, re-`add` the fresh file so the
model sees the current text, and
`/map-refresh` if the map is stale.
Repeated failures after that are the
model telling you its limit on this
project's size; shrink the task.

**`/undo` refuses.** "The last commit
was not made by aider in this chat
session" (chapter 10). Undo in the
session that made the change, or use
git directly — `git revert` for a
polite public undo, `git reset` only
when you mean it; Aider's own warning
about the destructive route is honest.

**The wrong model answers.** The
banner names the model in force; if
it is not the one you set on the
command line, a config file or
environment variable out-voted you
(chapter 11). `/settings` shows the
values in force, and `/model` switches
mid-session when the discovery is
merely annoying.
