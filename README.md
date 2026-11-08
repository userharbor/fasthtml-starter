<a href="https://github.com/userharbor/userharbor">
  <picture>
    <img src="https://github.com/userharbor/userharbor/raw/master/docs/assets/logo-full.png" alt="UserHarbor">
  </picture>
</a>

[![License: MIT](https://img.shields.io/github/license/userharbor/fasthtml-starter)](LICENSE)
[![HTMX](https://img.shields.io/badge/HTMX-3366CC?logo=htmx&logoColor=white)](https://github.com/bigskysoftware/htmx)
[![FastHTML](https://img.shields.io/badge/framework-FastHTML-7854F7)](https://github.com/AnswerDotAI/fasthtml)
[![Basecoat](https://img.shields.io/badge/UI-Basecoat-18181B)](https://basecoatui.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/badge/linting-Ruff-black?logo=ruff&logoColor=black)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

https://github.com/user-attachments/assets/1bcafdda-fe51-4bb3-a3e7-cb1302952d13

A ready-to-use template showing how easily you can build a [Hypermedia-Driven Application (HDA)](https://htmx.org/essays/hypermedia-driven-applications/) with [FastHTML](https://github.com/AnswerDotAI/fasthtml), [HTMX](https://github.com/bigskysoftware/htmx), and [UserHarbor](https://github.com/userharbor/userharbor) for authentication, authorization, and user management.

Includes registration, email verification, login, password recovery, a paginated user list, user profiles, password changes, and account deletion.

For a step-by-step guide, follow the [FastHTML Application with UserHarbor tutorial](https://userharbor.github.io/tutorials/fasthtml-application/).

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
