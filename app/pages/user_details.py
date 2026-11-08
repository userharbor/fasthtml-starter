from components.user_details import (
    ChangePasswordCard,
    DeleteAccountCard,
    UserDetailsCard,
)
from core.types import User
from fasthtml.common import FT
from layouts.dashboard import DashboardLayout
from userharbor.interfaces import UserLike


def UserDetailsPage(profile: UserLike, user: User) -> FT:
    is_owner = profile.username == user.username
    return DashboardLayout(
        UserDetailsCard(profile),
        (ChangePasswordCard(), DeleteAccountCard()) if is_owner else None,
        title=profile.username,
        user=user,
    )
