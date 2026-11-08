from fasthtml.common import FT, H3, A, Div, Header, Img, Li, Nav, Section, Span, Ul
from fasthtml_basecoat import Button, Sidebar
from fasthtml_lucide import Icon


def DashboardSidebar(*, active_path: str = "/") -> FT:
    return Sidebar(
        Nav(
            Header(
                A(
                    Img(src="/static/logo.png", cls="size-12"),
                    Span("UserHarbor", cls="font-semibold text-xl"),
                    href="/",
                    cls="flex min-w-0 items-center gap-3 rounded-md p-2",
                ),
                Button(
                    Icon("x"),
                    type="button",
                    variant="ghost",
                    size="icon",
                    cls="absolute top-4 right-2 md:hidden",
                    aria_label="Close sidebar",
                    aria_controls="dashboard-sidebar",
                    onclick="document.getElementById('dashboard-sidebar').close()",
                ),
                cls="relative",
            ),
            Section(
                Div(
                    H3("Workspace", id="dashboard-navigation-label"),
                    Ul(
                        Li(
                            A(
                                Icon("layout-dashboard"),
                                Span("Users"),
                                href="/",
                                aria_current="page" if active_path == "/" else None,
                            ),
                        ),
                    ),
                    role="group",
                    aria_labelledby="dashboard-navigation-label",
                ),
                cls="scrollbar-sm",
            ),
            aria_label="Dashboard navigation",
        ),
        id="dashboard-sidebar",
        side="left",
    )
