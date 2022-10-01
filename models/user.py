

from logging import exception
import sqlite3

def create_user_model(dbConn: sqlite3.Connection):
    try:
        dbConn.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, user_id char(50) NOT NULL, first_name char(200) NOT NULL, last_name char(200) NOT NULL, email char(200) NOT NULL UNIQUE, username char(200) NOT NULL UNIQUE, password char(200) NOT NULL)")
        print("User table Created")
    except sqlite3.OperationalError:
        print("User table already exists")
    except Exception as e:
        print(f"Error: {e}")

def create_session_model(dbConn: sqlite3.Connection):
    try:
        dbConn.execute("CREATE TABLE session (id INTEGER PRIMARY KEY, session_id char(50) NOT NULL UNIQUE, email char(200) NOT NULL)")
        print("Session table Created")
    except sqlite3.OperationalError:
        print("Session table already exists")
    except Exception as e:
        print(f"Error: {e}")

def insert_user(dbConn: sqlite3.Connection, **data):
    user_id = data.get("user_id", None)
    first_name = data.get("user_first_name", None)
    last_name = data.get("user_last_name", None)
    email = data.get("user_email", None)
    username = data.get("user_name", None)
    password = data.get("user_password", None)

    sql_query = "INSERT INTO user (user_id, first_name, last_name, email, username, password) VALUES (?,?,?,?,?,?)"
    args = user_id, first_name, last_name, email, username, password
    try:
        dbConn.execute(sql_query, args)
    except sqlite3.IntegrityError:
        return False, "Username already exists"
    except Exception as e:
        print(f"Error: {e}")
        return False, "Internal Error, contact admin"
    print(f"Inserted {args} into user table")
    return True, f"User {username} created"

def find_user(dbConn: sqlite3.Connection, email):
    sql_query = "SELECT email, password FROM user WHERE email=?"
    c = dbConn.cursor()
    c.execute(sql_query, (email,))
    queryset = c.fetchall()
    return queryset

def insert_session(dbConn: sqlite3.Connection, session_id, email):
    sql_query = "INSERT INTO session (session_id, email) VALUES (?, ?)"
    try:
        dbConn.execute(sql_query, (session_id, email,))
    except sqlite3.IntegrityError:
        return False, "Session id already exists"
    except Exception as e:
        print(f"Error: {e}")
        return False, "Internal Error, contact admin"
    print(f"Inserted {session_id} into session table")
    return True, f"Session {session_id} created"

def find_session_id(dbConn: sqlite3.Connection, session_id):
    sql_query = "SELECT id FROM session WHERE session_id=?"
    c = dbConn.cursor()
    c.execute(sql_query, (session_id,))
    queryset = c.fetchall()
    return queryset