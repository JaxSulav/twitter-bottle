import sqlite3
from datetime import datetime

def create_tweet_model(dbConn: sqlite3.Connection):
    try:
        dbConn.execute("CREATE TABLE tweet (id INTEGER PRIMARY KEY, image char(200), date char(20) NOT NULL, text char(500) NOT NULL, like char(10), user_id INTEGER, CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES user(id))")
        print("Tweet table Created")
    except sqlite3.OperationalError:
        print("Tweet table already exists")
    except Exception as e:
        print(f"Error: {e}")


def insert_tweet(dbConn: sqlite3.Connection, **data):
    user_id = data.get("user_id", None)
    image = data.get("image", None)
    date = data.get("date", None)
    text = data.get("text", None)
    like = data.get("like", None)
    tweet_id = None

    if image:
        sql_query = "INSERT INTO tweet(image, date, text, like, user_id) VALUES (?,?,?,?,?)"
        args = image, date, text, like, user_id
    else:
        sql_query = "INSERT INTO tweet(date, text, like, user_id) VALUES (?,?,?,?)"
        args = date, text, like, user_id
    try:
        c = dbConn.execute(sql_query, args)
        tweet_id = c.lastrowid
    except Exception as e:
        print(f"Error: {e}")
        return False, "Internal Error, contact admin", tweet_id
    print(f"Inserted {args} into tweet table")
    return True, f"Tweet created", tweet_id

def update_tweet(dbConn: sqlite3.Connection, **data):
    tweet_id = data.get("tweet_id", None)
    text = data.get("text", None)
    sql_query = "UPDATE tweet SET text=? WHERE id=?"
    try:
        dbConn.execute(sql_query, (text, tweet_id))
        dbConn.commit()
    except Exception as e:
        print(f"Error occurred while updating tweet {e}")
        return False
    return True

def update_tweet_for_admin(dbConn: sqlite3.Connection, **data):
    tweet_id = data.get("tweet_id", None)
    text = data.get("text", None)
    date = data.get("date", None)
    likes = data.get("likes", None)
    print("SSS: ", tweet_id)
    sql_query = "UPDATE tweet SET date=?, text=?, like=? WHERE id=?"
    try:
        dbConn.execute(sql_query, (date, text, likes, tweet_id))
        dbConn.commit()
    except Exception as e:
        print(f"Error occurred while updating tweet {e}")
        return False
    return True

def get_all_tweets(dbConn: sqlite3.Connection, request_user_email):
    c = dbConn.cursor()
    c.execute("SELECT user.image, user.first_name, user.last_name, user.username, tweet.date, tweet.text, tweet.image, tweet.like, tweet.id from tweet LEFT JOIN user ON tweet.user_id=user.id ORDER BY date DESC")
    res = c.fetchall()
    final = []
    for r in res:
        temp = dict()
        try:
            tweet_date = datetime.strptime(r[4], '%Y-%m-%d %H:%M:%S').strftime('%b %d')
        except ValueError as e:
            print("Error due to date in not saved in proper format", e)
            tweet_date = datetime.strptime(r[4], '%Y-%m-%d').strftime('%b %d')
        
        temp["user_image"] = r[0]
        temp["user_first_name"] = r[1]
        temp["user_last_name"] = r[2]
        temp["user_username"] = r[3]
        temp["tweet_date"] = tweet_date
        temp["tweet_text"] = r[5]
        if r[6]:
            temp["tweet_image"] = r[6]
        temp["tweet_like"] = r[7]
        temp["tweet_id"] = r[8]

        q = find_tweet_like(dbConn, r[8], request_user_email)
        if q:
            temp["liked"] = True
        else:
            temp["liked"] = False
        final.append(temp)

    return final

def get_tweets_for_admin(dbConn: sqlite3.Connection):
    c = dbConn.cursor()
    c.execute("SELECT tweet.text, user.email, tweet.date, tweet.id, tweet.like from tweet LEFT JOIN user ON tweet.user_id=user.id ORDER BY date DESC")
    res = c.fetchall()
    return res

def get_tweets_by_id(dbConn: sqlite3.Connection, tweet_id):
    c = dbConn.cursor()
    c.execute("SELECT date, text, like FROM tweet WHERE id=?", (tweet_id,))
    res = c.fetchall()
    return res

def delete_tweet(dbConn: sqlite3.Connection, tweet_id):
    sql_query = "DELETE from tweet WHERE id=?"
    try:
        dbConn.execute(sql_query, (tweet_id,))
        dbConn.commit()
    except Exception as e:
        print(f"Error occurred while deleting tweet {e}")
        return False
        
    return True

def create_tweet_like_model(dbConn: sqlite3.Connection):
    try:
        dbConn.execute("CREATE TABLE tweet_like (id INTEGER PRIMARY KEY, tweet_id INTEGER, user_email char(200),email_tweet char(210) NOT NULL UNIQUE, CONSTRAINT fk_user FOREIGN KEY (user_email) REFERENCES user(email), CONSTRAINT fk_tweet FOREIGN KEY (tweet_id) REFERENCES tweet(id))")
        print("Tweet Like table Created")
    except Exception as e:
        print(f"Error: {e}")


def insert_tweet_like(dbConn: sqlite3.Connection, tweet_id, user_email):
    sql_query = "INSERT INTO tweet_like(tweet_id, user_email, email_tweet) VALUES (?,?, ?)"
    args = tweet_id, user_email, (tweet_id+user_email)
    try:
        dbConn.execute(sql_query, args)
    except Exception as e:
        print(f"Error: {e}")
        return False, "Internal Error, contact admin"
    print(f"Inserted {args} into tweet like table")
    return True, f"Tweet Like created"

def find_tweet_like(dbConn: sqlite3.Connection, tweet_id, user_email):
    sql_query = "SELECT id FROM tweet_like WHERE tweet_id=? AND user_email=?"
    c = dbConn.cursor()
    c.execute(sql_query, (tweet_id, user_email,))
    queryset = c.fetchall()
    return queryset

def update_tweet_like(dbConn: sqlite3.Connection, like_count, tweet_id):
    sql_query = "UPDATE tweet SET like = ? WHERE id=?"
    dbConn.execute(sql_query, (like_count, tweet_id))
    return True