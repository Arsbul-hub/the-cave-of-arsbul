
from flask import render_template
from . import bp






@bp.route('/a')
def send():
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
        print(username,password)
    return render_template('comment.html')

