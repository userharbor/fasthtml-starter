from core.harbor import harbor
from core.types import HTMLResult
from fasthtml.common import HTTPException, fast_app
from pages.user_details import UserDetailsPage
from pages.users import UsersPage

users_app, rt = fast_app()


@rt
def index(request, page: int = 1) -> HTMLResult:
    page_size = 10
    page = max(1, page)
    users = harbor.users.list(limit=page_size, offset=(page - 1) * page_size)
    total_pages = max(1, (users.total + page_size - 1) // page_size)
    if page > total_pages:
        page = total_pages
        users = harbor.users.list(limit=page_size, offset=(page - 1) * page_size)
    return UsersPage(users, request.scope.get("user"), page, total_pages)


@rt("/users/{username}", methods=["GET"])
def details(request, username: str) -> HTMLResult:
    profile = harbor.users.get_by_username(username)
    if profile is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDetailsPage(profile, request.scope["user"])
