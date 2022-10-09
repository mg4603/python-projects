from flask import (
    Blueprint, g, session, redirect, url_for, request, flash, 
    render_template
)
from .db import get_db
from werkzeug.exceptions import abort
from .auth import login_required

bp = Blueprint("blog", __name__)