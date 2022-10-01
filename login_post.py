from bottle import post, redirect, request, response
import re
import uuid
import g
import sqlite3
from models.user import find_user, insert_session

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

    con = sqlite3.connect('bottle.db')
    queryset = find_user(con, user_email)
    if queryset:
        if user_email == queryset[0][0] and user_password == queryset[0][1]:
            user_session_id = str(uuid.uuid4())
            response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
            insert_session(con, user_session_id, user_email)
            con.commit()
            response.set_cookie("session_id", user_session_id)
            con.close()
            return redirect("/tweets")
        else:
            con.close()
            return "Username and password do not match !!"
    else:
        con.close()
        return "User not found !!"