from flask import Flask, render_template, g
from flask_bootstrap import Bootstrap
import create_db, user
import os, sqlite3

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        if os.path.isfile(create_db.DATABASE):
            db = g._database = sqlite3.connect(create_db.DATABASE)
        else:
            create_db.create_db(create_db.DATABASE)
    return db

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/')
    def index():
        db = get_db()
        return render_template('index.html')
    
    return app
