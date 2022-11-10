import sqlite3
from bottle import post, redirect, request, response
import jwt
import uuid
import g
import re
from models.user import insert_user, insert_session



@post("/api-create-user")
def create_user():
    if not re.match(g.REGEX_USERNAME, request.forms.get("user_name")):
        response.status = 400
        return "Username must contain 5 to 20 characters or numbers and only '.', '-' and '_' characters are allowed "

    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        return "Please insert a valid email"

    if not re.match(g.REGEX_PASSWORD, request.forms.get("user_password")):
        response.status = 400
        return "Password must contain minimum eight characters, at least one letter and one number"
    
    user_id = str(uuid.uuid4())
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_email = request.forms.get("user_email")
    user_name = request.forms.get("user_name")
    user_password = request.forms.get("user_password")

    user_image = request.files.get("user_image")
    save_path = "images/" 
    filename = str(user_name) + str(user_image.filename)

    file_path = "{path}/{file}".format(path=save_path, file=filename)
    user_image.save(file_path)
    
    user = {
        "user_id": user_id,
        "user_first_name": user_first_name,
        "user_last_name": user_last_name,
        "user_email": user_email,
        "user_name": user_name,
        "user_password": user_password,
    }

    if user_image:
        user["user_image_path"] = save_path + filename

    con = sqlite3.connect('bottle.db')
    success, _ = insert_user(con, **user)
    con.commit()

    encoded_jwt = jwt.encode(user, "secret", algorithm="HS256")
    user_session_id = str(uuid.uuid4())
    response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
    insert_session(con, user_session_id, user_email)
    con.commit()
    response.set_cookie("session_id", user_session_id)
    con.close()

    if success:
        return redirect("/tweets")
    return redirect("/409")
  #  return redirect (f"/?user_id={user_id}&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&user_name={user_name}&user_password={user_password}")
