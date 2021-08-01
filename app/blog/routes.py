
from flask import render_template
from. import bp






@bp.route('/blog')
def index():
    return render_template('blog.html',
                           title='Блог')

