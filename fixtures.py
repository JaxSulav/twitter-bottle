from email.mime import image
import sqlite3

from models.user import insert_user
from models.tweets import insert_tweet

USERS = [
    {
        "user_id": "unique1",
        "first_name": "Barack",
        "last_name": "Obama",
        "email": "barackobama@gmail.com",
        "username": "barackobama",
        "password": "asdf1234",
        "image": "6.jpg"
    },
    {
        "user_id": "unique2",
        "first_name": "Elon",
        "last_name": "Musk",
        "email": "elonmusk@gmail.com",
        "username": "elonmusk",
        "password": "asdf1234",
        "image": "3.jpg"
    },
    {
        "user_id": "unique3",
        "first_name": "Joe",
        "last_name": "Biden",
        "email": "joebiden@gmail.com",
        "username": "joebiden",
        "password": "asdf1234",
        "image": "2.jpg"
    },
    {
        "user_id": "unique4",
        "first_name": "Kevin",
        "last_name": "Hart",
        "email": "kevinhart@gmail.com",
        "username": "kevinhart",
        "password": "asdf1234",
        "image": "4.jpg"
    },
    {
        "user_id": "unique5",
        "first_name": "Jax",
        "last_name": "Teller",
        "email": "wabalabadubdub26@gmail.com",
        "username": "jaxteller",
        "password": "asdf1234",
        "image": "bbc.png"
    },
    {
        "user_id": "unique6",
        "first_name": "Elton",
        "last_name": "John",
        "email": "wabalabadubdub126@gmail.com",
        "username": "eltonjohn",
        "password": "asdf1234",
    },
    
]

TWEETS = [
    {
        "image": "1.jpg",
        "date": "2022-09-14",
        "text": "The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.",
        "like": "320",
        "user_id": "1",
        
    },
    {
        "date": "2022-08-23",
        "text": "Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come.",
        "like": "1110",
        "user_id": "2",
        
    },
    {
        "date": "2022-09-25",
        "text": "Last year has been the best year for manufacturing jobs and trucking jobs since 1994.",
        "like": "880",
        "user_id": "3",
        
    },
    {
        "image": "1.jpg",
        "date": "2022-09-30",
        "text": "The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.",
        "like": "8300",
        "user_id": "1",
        
    },
    {
        "image": "2.jpg",
        "date": "2022-08-11",
        "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
        "like": "100",
        "user_id": "2",
        
    },
    {
        "date": "2022-09-24",
        "text": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here",
        "like": "1100",
        "user_id": "4",
        
    },
    {
        "image": "7.png",
        "date": "2022-08-18",
        "text": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        "like": "307",
        "user_id": "6",
    },
    {
        "image": "harris.jpg",
        "date": "2022-09-21",
        "text": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        "like": "576",
        "user_id": "5",
    },
    
]

if __name__=="__main__":
    print("Starting load fixtures...")
    con = sqlite3.connect('bottle.db')
    for user in USERS:
        temp = dict()
        temp["user_id"] = user.get("user_id", None)
        temp["user_first_name"] = user.get("first_name", None)
        temp["user_last_name"] = user.get("last_name", None)
        temp["user_email"] = user.get("email", None)
        temp["user_name"] = user.get("username", None)
        temp["user_password"] = user.get("password", None)
        if user.get("image", None):
            temp["user_image_path"] = user.get("image", None)
        insert_user(con, **temp)
        con.commit()
    
    for tweet in TWEETS:
        temp = dict()
        temp["user_id"] = tweet.get("user_id", None)
        if tweet.get("image"):
            temp["image"] = tweet.get("image")
        temp["date"] = tweet.get("date", None)
        temp["text"] = tweet.get("text", None)
        temp["like"] = tweet.get("like", None)
        insert_tweet(con, **temp)
        con.commit()
    
    con.close()