from sqlite3 import PARSE_DECLTYPES, Row, connect
from flask import current_app, g

def get_db():
    if "db" not in g:
        g.db = connect(
            current_app.config["DATABASE"],
            detect_types=PARSE_DECLTYPES
        )
        g.db.row_factory = Row

        return g.db


