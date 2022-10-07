from sqlite3 import Row, connect, PARSE_DECLTYPES
from flask import g, current_app

def get_db():
    if "db" not in g:
        g.db = connect(
            current_app.config["DATABASE"],
            detect_types=PARSE_DECLTYPES
        )
        g.db.row_factory = Row
    
    return g.db

def close_db(e=None):
    db = g.db("db", None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))