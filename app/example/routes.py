
from flask import render_template
from. import bp




import datetime as dt

@bp.route('/example')
def index():
    date = dt.datetime.now()
    time = date.time().isoformat()
    return f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML  4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>example</title>
 </head>
 <body>

    <a>
     {time}
    </a>
  <table border="1" width="100%" cellpadding="5">
   <tr>
    <th>Ячейка 1</th>
    <th>Ячейка 2</th>
   </tr>
   <tr>
    <td>1</td>
    <td>2</td>

  </tr>
   <tr>
    <td>3</td>
    <td>4</td>

  </tr>
   <tr>
    <td>5</td>
    <td>6</td>

  </tr>
 </table>
 </body>
</html>'''
