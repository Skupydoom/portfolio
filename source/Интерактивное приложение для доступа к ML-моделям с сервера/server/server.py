import sqlite3
import os
from flask import Flask, g, request
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
from constants import *
import json


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsite.db")))

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "login first to get access to closed pages"
login_manager.login_message_category = "sucess"

@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(user_id, dbase)

def connect_db():
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """Auxiliary function for creating database tables"""
    db = connect_db()
    with app.open_resource("sql_db.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    """Connect to the database if it's not already connected"""
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db

dbase = None
@app.before_request
def before_request():
    """Establish a connection to the database before executing a request"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)

@app.teardown_appcontext
def close_db(error):
    """Close the connection with the database if it has been established """
    if hasattr(g, "link_db"):
        g.link_db.close()

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        email = request.authorization.username
        entire_password = request.authorization.password
        password = entire_password[:(len(entire_password) // 2)]
        confirm_password = entire_password[(len(entire_password) // 2):]

        if len(email) > 4 and len(password) > 4 \
           and password == confirm_password:
            hash = generate_password_hash(password)
            res = dbase.addUser(email, hash)
            if res:
                print("Success!")
                # Redirect user
                print({"registered": "redirect to login window"})
                return {"registered": "redirect to login window"}
            else:
                print("Error while adding data into the database")
                return {"Error": "Error while adding data into the database"}
        else:
            print("The fields are field in incorrectly")
            return {"Error": "The fields are field in incorrectly"}
    
    print({"Error": "unknown method"})
    return {"Error": "unknown method"}

@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        print({"logged": "redirect to models window"})
        return {"logged": "redirect to models window"}
    
    if request.method == "POST":
        user = dbase.getUserByEmail(request.authorization.username)

        if user and check_password_hash(user["password"], request.authorization.password):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            print({"logged": "redirect to models window"})
            return json.dumps({"logged": "redirect to models window"})
        
        print({"Error": "user not found or password is incorrect"})
        return {"Error": "user not found or password is incorrect"}
    
    print({"Error": "unknown method"})
    return {"Error": "unknown method"}



if __name__ == "__main__":
    app.run(debug=True)
