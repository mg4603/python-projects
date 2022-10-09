from sqlite3 import Row, connect, PARSE_DECLTYPES
from click import command, echo
from flask import current_app, g

def get_db():
    if "db" not in g:
        g.db = connect(
            current_app.config["DATABASE"],
            detect_types=PARSE_DECLTYPES
        )
        g.db.row_factory = Row
    
    return g.db

def close_db():
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
    echo("Initialize the database")

def register_db(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)