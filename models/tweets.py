import sqlite3

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

    if image:
        sql_query = "INSERT INTO tweet(image, date, text, like, user_id) VALUES (?,?,?,?,?)"
        args = image, date, text, like, user_id
    else:
        sql_query = "INSERT INTO tweet(date, text, like, user_id) VALUES (?,?,?,?)"
        args = date, text, like, user_id
    try:
        dbConn.execute(sql_query, args)
    except Exception as e:
        print(f"Error: {e}")
        return False, "Internal Error, contact admin"
    print(f"Inserted {args} into tweet table")
    return True, f"Tweet created"

def get_all_tweets(dbConn: sqlite3.Connection):
    c = dbConn.cursor()
    c.execute("SELECT user.image, user.first_name, user.last_name, user.username, tweet.date, tweet.text, tweet.image, tweet.like, tweet.id from tweet LEFT JOIN user ON tweet.user_id=user.id ORDER BY date DESC")
    res = c.fetchall()
    final = []
    for r in res:
        temp = dict()
        temp["user_image"] = r[0]
        temp["user_first_name"] = r[1]
        temp["user_last_name"] = r[2]
        temp["user_username"] = r[3]
        temp["tweet_date"] = r[4]
        temp["tweet_text"] = r[5]
        if r[6]:
            temp["tweet_image"] = r[6]
        temp["tweet_like"] = r[7]
        temp["tweet_id"] = r[8]
        final.append(temp)

    return final