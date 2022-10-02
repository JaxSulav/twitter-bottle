import sqlite3
from bottle import post, request, response
import g
import sqlite3
from models.tweets import insert_tweet

from models.user import find_user
from datetime import datetime


@post("/api-create-tweet")
def _():
    # Validate
    tweet_text = request.forms.get("tweet_text", "")
    if len(tweet_text) < 1 or len(tweet_text) > 100:
        response.status = 400
        return "tweet_text invalid"
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )

    con = sqlite3.connect('bottle.db')
    queryset = find_user(con, user_email)
   
    if queryset:
        tweet = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "text": tweet_text,
            "image": "1.jpg",
            "like": "130",
            "user_id": queryset[0][2],
            "username": queryset[0][3],
            "first_name": queryset[0][4],
            "last_name": queryset[0][5],
            "user_image": queryset[0][6]
        }
        success, message = insert_tweet(con, **tweet)
        con.commit()
        if success:
            con.close()
            print("Tweet Created")
            return tweet
    con.close()
    return "Could not add the tweet !!"