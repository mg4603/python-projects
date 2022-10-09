from flask import (
    Blueprint, g, current_app, session, url_for, redirect
)
from .db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")