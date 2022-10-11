from flask import (
    Blueprint, request, render_template, redirect, url_for
)

bp = Blueprint('hello', __name__, url_prefix='/hello')



@bp.route('/form/', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        greet = request.form['greet']
        name = request.form['name']
        if not greet:
            greet = "Hello"
        if not name:
            name = "Nobody"
        return redirect(url_for('hello.index', greet=greet, name=name))
        
    return render_template('hello/form.html')