from bottle import get, redirect, request
import g



############## LOGOUT ###############################
@get("/logout")
def logout():
    user_session_id = request.get_cookie("session_id")
    g.SESSIONS.remove(user_session_id)
    return redirect("/login")
