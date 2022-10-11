from flask import (
    Blueprint, request, render_template
)

bp = Blueprint('hello', __name__, url_prefix='/hello')
