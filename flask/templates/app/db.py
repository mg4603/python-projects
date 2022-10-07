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

