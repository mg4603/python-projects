from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, 
    url_for
)

bp = Blueprint("auth", __name__, url_prefix="/auth")