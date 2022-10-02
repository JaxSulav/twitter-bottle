import sqlite3
from bottle import post, request, response
import g
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
        date = datetime.now()
        tweet = {
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "text": tweet_text,
            "image": "1.jpg",
            "like": "0",
            "user_id": queryset[0][2],
            "username": queryset[0][3],
            "first_name": queryset[0][4],
            "last_name": queryset[0][5],
            "user_image": queryset[0][6]
        }
        success, _, tweet_id = insert_tweet(con, **tweet)
        con.commit()
        tweet['date'] = date.strftime("%b %d")
        if success:
            if tweet_id:
                tweet["id"] = tweet_id
            con.close()
            print("Tweet Created")
            return tweet
    con.close()
    return "Could not add the tweet !!"