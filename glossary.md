# Glossary

**API key** — the secret token a model
provider issues to your account; Aider
presents it with each request and the
provider bills or admits you by it.
Lives in the environment or a `.env`
file, never in the chat.

**Architect / editor** — the two-model
split of chapter 8: the architect
plans a change in words, the editor
turns the plan into edits.

**Banner** — the lines Aider prints at
startup naming its version, the model
and edit format in force, the git
repository, the repo-map budget and
the files added.

**Chat mode** — how a message is
handled: *code* (edits happen), *ask*
(answers only), *context* (gathering
relevant code), or *architect* (plan,
then edit).

**Commit** — a saved step in a git
repository. Aider makes one for each
set of model edits, and one for your
uncommitted work before it edits a
dirty file (a **dirty commit**).

**CONVENTIONS.md** — a file of standing
rules for the model, loaded read-only
into every session (chapter 11).

**Context** — everything the model is
shown with a request: the files in the
chat, the repo map, the conversation
history and the system instructions.

**Edit format** — the contract for how
the model's changes are written:
*whole* files, *diff* search-and-
replace blocks, *udiff* patches, and
the *editor-* variants (chapter 9).

**In the chat** — said of a file whose
full contents are in the context,
either *editable* or *read-only*.

**LiteLLM** — the library Aider uses
to talk to hundreds of model providers
through one interface; why a model
name is written `provider/model`.

**Repo map** — the ranked skeleton of
signatures and definitions for every
file in the repository, sent with each
request so the model knows the project
beyond the files in the chat
(chapter 7).

**Slash command** — an instruction to
Aider itself typed at the prompt and
beginning with `/`: `/add`, `/undo`,
`/run` and about forty more.

**Token** — the chunk of text (roughly
three-quarters of a word, for English
code and prose) that models read and
write in units of; context size and
cloud prices are both counted in them.

**Weak model** — the second, smaller
model Aider uses for cheap side jobs
such as writing commit messages.

**Whole edit format** — see *edit
format*: the model returns each
changed file complete.
