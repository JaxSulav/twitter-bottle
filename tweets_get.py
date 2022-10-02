from bottle import get, redirect, request, response, view
import g
import sqlite3
from models.tweets import get_all_tweets

from models.user import find_session_id


############## RENDERS TWEETS PAGE ###############################
@get("/tweets")
@view("tweets")
def tweets():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    user_session_id = request.get_cookie("session_id")
    con = sqlite3.connect('bottle.db')
    queryset = find_session_id(con, user_session_id)
    if not queryset:
        return redirect("/login")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
    user_name = request.forms.get("user_name")

    tweets = get_all_tweets(con, user_email)
    con.close()
    
    return dict(user_email=user_email, user_name=user_name, tabs=g.TABS, tweets=tweets, trends=g.TRENDS, items=g.ITEMS, users=g.USERS)