""" Simple web application that demonstrates flask bootstrap,
database functionality, and user input
"""

from flask import Flask, render_template, g, request
from flask_bootstrap import Bootstrap
import create_db
import user, view
import os, sqlite3, random

def get_db():
    """ This function accesses the global database.
    If the database isn't loaded and doesn't exist, it will
    create one in the local directory. Note: when this is hosted
    on a real webserver, it might put the database in the home directory.
    """
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

    @app.route('/add_user', methods=('POST', 'GET'))
    def add_user():
        """ Inserts a user into the database. Assigns them a random id (1-1000)
        input: 'user_name' : form data string
        """
        db = get_db()
        new_user = user.User(random.randint(0, 1000), request.form["user_name"].strip())
        user.insert_user_into_db(new_user, db)
        return view.get_user_list_html(db)
    
    return app
