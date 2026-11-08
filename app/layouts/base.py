from pathlib import Path

from fasthtml.common import (
    FT,
    Body,
    Div,
    Head,
    Html,
    Link,
    Meta,
    Script,
    Title,
)
from fasthtml_basecoat import (
    BasecoatInput,
    BasecoatJS,
    Spinner,
)
from fasthtml_tailwindcss import TailwindHead

ASSETS_ROOT = Path(__file__).parent.parent


def BaseLayout(*c, title: str, **kwargs) -> FT:
    return Html(
        Head(
            Title(title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="icon", type="image/x-icon", href="/static/favicon.ico"),
            Script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.11/dist/htmx.js"),
            BasecoatJS(),
            TailwindHead(input=BasecoatInput("nova"), watch=True),
        ),
        Body(
            Spinner(
                id="global-spinner",
                cls="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-50 pointer-events-none size-10 htmx-indicator",
            ),
            Div(
                id="alerts",
                cls="fixed top-4 inset-x-0 z-50 flex flex-col items-center gap-4",
            ),
            *c,
            hx_boost="true",
            hx_indicator="#global-spinner",
        ),
        **kwargs,
    )
