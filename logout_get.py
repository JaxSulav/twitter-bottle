from bottle import get, redirect, request
import g, sqlite3

from models.user import delete_session_id



############## LOGOUT ###############################
@get("/logout")
def logout():
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
    user_session_id = request.get_cookie("session_id")
    con = sqlite3.connect('bottle.db')
    success = delete_session_id(con, user_session_id, user_email)
    con.commit()
    con.close()
    if success:
        return redirect("/login")
    return "Could not logout !!"
