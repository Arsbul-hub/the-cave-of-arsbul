
from flask import render_template
from. import bp




@bp.route('/')
@bp.route('/index')
@bp.route('/main')
def index():
    return render_template('main.html',
                           title='Главная')

