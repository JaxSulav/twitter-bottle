import sqlite3, g
from models.tweets import find_tweet_like, insert_tweet_like, update_tweet_like
from models.user import find_user
from datetime import datetime
from bottle import redirect, response, request, post


@post("/api-like-tweet")
def like_tweet():
    ret = {
        "success": True
    }
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
    tweet_id = request.forms.get("tweet_id", None)
    con = sqlite3.connect('bottle.db')
    queryset = find_tweet_like(con, tweet_id, user_email)

    if queryset:
        ret["success"] = True
    success, _ = insert_tweet_like(con, tweet_id, user_email)

    con.commit()
    
    if not success:
        ret["success"] = False
        return ret
    
    like_count = request.forms.get("likes", None)
    db_success = update_tweet_like(con, like_count, tweet_id)
    con.commit()

    if not db_success:
        ret["success"] = False
        return ret

    con.close()
    return ret