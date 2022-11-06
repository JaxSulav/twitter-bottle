
from ast import arg
from platform import architecture
from bottle import Bottle, default_app, delete, error, get, post, put, redirect, response, run,  request, static_file, view, route
import jwt
import g
import re
import uuid
import json

import logout_get
import tweets_get
import login_get
import api_create_user_get
import admin_get


import api_create_tweet_post
import login_post

import os
import sqlite3
import argparse
from models.user import create_user_model, create_session_model, find_session_id
from models.tweets import create_tweet_like_model, create_tweet_model, delete_tweet, update_tweet
from api import api_tweets_others

app = Bottle()


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./views/static/')

@post('/api_update_tweet')
def tweet_update():
    tweet_text = request.forms.get("tweet_text", "")
    print("TEXT: ", tweet_text)
    tweet_id = request.forms.get("tweet_id", "")
    if len(tweet_text) < 1 or len(tweet_text) > 100:
        response.status = 400
        return "tweet_text invalid"

    con = sqlite3.connect('bottle.db')
    data = {
        "tweet_id": tweet_id,
        "text": tweet_text,
    }
    success = update_tweet(con, **data)
    con.close()
    if not success:
        return "Could not update the tweet !!"
        
    return "Tweet Updated"


####################################################

@delete("/api-delete-tweet/<tweet_id>")
def _(tweet_id):
    con = sqlite3.connect('bottle.db')
    success = delete_tweet(con, tweet_id)

    if success:
        print(f"Tweet with tweet_id {tweet_id} deleted")
    else:
        print(f"Tweet with tweet_id {tweet_id} deletion failed")
    con.close()


############## युजर मेटाउछ ###############################
@delete("/delete-user/<user_id>")
def delete_user(user_id):
    print("*"*30)
    print(g.USERS)
    user_id = request.forms.get("user_id")
    for index, user in enumerate(g.USERS):
        if user["user_id"] == user_id:
            g.USERS.pop(index)
            return redirect("/users")
    print("#"*30)        
    print(g.USERS)
    response.status = 204
    return redirect("/users")




############## ERROR DISPLAY ###############################
@error(404)
@view("404")
def _(error):
    print(error)
    return

@get("/409")
@view("409")
def _():
    pass

############## RENDERS INDEX PAGE ###############################
@get("/")
@view("index")
def index():
    # Send to tweets page if already logged in
    user_session_id = request.get_cookie("session_id")
    con = sqlite3.connect('bottle.db')
    queryset = find_session_id(con, user_session_id)
    con.close()
    if queryset:
        return redirect("/tweets")
    return

############## युजर बनाउछ ###############################
@get("/users")
@view("users")
def get_all_users():
    return dict(users=g.USERS)


#############################################
@get("/api-create-user")
@view("users")
def get_users():
    return

#############################################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

#############################################
@get("/images/<image_name>")
def _(image_name):
    return static_file(image_name, root="./images")
#############################################
@get("/app.js")
def _():
    return static_file("app.js", root=".")

#############################################
@get("/validator.js")
def _():
    return static_file("validator.js", root=".")

#############################################


def parse_args():
    """ Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Twitter Clone.')
   
    parser.add_argument("option", help="Option for run conditions")
    return parser.parse_args()


def migrate_db():
    con = sqlite3.connect('bottle.db')
    create_user_model(con)
    create_session_model(con)
    create_tweet_model(con)
    create_tweet_like_model(con)
    con.commit()
    con.close()


if __name__ == '__main__':
    args = parse_args()
    if args.option == "migrate":
        migrate_db()
    if args.option == "runserver":
        try:
            import production
            application = default_app()
        except:
            run(host='0.0.0.0', port=2222, debug=True, reloader=True, server="paste")
