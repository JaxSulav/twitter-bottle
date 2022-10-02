from bottle import get, view, redirect, request
import sqlite3
from models.user import find_session_id

@get("/login")
@view("index")
def login():
    # Redirect to /tweets page if already logged in
    user_session_id = request.get_cookie("session_id")
    con = sqlite3.connect('bottle.db')
    queryset = find_session_id(con, user_session_id)
    if queryset:
        con.close()
        return redirect("/tweets")
    con.close()
    return