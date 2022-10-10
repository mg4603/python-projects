from flask import (
    Blueprint, render_template, request, flash, redirect, url_for
)
from werkzeug.security import generate_password_hash, check_password_hash
from .db import get_db

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