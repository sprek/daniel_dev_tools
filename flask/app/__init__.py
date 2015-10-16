from flask import Flask, render_template, g
from flask_bootstrap import Bootstrap
import create_db
import user, view
import os, sqlite3

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        if not os.path.isfile(create_db.DATABASE):
            create_db.create_db(create_db.DATABASE)
        db = g._database = sqlite3.connect(create_db.DATABASE)
    return db

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/')
    def index():
        db = get_db()
        return render_template('index.html', users_html=view.get_user_list_html(db))

    @app.route('/add_user', methods=('POST','GET'))
    def add_user(user_name):
        #user.insert_user_into_db(user.User(
        #user.insert_user_into_db(user.User(
        return view.get_user_list_html(get_db())


    
    return app
