from bottle import post, request, response
import g
import uuid




@post("/api-create-tweet")
def _():
    # Validate
    tweet_text = request.forms.get("tweet_text", "")
    if len(tweet_text) < 1 or len(tweet_text) > 100:
        response.status = 400
        return "tweet_text invalid"
    # Connect to the db
    # query
    tweet_id = str(uuid.uuid4())
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
   
    for user in g.USERS:
        if user_email == user["user_email"]:
            tweet = {
                "id": tweet_id,
                "src": "6.jpg",
                "user_first_name": user["user_first_name"],
                "user_last_name": user["user_last_name"],
                "user_name": user["user_name"],
                "date": "Feb 20",
                "text": tweet_text
            }
            g.TWEETS.append(tweet)
            # respond
            return tweet