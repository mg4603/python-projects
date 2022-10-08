from functools import wraps
from tabnanny import check
from tkinter.tix import Select
from flask import(
    g, url_for, Blueprint, flash, redirect, render_template, request,
    session
)
from werkzeug.security import check_password_hash, generate_password_hash
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

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        
        if (username is None) or (password is None):
            error = "Username and password are required"
        else:
            user = db.execute(
                "SELECT * FROM user WHERE username=?", (username)
            ).fetchone()

            if (user is not None) and (not check_password_hash(user["password"], password)):
                error = "Invalid credentials"
        
        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM user WHERE id=?", (user_id)
        ).fetchone()

@bp.route("/logout", methods=("GET", "POST"))
def logout():
    session.clear()
    return redirect(url_for("index"))