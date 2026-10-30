# Installing Aider

By the end of this chapter Aider is
installed, and you have run the one
command that proves it:

```bash
aider --version
```

The lab's install printed:

```text
aider 0.86.2
```

(the version in transcript t03; yours
will be newer, and that is fine —
everything in this guide was checked
against 0.86.2).

Aider is a Python program, and it is
installed the way Python applications
are installed — into an environment of
its own, never loose in your system
Python. The project publishes three
official routes:

```bash
# route one: pipx, if you have it
pipx install aider-chat

# route two: the project's own installer
python -m pip install aider-install
aider-install

# route three: the one-line script
# (see the install page at aider.chat)
```

Route two is the one the project
recommends first: `aider-install`
fetches a tool called **uv** and uses
it to build Aider a private home with
its own Python, so a system Python
that is too old — this version wants
Python 3.10 to 3.12, per its package
metadata — does not stop you. Route one,
pipx, does the same job with the
isolation tool many readers will
already have from the pipx guide in
this series.

## What the lab actually did

The lab's machine had neither pipx nor
uv, and its system pip gave the modern
refusal that anyone installing Python
tools on Ubuntu or Debian will meet
sooner or later. It is worth seeing
once, quoted exactly (transcript t01):

```text
$ pip3 install aider-chat
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying
    to install.
    ...
note: If you believe this is a mistake, please contact
your Python installation or OS distribution provider.
You can override this, at the risk of breaking your
Python installation, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

That is **PEP 668**: the operating
system protecting its own Python from
being overwritten by pip. Do not pass
`--break-system-packages` — the
warning is honest. The lab took the
refusal's own advice and used a
**virtual environment**, which works
on any machine with a suitable Python:

```bash
python3 -m venv ~/aider-venv
~/aider-venv/bin/pip install aider-chat
~/aider-venv/bin/aider --version
```

The install is heavy for a command-line
tool — a little over a hundred
packages, including the LiteLLM model
library, the tree-sitter parsers that
build the repo map, and GitPython —
and it took about five and a half
minutes on the lab's small shared
machine (transcript t02). On your own
machine, expect less. With this route,
either put the venv's `bin` folder on
your `PATH`, make an alias, or call
Aider by its full path; the rest of
this guide just says `aider`.

Two first-run behaviours to know
about, both seen by the lab. Aider
checks for a newer version of itself
and fetches model information from
the network at startup; on a slow or
blocked connection that fetch can time
out, and Aider carries on with built-in
defaults and a warning (it appears in
several transcripts, and chapter 15
explains it). And Aider collects
anonymous usage analytics by default;
`aider --analytics-disable` turns them
off **permanently** — the lab did, and
every later transcript carries the
receipt line "Analytics have been
permanently disabled."

## The check

```bash
aider --version        # a version line, no errors
aider --help | head    # the usage text
```

The help output is long — over 500
lines in the lab's capture (transcript
t03) — because almost every behaviour
in this guide has a flag. You do not
need them yet. You need the version
line; everything else in the help is
there when a later chapter names it.
