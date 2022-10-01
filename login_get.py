from bottle import get, view

@get("/login")
@view("index")
def login():
    return