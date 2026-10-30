# Connecting a Model

By the end of this chapter Aider has a
model to talk to — or you know exactly
which door is closed and why. The
check is the startup banner: start
Aider inside any git repository and
read its second line. When a model is
connected, it names it:

```text
Aider v0.86.2
Model: ollama/llama3.2 with whole edit format
```

That banner is real (transcript t06) —
but the lab's story has a twist, told
below: the banner printed, and no
model ever answered. Read this chapter
as the map of doors, with the lab's
footprints showing which ones it could
open.

## Door one: a cloud API key

The standard route. Sign up with a
model provider — OpenAI, Anthropic,
Google, OpenRouter and many more —
create an **API key**, and put it in
your environment:

```bash
export OPENAI_API_KEY=...your key...
# or
export ANTHROPIC_API_KEY=...your key...
aider --model gpt-5            # or anthropic/claude-sonnet-4-5
```

Model names are `provider/model`, and
you can ask which names Aider knows:

```bash
aider --models ollama     # every name matching "ollama"
aider --models gpt-5      # every name matching "gpt-5"
```

Both listings are real (transcript
t04) — they come from Aider's built-in
model registry, and no account is
needed to read them. One warning from
the lab before you try it: **run that
command inside a git repository.** In
a bare folder Aider first asks whether
to create a repository, and a scripted
or piped run will sit waiting on that
question instead of answering (the lab
lost a few minutes to exactly this;
chapter 15 has the details).

A `.env` file in the project folder is
the other sanctioned place for keys —
chapter 11 covers it, including the
pleasant detail that Aider adds `.env`
to your `.gitignore` the moment it
sees one, so the key cannot be
committed by accident (transcript
t10). Keys never belong in the chat
itself: anything you type at the
prompt goes to the model, and the chat
history is saved to a file.

## Door two: a local model

Run a model on your own machine with
Ollama (its own guide in this series
covers installing it and pulling
models), tell Aider where it lives,
and name the model:

```bash
export OLLAMA_API_BASE=http://127.0.0.1:11434
aider --model ollama/llama3.2
```

No key, no account, no cost per
question, and your code never leaves
the machine. The trade is quality and
speed: a model small enough to run at
home is a weaker programmer than the
frontier cloud models, and chapter 9's
edit formats exist largely to help it
succeed anyway. Aider accepts any
OpenAI-compatible endpoint the same
way, so other local servers work too.

## Door three: the one the lab met

The lab had no key and no Ollama
server. Here is what Aider does then,
verbatim (transcript t05):

```text
$ aider --message "Say hello" garden.py
No LLM model was specified and no API keys were provided.
OpenRouter provides free and paid access to many LLMs.

Please open this URL in your browser to connect Aider with OpenRouter:

https://openrouter.ai/auth?callback_url=http://localhost:8484/callback/aider&...

Waiting up to 5 minutes for you to finish in the browser...
```

With no model specified and no keys
found, Aider offers a **sign-in with
OpenRouter**, a broker that fronts
many providers, some of them free. It
is a reasonable offer — and it is
still creating an account, with a
browser and terms of service, so the
lab declined it and stopped the wait.
The lesson stands either way: **no
model, no Aider.** Everything else in
this guide is the machinery around a
conversation the lab could prepare for
but not hold.

Pointing Aider at a local endpoint
that is not there shows the other
failure shape (transcript t06). The
banner prints in full — model, edit
format, repo map, files added — and
then the send fails:

```text
litellm.APIConnectionError: OllamaException - [Errno 111] Connection refused
Retrying in 0.2 seconds...
litellm.APIConnectionError: OllamaException - [Errno 111] Connection refused
Retrying in 0.5 seconds...
```

nine attempts in all, the pause
doubling each time up to 32 seconds,
before Aider gives up. So a dead
endpoint costs about a minute, not a
crash — and "Connection refused" in
that first line is the whole
diagnosis: nothing is listening at the
address in `OLLAMA_API_BASE`. Check
the server is running and the model is
pulled before blaming Aider.
