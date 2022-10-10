from flask import (
    Blueprint, render_template, request, flash, redirect, url_for,
    session, g
)
from werkzeug.security import generate_password_hash, check_password_hash
from .db import get_db
from functools import wraps

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        db = get_db()

        if (not username) or (not password):
            error = 'Username and password required'

        if error is None:
            try:
                db.execute(
                    'INSERT INTO user(username, password)'
                    ' VALUES (?, ?)',
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f'Username {username} already exists.'
            else:
                return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        db = get_db()

        if (username is None) or (password is None):
            error = 'Username and password are required'
        else:
            user = db.execute(
                'SELECT * FROM user WHERE username=?', (username,)
            ).fetchone()

            if (user is None) or (not check_password_hash(user['password'], password)):
                error = 'Invalid credentials'
            else:
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('index')) 

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id=?',
            (user_id, )
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view