from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, 
    url_for
)

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username required"
        elif not password:
            error = "Password required"
        
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} already exists."
            else:
                return redirect(url_for("auth.login"))
                
        flash(error)

    return render_template("auth/register.html")