<picture>
  <img src="https://github.com/userharbor/userharbor/raw/master/docs/assets/logo-full.png" alt="UserHarbor">
</picture>

# FastHTML Starter

[![License: MIT](https://img.shields.io/github/license/userharbor/fasthtml-starter)](LICENSE)
[![HTMX](https://img.shields.io/badge/HTMX-3366CC?logo=htmx&logoColor=white)](https://github.com/bigskysoftware/htmx)
[![FastHTML](https://img.shields.io/badge/FastHTML-6554C0)](https://github.com/AnswerDotAI/fasthtml)
[![Basecoat](https://img.shields.io/badge/Basecoat-18181B)](https://github.com/hunvreus/basecoat)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

[▶ Watch the presentation](presentation.mp4)

A ready-to-use template showing how easily you can build a [Hypermedia-Driven Application (HDA)](https://htmx.org/essays/hypermedia-driven-applications/) with [FastHTML](https://github.com/AnswerDotAI/fasthtml), [HTMX](https://github.com/bigskysoftware/htmx), and [UserHarbor](https://github.com/userharbor/userharbor) for authentication, authorization, and user management.

Includes registration, email verification, login, password recovery, a paginated user list, user profiles, password changes, and account deletion.

## Run locally

Use this repository as a template, then install dependencies with [uv](https://github.com/astral-sh/uv):

```bash
uv sync
cp .env.default .env
```

Set your secret key and email settings in `.env`, then start the app:

```bash
cd app
uv run --env-file ../.env uvicorn main:app --reload
```

Open <http://localhost:8000>.

For more on the approach, read [Hypermedia Systems](https://hypermedia.systems/), the free book from the creators of [HTMX](https://github.com/bigskysoftware/htmx).
