from bottle import get, redirect, request, response, view
import g


############## RENDERS TWEETS PAGE ###############################
@get("/tweets")
@view("tweets")
def tweets():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    user_session_id = request.get_cookie("session_id")
    if user_session_id not in g.SESSIONS:
        return redirect("/login")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET )
    user_name = request.forms.get("user_name")
    print(user_name)
    return dict(user_email=user_email, user_name=user_name, tabs=g.TABS, tweets=g.TWEETS, trends=g.TRENDS, items=g.ITEMS, users=g.USERS)