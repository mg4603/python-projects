from functools import wraps
from flask import(
    g, url_for, Blueprint, flash, redirect, render_template, request,
    session
)
from werkzeug.security import check_password_has, generate_password_hash
from .db import get_db

bp = Blueprint("auth", __name__, url_prefix= "/auth")

@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username  = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username or not password:
            error = "Username and password are required"
        
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUE (?, ?)", 
                    (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f"Username {username} already exists."
            else:
                return redirect(url_for("auth.login"))

        flash(error)
    
    return render_template("auth/register.html")

