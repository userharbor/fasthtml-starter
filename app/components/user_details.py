from fasthtml.common import FT, H2, Div, Form, Header, P, Section, Tbody, Td, Tr
from fasthtml_basecoat import Button, Card, Checkbox, Input, Label, Table
from userharbor.interfaces import UserLike


def UserDetailsCard(user: UserLike) -> FT:
    return Card(
        Header(H2("User details")),
        Section(
            Table(
                Tbody(
                    Tr(
                        Td("Username", cls="font-semibold"),
                        Td(user.username),
                    ),
                    Tr(
                        Td("Email", cls="font-semibold"),
                        Td(user.email),
                    ),
                    Tr(
                        Td("Verified", cls="font-semibold"),
                        Td("Yes" if user.verified else "No"),
                    ),
                ),
            ),
        ),
    )


def ChangePasswordCard() -> FT:
    return Card(
        Header(
            H2("Change password"),
            P("You will need to log in again after changing your password."),
        ),
        Section(
            Form(
                Div(
                    Label("Current password", fr="old-password"),
                    Input(
                        type="password",
                        id="old-password",
                        name="old_password",
                        autocomplete="current-password",
                        required=True,
                    ),
                    cls="grid gap-2",
                ),
                Div(
                    Label("New password", fr="new-password"),
                    Input(
                        type="password",
                        id="new-password",
                        name="new_password",
                        autocomplete="new-password",
                        required=True,
                    ),
                    cls="grid gap-2",
                ),
                Div(
                    Label("Confirm password", fr="confirm-password"),
                    Input(
                        type="password",
                        id="confirm-password",
                        name="confirm_password",
                        autocomplete="new-password",
                        required=True,
                    ),
                    cls="grid gap-2",
                ),
                Button("Change password", type="submit"),
                id="change-password-form",
                hx_post="/account/change_password",
                hx_disabled_elt="#change-password-form input, #change-password-form button",
                hx_swap="none",
                cls="grid gap-6",
            ),
        ),
    )


def DeleteAccountCard() -> FT:
    return Card(
        Header(H2("Delete account"), P("Deleting your account is permanent.")),
        Section(
            Form(
                Div(
                    Label("Current password", fr="delete-password"),
                    Input(
                        type="password",
                        id="delete-password",
                        name="password",
                        autocomplete="current-password",
                        required=True,
                    ),
                    cls="grid gap-2",
                ),
                Div(
                    Label(
                        Checkbox(
                            name="confirmed",
                            value="true",
                            required=True,
                            onchange="this.form.querySelector('button[type=submit]').disabled = !this.checked",
                        ),
                        "I understand that my account will be permanently deleted.",
                        cls="flex items-center gap-2",
                    ),
                ),
                Button(
                    "Delete account",
                    type="submit",
                    variant="destructive",
                    disabled=True,
                ),
                id="delete-account-form",
                hx_post="/account/delete",
                hx_disabled_elt="#delete-account-form input, #delete-account-form button",
                hx_swap="none",
                cls="grid gap-6",
            ),
        ),
    )
