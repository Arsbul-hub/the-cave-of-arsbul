from flask import Flask, render_template, request
import pandas as pd
from. import bp
@bp.route('/test_font/', methods=['GET'])
def search():
    error = None
    font = request.args.get('font')
    size = request.args.get('size')

    # проверяем, передается ли параметр
    # 'query' в URL-адресе
    print(font,size)
    if size != '' and font != '':
        # если `query`существует и это не пустая строка,
        # то можно приступать к обработке запроса

        return render_template('test_font.html',size=size,text=f"""font = {font}, size = {size}""")

    else:
        # если `query` не существует или это пустая строка, то 
        # отображаем форму поискового запроса с сообщением.
        error = 'Не введен запрос!'
        return render_template('test_font.html')