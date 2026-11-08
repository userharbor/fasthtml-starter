from components.pagination import Pagination
from components.user_table import UserTable
from core.types import User
from fasthtml.common import FT
from layouts.dashboard import DashboardLayout
from userharbor.interfaces import UserList


def UsersPage(users: UserList, user: User, page: int, total_pages: int) -> FT:
    return DashboardLayout(
        UserTable(users),
        Pagination(page, total_pages),
        title="Users",
        user=user,
    )
