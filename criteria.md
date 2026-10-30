# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's project is an invented garden planner.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 14 names what the tool
   cannot do: nothing at all without a model the reader
   supplies, quality bounded by that model, an `/undo` narrower
   than its description suggests, text-shaped edits, finite and
   priced context, supervised one-request-at-a-time work, and
   failure modes that take a minute to fail.
8. **The ethics rule is in the text, early.** Aider writes to
   your files and commits to your repository under the
   direction of a model you do not control, so chapter 1 and
   the README state the guardrails before any procedure depends
   on them — work in a committed repository, review the diffs,
   keep keys in the environment or a `.env` file and never in
   the chat — and chapter 14 repeats the review duty plainly.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran. Aider **0.86.2** was
installed unmodified from PyPI. The lab's practice project is
an invented three-file Python program, `garden-planner`
(kept in `aider-lab/garden-planner/`), in a git repository the
lab created for the purpose.

**The lab had no model.** It held no API key, ran no local
model server, and created no accounts — the one free route
Aider offered on its own (a browser sign-in with OpenRouter)
was declined at the point it asked for one, and the transcript
shows the stopping. Every claim in this guide is therefore in
one of two classes, and the chapters keep them apart: what
Aider does *around* a conversation was run for real and is
evidenced below; the conversation itself — a model reading,
answering and editing — was never held, and everything about
it is taught from Aider's own documentation and help text and
labelled documented-only. No chat transcript in this guide is
real except the command sessions quoted from the lab, and
none is presented as anything else. All keys used anywhere in
the lab were deliberately fake strings, labelled as such,
which no system accepted as genuine.

Run for real, with transcripts as evidence
(`aider-lab/transcripts/`):

- The PEP 668 refusal of a system-wide pip install, verbatim
  (t01); the working route — a Python venv and
  `pip install aider-chat`, about 120 packages, roughly five
  and a half minutes on the shared machine (t02);
  `aider --version` reporting 0.86.2, and the full 525-line
  `--help` (t03).
- `aider --models ollama` and `aider --models gpt-5` listing
  the registry's matching names with no account (t04) — and
  the same command outside a git repository, which stops at
  Aider's create-a-repository question instead.
- First contact in a fresh repository: Aider added `.aider*`
  to `.gitignore` unprompted (t04, t12).
- The no-model behaviour, verbatim: "No LLM model was
  specified and no API keys were provided", followed by the
  OpenRouter sign-in offer and its five-minute browser wait,
  which the lab stopped without creating an account (t05).
- A session aimed at an Ollama endpoint with nothing
  listening: the startup `OllamaError`, the complete banner
  (whole edit format, repo map at 1024 tokens), and nine
  `APIConnectionError` retries with pauses doubling from 0.2
  to 32 seconds before Aider gave up (t06).
- The in-chat `/help`: all 43 commands of 0.86.2 with their
  one-line descriptions, quoted throughout the guide (t07).
- A working command session against the dead endpoint: `/ls`
  splitting repo files from chat files, `/map` printing the
  real repo map, `/tokens` accounting for the context
  (450 system + 129 map + 361 file = 940 tokens), `/add`,
  `/run python3 -m unittest` executing the project's suite
  inside the chat and keeping its output there, `/drop`,
  `/exit` (t08).
- Configuration pickup, proved rather than asserted: a
  project `.aider.conf.yml` naming the model and
  `map-tokens: 512` changed the banner of a flagless run to
  that model and that budget (t09).
- `.env` handling: Aider added the new `.env` to `.gitignore`
  itself, and with a deliberately fake key inside it and an
  otherwise empty environment, startup proceeded past the
  no-keys state to the full banner (t10). The provider's
  verdict on the fake key did not arrive within the lab's
  network timeout, so no claim is made about it.
- `aider --show-repo-map` printing the whole map of the
  practice project with no chat and no model (t11).
- The files Aider writes into a repository — chat history,
  input history, tag cache — and `git status` staying clean
  of all of them (t12).
- Edit-format selection read from real banners: whole for
  `ollama/llama3.2` and for `gpt-4o-mini`, diff for
  `anthropic/claude-sonnet-4-5`, and an explicit
  `--edit-format diff` overriding the local model's default
  (t13). One further banner, for `gpt-5`, did not print
  inside 45 seconds on the shared machine, and the guide
  claims nothing about its default.
- `/commit` with a human-supplied message committing an
  outside edit — commit `1f3460b`, verified in `git log`
  (t15).
- `/undo` refusing, verbatim, in a later session and in the
  same session as the `/commit`: it covers only commits
  Aider made from model edits in the current session
  (t16, t17).

Documented only — described from the project's documentation
and the tool's own help text, not run, and the text does not
claim otherwise:

- Every actual model conversation: requests, answers, and
  edits applied in code mode; ask, context and architect
  modes in operation; the plan-approval step; the model
  asking for files to be added.
- Auto-commits after model edits, weak-model commit messages,
  dirty commits, and `/undo` succeeding on a model-made
  commit.
- `/test` and `--auto-test`/`--auto-lint` behaviour with a
  failing suite (the underlying `/run` machinery is verified;
  the failing-test loop is not), and `/lint` fixing.
- `CONVENTIONS.md` changing a model's behaviour.
- Account creation with any provider, the OpenRouter sign-in
  completing, and every judgement about which model writes
  good code or what real work costs.
- The neighbour tools of chapter 13 — characterised, not run
  or benchmarked.

Fixtures are this guide's own and deliberately generic: a
vegetable-bed planner with three functions and three tests,
an author named "Lab" at example.org, and keys that are
labelled fakes. No real project, person, organisation or
credential appears anywhere in the lab.
