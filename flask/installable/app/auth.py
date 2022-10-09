from .db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Blueprint, g, current_app, session, redirect, request, url_for
)

bp = Blueprint("auth", __name__, url_prefix="/auth")