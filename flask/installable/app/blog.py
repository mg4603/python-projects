from flask import (
    Blueprint, render_template, request, redirect, url_for, flash,
    g
)
from .db import get_db

bp = Blueprint("blog", __name__)

@bp.route("/")
def index():
    db = get_db()

    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM post p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()

    return render_template("blog/index.html", posts=posts)

@bp.route("/create/", methods=("GET", 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if title is None:
            error = "Title is required"
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post(title, body, author_id)'
                'VALUE (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('index'))
        
        flash(error)
    return render_template('blog/create.html')

