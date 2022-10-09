from sqlite3 import connect, Row, PARSE_DECLTYPES
from flask import g, current_app
from click import echo, command

def get_db():
    if "db" not in g:
        g.db = connect(
            current_app.config["DATABASE"],
            detect_types=PARSE_DECLTYPES
        )
    
    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

