from .db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Blueprint, g, current_app, session, redirect, request, url_for,
    render_template, flash
)

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if (username is None) or (password is None):
            error = "Username and password are required"
        else:
            try:
                db.execute(
                    "INSERT INTO user(username, password) VALUES (?, ?)"
                    , (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Username {username} already exists."
            else:
                return redirect(url_for("auth.login"))
                
        flash(error)

    render_template("auth/register.html")