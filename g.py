
USERS = []
##############################################################

SESSIONS = []
##############################################################

COOKIE_SECRET = "THIS IS SECRET COOKIE KEY"


REGEX_ID = "^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
##############################################################

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
##############################################################

REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
##############################################################

REGEX_USERNAME = '^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$'
##############################################################

TABS = [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id": "home",  "href": "/home"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore",  "href": "/explore"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications",  "href": "/notifications"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages",  "href": "/messages"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks", "href": "/bookmarks"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists",  "href": "/lists"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile", "href": "/profile"},
    {"icon": "fa-solid fa-arrow-right-from-bracket", "title": "Logout", "id": "logout", "href": "/logout"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more",  "href": "/logout"}

]


TRENDS = [
    {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
    {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
    {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
    {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "20k"},
    {"category": "Russia", "title": "Russia", "tweets_counter": "10k"},
]


TWEETS = [
    {"id": "1", "src": "6.jpg", "user_first_name": "Barack", "user_last_name": "Obama", "user_name": "barackobama", "date": "Feb 20",
     "text": "The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image": "1.jpg", "like": "0"},
    {"id": "2", "src": "2.jpg", "user_first_name": "Elon", "user_last_name": "Musk", "user_name": "joebiden", "date": "Mar 3",
     "text": "Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"id": "3", "src": "3.jpg", "user_first_name": "Joe Biden", "user_last_name": "Biden", "user_name": "elonmusk",
     "date": "Mar 7", "text": "Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
    {"id": "4", "src": "6.jpg", "user_first_name": "Barack", "user_last_name": "Obama", "user_name": "barackobama", "date": "Feb 20",
     "text": "The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image": "1.jpg"},
    {"id": "5", "src": "2.jpg", "user_first_name": "Elon", "user_last_name": "Musk", "user_name": "joebiden", "date": "Mar 3",
     "text": "Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"id": "6", "src": "3.jpg", "user_first_name": "Joe Biden", "user_last_name": "Biden", "user_name": "elonmusk",
     "date": "Mar 7", "text": "Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
    {"id": "7", "src": "6.jpg", "user_first_name": "Barack", "user_last_name": "Obama", "user_name": "barackobama", "date": "Feb 20",
     "text": "The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image": "1.jpg"},
    {"id": "8", "src": "2.jpg", "user_first_name": "Elon", "user_last_name": "Musk", "user_name": "joebiden", "date": "Mar 3",
     "text": "Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"id": "9", "src": "3.jpg", "user_first_name": "Joe Biden", "user_last_name": "Biden", "user_name": "elonmusk",
     "date": "Mar 7", "text": "Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
    {"id": "10", "src": "6.jpg", "user_first_name": "Barack", "user_last_name": "Obama", "user_name": "barackobama", "date": "Feb 20",
     "text": "The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image": "1.jpg"},
    {"id": "11", "src": "2.jpg", "user_first_name": "Elon", "user_last_name": "Musk", "user_name": "joebiden", "date": "Mar 3",
     "text": "Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
    {"id": "12", "src": "3.jpg", "user_first_name": "Joe Biden", "user_last_name": "Biden", "user_name": "elonmusk",
     "date": "Mar 7", "text": "Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
]

ITEMS = [
    {"img": "bbc.png", "title": "BBC News", "user_name": "bbcworld"},
    {"img": "biden.jpg", "title": "Joe Biden", "user_name": "joebiden"},
    {"img": "harris.jpg", "title": "Vice President", "user_name": "vp"},
]