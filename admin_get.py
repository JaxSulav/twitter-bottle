from bottle import get, request, view, route, template, redirect
from models.tweets import get_tweets_for_admin
from models.user import get_users_for_admin
import sqlite3

############## RENDERS ADMIN PAGE###############################
@get("/admin/users")
@route("admin-css/users")
def users():
    con = sqlite3.connect('bottle.db')
    users = get_users_for_admin(con)
    all_users = list()
    for user in users:
        all_users.append(list(user))
    return template("admin-css/users", users=all_users) 

@get("/admin/tweets")
@route("admin-css/tweets")
def tweets():
    con = sqlite3.connect('bottle.db')
    tweets = get_tweets_for_admin(con)
    all_tweets = list()
    for tweet in tweets:
        all_tweets.append(list(tweet))
    return template("admin-css/tweets", tweets=all_tweets) 

@get("/admin")
def admin():
    return redirect("/admin/users")