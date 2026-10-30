# Limits

What Aider cannot do, collected in one
place. Several of these were met by
the lab personally; the rest are
stated by the project or follow from
its design.

**No model, no edits.** Aider contains
no intelligence of its own. Without an
API key, an account, or a local model
server, it can show you its help, its
model registry, its repo map and its
session commands — the lab proved all
of those — and it cannot change one
line of code for you. The tool is a
harness; the horse is yours to bring.

**Quality is the model's, plus your
context.** Aider's benchmarks of
models on real editing tasks vary
widely by model, and your results will
too. A weak model in whole-file mode
can drop a function while rewriting a
file; a strong one in diff mode can
still misunderstand the request.
Aider gives the model every chance —
map, conventions, test loops — and
cannot give it judgment. Yours is the
only review in the loop.

**Undo is narrower than it sounds.**
`/undo` reverses commits Aider made
from model edits in the *current*
session. It does not reverse
`/commit` commits, other sessions'
work, or anything you did in your
editor — the lab hit this wall twice
and chapter 10 quotes it. Git itself
can unwind those, with git's usual
care requirements.

**Edits are text-shaped.** The edit
formats move text. Renames across a
codebase, generated files, binary
assets, database migrations with live
data — Aider will attempt what the
model proposes, but its safety story
(small commits, readable diffs) is
built for source code, and thins out
quickly beyond it.

**Context is finite and priced.**
Every file in the chat and the repo
map are re-sent with each request.
Long sessions on large projects cost
real money on cloud models and real
patience on local ones, and a model
with a small window will quietly have
less of your project in mind than you
assume. `/tokens` tells the truth;
check it (chapter 7).

**It works one request at a time, in
the open.** Aider is a supervised
pair, not a background workforce: no
queues of tasks, no working while you
sleep, no judgement about which of
your requests matter. Sessions are
also single-repository affairs.

**The network is touched even when
the model is local.** Startup checks
for updates and refreshes model
information online, and analytics are
on unless disabled (chapter 3). On an
air-gapped machine expect warnings and
defaults, not silence — the lab's
transcripts show the fetch timing out
and Aider carrying on.

**Failure can be slow.** A dead
endpoint is retried with doubling
pauses — about a minute before the
tool gives up (chapter 4). A model
that returns unparseable edits is
asked again, and again. These are the
right instincts for flaky services and
the wrong feel for a tool you expected
to answer instantly; knowing they are
coming is most of the cure.
