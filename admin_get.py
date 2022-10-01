from bottle import get, request, view


############## RENDERS ADMIN PAGE###############################
@get("/admin")
@view("admin")
def admin():
    user_id = request.params.get("user_id")
    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    user_email = request.params.get("user_email")
    user_name = request.params.get("user_name")
    user_password = request.params.get("user_password")
    return dict(user_first_name=user_first_name, user_last_name=user_last_name, user_id=user_id, user_email=user_email, user_name=user_name, user_password=user_password)
