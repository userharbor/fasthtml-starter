from components.alert import Alert
from core.harbor import harbor
from core.types import HTMLResult
from fasthtml.common import Response, fast_app
from userharbor.exceptions import UserHarborError

account_app, rt = fast_app()


@rt(methods=["POST"])
def change_password(
    request, old_password: str, new_password: str, confirm_password: str
) -> HTMLResult:
    if new_password != confirm_password:
        return Alert(
            "Password Change Failed", "Passwords do not match.", variant="error"
        )
    try:
        harbor.change_password(
            old_password=old_password,
            new_password=new_password,
            session_token=request.cookies.get("session_token", ""),
        )
    except UserHarborError as e:
        return Alert("Password Change Failed", str(e), variant="error")
    response = Response(headers={"HX-Redirect": "/auth/"})
    response.delete_cookie("session_token", path="/")
    return response


@rt(methods=["POST"])
def delete(request, password: str, confirmed: bool = False) -> HTMLResult:
    if not confirmed:
        return Alert(
            "Account Deletion Failed",
            "Confirm account deletion first.",
            variant="error",
        )
    try:
        harbor.delete_account(
            password=password,
            session_token=request.cookies.get("session_token", ""),
        )
    except UserHarborError as e:
        return Alert("Account Deletion Failed", str(e), variant="error")
    response = Response(headers={"HX-Redirect": "/auth/"})
    response.delete_cookie("session_token", path="/")
    return response
