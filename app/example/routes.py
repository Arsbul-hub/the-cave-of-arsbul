
from flask import render_template
from. import bp




import datetime as dt

@bp.route('/example')
def index():
    date = dt.datetime.now()
    time = date.time().isoformat()
    return render_template('example.html',
                           time=time)

