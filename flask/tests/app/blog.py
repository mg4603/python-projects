from flask import (
    Blueprint, render_template
)
from .db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, username, author_id'
        ' FROM post p JOIN user u on p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

