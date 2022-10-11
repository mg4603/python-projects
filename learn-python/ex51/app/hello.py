from flask import (
    Blueprint, request, render_template
)

bp = Blueprint('hello', __name__, url_prefix='/hello')


@bp.route('/form/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        greet = request.form['greet']
        name = request.form['name']

        
    return render_template('hello_form.html')