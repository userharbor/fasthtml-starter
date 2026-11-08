from urllib.parse import quote

from fasthtml.common import FT, A, Tbody, Td, Th, Thead, Tr
from fasthtml_basecoat import Table
from userharbor.interfaces import UserList


def UserTable(users: UserList) -> FT:
    return Table(
        Thead(
            Tr(
                Th("Username"),
                Th("Email"),
                Th("Verified"),
            )
        ),
        Tbody(
            *[
                Tr(
                    Td(
                        A(
                            u.username,
                            href=f"/users/{quote(u.username, safe='')}",
                            cls="hover:underline",
                        )
                    ),
                    Td(u.email),
                    Td("Yes" if u.verified else "No"),
                )
                for u in users.items
            ]
        ),
    )
