# The Moving Parts

By the end of this chapter you can
name each piece of an Aider session
and say which piece a given surprise
belongs to. The check, when you reach
chapter 5: the startup banner lists
most of these parts on its own lines —
you should be able to point at each
line and name the part below that it
belongs to.

Aider looks like one program, but a
working session has **six parts**, and
they fail in six different ways.

**The chat.** The prompt you type
into. It keeps the session's history,
accepts your requests in plain words,
and understands about forty **slash
commands** — instructions to Aider
itself, not to the model: `/add`,
`/undo`, `/run` and their kin. The lab
captured the full list from the tool's
own `/help` (transcript t07); chapter
6 introduces the ones for files, and
the rest appear as they earn their
place.

**The model.** The large language
model that actually reads, reasons and
writes code. It is not inside Aider —
it lives at a cloud provider or in a
local server such as Ollama, and
Aider talks to it through a library
called **LiteLLM**, which is why one
tool can speak to hundreds of models
with the same commands. When this
guide says "the model decided", it
means that remote brain; when it says
"Aider decided", it means the local
program. The distinction decides where
to look when something odd happens.

**The files in context.** The model
can only edit what it can see in
full. Files you name on the command
line or add with `/add` are in the
chat as **editable**; files added with
`/read-only` are visible but fenced
off. Everything costs **tokens** — the
chunks of text models read and write —
and the context window is finite, so
choosing files is a real decision, not
a formality. Chapter 6.

**The repo map.** For everything in
your git repository that is *not* in
the chat, Aider builds a **map**: each
file reduced to its shape — class and
function names, the signatures that
matter — ranked so the most-referenced
pieces survive when the map must be
trimmed to its token budget. The map
is how the model knows your project
has a `water_litres` function without
you pasting it. The lab watched the
map being built and measured it;
chapter 7.

**The edit format.** Models do not
edit files; they produce text, and
Aider must turn that text into changes
on disk. The **edit format** is the
contract for that text: rewrite the
whole file, or send search-and-replace
blocks, or send a diff. Aider picks a
default per model — the lab's local
model was given the whole-file format,
a frontier cloud model the diff
format — because weaker models follow
simpler contracts more reliably.
Chapter 9.

**Git.** Underneath everything, the
repository. Aider requires one (it
will offer to create it), commits each
set of model edits with its own
message, commits your uncommitted
work first if it has to touch dirty
files, and offers `/undo` for its own
latest step. Your `.gitignore` is
respected — and, as the lab saw,
actively defended: Aider adds its own
housekeeping files and your `.env` to
it. Chapter 10.

Around the six parts sit two quieter
mechanisms worth knowing now.
**Configuration** — command-line
flags, a `.aider.conf.yml` file, and
environment variables, all saying the
same settings in three places —
chapter 11. And the **weak model**: a
second, smaller model Aider uses for
cheap side jobs such as writing commit
messages, so the expensive model is
only billed for the real work. It
appears in the banner's family of
settings as `--weak-model`, and in
chapter 10 where the messages are
written.
