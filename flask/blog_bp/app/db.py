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

def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))

@command("init-db")
def init_db_command():
    init_db()
    echo("Initializing the database")

def register_db(app):
    app.teardown_context(close_db)
    app.cli.add_command(init_db_command)

