# Steering Aider

By the end of this chapter the things
you would otherwise retype every
session — the model, the map size,
your project's rules, the commands
that test it — are written down once,
in files Aider reads on its own. The
check is the banner again: set a
value in the config file, start Aider
with no flags, and watch the banner
obey. The lab's proof is below.

## Three places, one set of settings

Nearly every flag in the `--help`
(transcript t03) annotates its
environment variable — `AIDER_MODEL`,
`AIDER_EDIT_FORMAT` and so on — and
every setting also exists as a key in
the config file. Precedence is the
usual one: command line beats
environment beats config file beats
defaults. Settle each fact in the
cheapest place that states it once:
flags for today's experiment, the
config file for the project's standing
choices, the home folder's config
(`~/.aider.conf.yml`) for yours.

## The config file

`.aider.conf.yml`, in the project
folder, the repository root, or your
home. The lab's test file chose values
that show up in print, so pickup could
be *proved*, not assumed (transcript
t09):

```yaml
# .aider.conf.yml
model: ollama/llama3.2
map-tokens: 512
auto-commits: false
```

Started with **no `--model` flag at
all**, Aider's banner read:

```text
Model: ollama/llama3.2 with whole edit format
Repo-map: using 512 tokens, auto refresh
```

The model and the map budget both came
from the file. That is the whole
mechanism — and the reason to keep the
file small and commented: it is read
silently, and a stale line in it will
out-vote the flag you forgot you
needed. (`/settings` inside the chat
prints the settings in force, values
included — the fastest way to catch a
config file you have forgotten.)

## The .env file

Keys and endpoints live in the
environment, or in a `.env` file Aider
loads from the project folder, your
home, or the path given by
`--env-file`:

```text
OPENAI_API_KEY=...
OLLAMA_API_BASE=http://127.0.0.1:11434
```

The lab verified the pickup two ways
(transcript t10): with a deliberately
fake key in `.env` and an otherwise
empty environment, Aider proceeded
past its "no API keys" state to the
full banner — the key had been found
and used (the provider's verdict on
the fake key did not arrive inside
the lab's network timeout, and the
guide does not pretend otherwise).
And the moment the `.env` appeared,
Aider protected it:

```text
Added .env to .gitignore
```

—the same reflex that gitignores its
own housekeeping (`.aider*`, covering
the chat history, the input history
and the map cache of transcript t12).
Keys in `.env` stay on the machine and
out of the repository. Keys typed at
the prompt do neither. Choose
accordingly.

## CONVENTIONS.md: rules for the model

A file of plain-language rules —
coding style, naming, "run the tests
after every change", "never edit the
files under `fixtures/`" — can ride
along in every session. Name it on
the command line read-only:

```bash
aider --read-only CONVENTIONS.md
```

or list it under `read:` in the
config file, and it becomes part of
the context permanently (the mechanism
is chapter 6's read-only state; the
file's contents are yours to write).
This is documented-only for the lab —
its effect is on the model's
behaviour, which the lab could not
observe — and it is, by every user
account, the highest-leverage file in
this chapter. Keep it short; a page of
rules is followed, a book is skimmed,
by models as by people.

## Lint and test commands

Two more settings close the loop
between editing and checking:

```bash
aider --lint-cmd "python3 -m pyflakes *.py" \
      --test-cmd "python3 -m unittest"
```

`--lint-cmd` runs after edits and
feeds complaints back to the model to
fix. `--test-cmd` backs the `/test`
command: run it, and **only a
failure** — output plus a non-zero
exit — is added to the chat for the
model to work on; a pass stays silent.
(`--auto-test` and `--auto-lint` run
them after every change unprompted.)
The lab verified the underlying
machinery with `/run`, which executes
any command and adds its output to the
chat (chapter 5); the test-specific
loop is documented here from Aider's
manual. Wire these two in any project
you care about: they turn "the model
says it works" into "the suite says it
works", inside the same session.
