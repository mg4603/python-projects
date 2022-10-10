from flask import (
    Blueprint, render_template, request, flash, url_for,
    redirect, g
)
from .auth import login_required
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

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if title is None:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post(author_id, title, body)'
                ' VALUES (?, ?, ?)',
                (g.user['id'], title, body)
            )
            db.commit()
            return redirect(url_for('blog.index'))
                
    return render_template('blog/create.html')