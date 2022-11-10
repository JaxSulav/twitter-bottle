from bottle import get, redirect, request, response, view
import g
import sqlite3
from models.tweets import find_tweet_like, get_all_tweets, get_tweets_by_user_id, find_tweet_like
from models.user import find_session_id, find_user, get_all_users


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
    users = get_all_users(con)[:5]
    all_users = []
    for user in users:
        all_users.append(list(user))
    con.close()
    
    return dict(user_email=user_email, user_name=user_name, tabs=g.TABS, tweets=tweets, trends=g.TRENDS, items=all_users, users=g.USERS)

@get("/profile")
@view("profile")
def users():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    user_session_id = request.get_cookie("session_id")
    con = sqlite3.connect('bottle.db')
    queryset = find_session_id(con, user_session_id)
    if not queryset:
        return redirect("/login")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
    user_name = request.forms.get("user_name")
    id = int(request.GET.get('id', '').strip())

    tweets = get_tweets_by_user_id(con, id)
    all_tweets = list()
    data = {
        "tweet_id": None,
        "user_image": None,
        "user_username": None,
        "user_first_name": None,
        "user_last_name": None,
        "tweet_text": None,
        "tweet_image": None,
        "tweet_like": None,
        "liked": False
    }
    for tweet in tweets:
        data["tweet_id"] = tweet[0] if tweet[0] else None
        data["user_image"] = tweet[1] if tweet[1] else None
        data["user_username"] = tweet[2] if tweet[2] else None
        data["user_first_name"] = tweet[3] if tweet[3] else None
        data["user_last_name"] = tweet[4] if tweet[4] else None
        data["tweet_text"] = tweet[5] if tweet[5] else None
        data["tweet_image"] = tweet[6] if tweet[6] else None
        data["tweet_like"] = tweet[7] if tweet[7] else None
        data["tweet_date"] = tweet[8] if tweet[8] else None
        data["user_email"] = tweet[9] if tweet[9] else None

        q = find_tweet_like(con,  tweet[0], user_email)
        if q:
            data["liked"] = True
        else:
            data["liked"] = False

        all_tweets.append(data)


    users = get_all_users(con)[:5]
    all_users = []
    for user in users:
        all_users.append(list(user))
    con.close()
    
    print("ALL: ", all_tweets)
    return dict(user_email=user_email, user_name=user_name, tabs=g.TABS, tweets=all_tweets, trends=g.TRENDS, items=all_users, users=g.USERS, profile=all_tweets[0])


@get("/user-profile")
@view("profile")
def user_profile():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    user_session_id = request.get_cookie("session_id")
    con = sqlite3.connect('bottle.db')
    queryset = find_session_id(con, user_session_id)
    if not queryset:
        return redirect("/login")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
    user_name = request.forms.get("user_name")

    q = find_user(con, user_email)
    id = q[0][2]
    user_image = q[0][6]
    user_first_name = q[0][4]
    user_last_name = q[0][5]
    username = q[0][3]

    tweets = get_tweets_by_user_id(con, id)
    all_tweets = list()
    data = {
        "tweet_id": None,
        "user_image": None,
        "user_username": None,
        "user_first_name": None,
        "user_last_name": None,
        "tweet_text": None,
        "tweet_image": None,
        "tweet_like": None,
        "user_email": None,
        "liked": False
    }
    for tweet in tweets:
        data["tweet_id"] = tweet[0] if tweet[0] else None
        data["user_image"] = tweet[1] if tweet[1] else None
        data["user_username"] = tweet[2] if tweet[2] else None
        data["user_first_name"] = tweet[3] if tweet[3] else None
        data["user_last_name"] = tweet[4] if tweet[4] else None
        data["tweet_text"] = tweet[5] if tweet[5] else None
        data["tweet_image"] = tweet[6] if tweet[6] else None
        data["tweet_like"] = tweet[7] if tweet[7] else None
        data["tweet_date"] = tweet[8] if tweet[8] else None
        data["user_email"] = tweet[9] if tweet[9] else None

        q = find_tweet_like(con,  tweet[0], user_email)
        if q:
            data["liked"] = True
        else:
            data["liked"] = False

        all_tweets.append(data)


    users = get_all_users(con)[:5]
    all_users = []
    for user in users:
        all_users.append(list(user))
    con.close()

    if len(all_tweets) <= 0:
        num_tweets = {
            "tweet_id": "",
            "user_image": user_image[7:],
            "user_username": username,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "tweet_text": "",
            "tweet_image": "",
            "tweet_like": "",
            "user_email": user_email,
            "liked": ""
        }
    else:
        num_tweets = all_tweets[0]
    
    print("ALL: ", num_tweets)
    return dict(user_email=user_email, user_name=user_name, tabs=g.TABS, tweets=all_tweets, trends=g.TRENDS, items=all_users, users=g.USERS, profile=num_tweets)