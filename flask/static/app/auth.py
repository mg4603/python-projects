from functools import wraps
from flask import(
    g, url_for, Blueprint, flash, redirect, render_template, request,
    session
)
from werkzeug.security import check_password_has, get_password_hash
from .db import get_db

bp = Blueprint("auth", __name__, url_prefix= "/auth")
