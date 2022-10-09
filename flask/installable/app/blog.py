from flask import (
    Blueprint
)
from .db import get_db

bp = Blueprint("blog", __name__)