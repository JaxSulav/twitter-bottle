from bottle import post, redirect, request, response
import re
import uuid
import g

@post("/login")
def login():
    if not request.forms.get("user_email"):
        return redirect("/login?error=user_email")

    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        return redirect("/login?error=user_email")

    user_email = request.forms.get("user_email")

    if not request.forms.get("user_password"):
        return redirect(f"/login?error=user_password&user_email={user_email}")

    if not re.match(g.REGEX_PASSWORD, request.forms.get("user_password")):
        return redirect("/login?error=user_password")

    
    user_password = request.forms.get("user_password")

    for user in g.USERS:
        if user_email == user["user_email"] and user_password == user["user_password"]:
            user_session_id = str(uuid.uuid4())
            response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
            g.SESSIONS.append(user_session_id)
            response.set_cookie("session_id", user_session_id)
            return redirect("/tweets")
    return redirect("/tweets")