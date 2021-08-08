
from flask import Flask, render_template, request
import pandas as pd
from. import bp




comments = []
comment = ""
users = []
@bp.route('/comment', methods=['post', 'get'])

def index():
    global comments,comment,users
    if request.method == 'POST':
        user = request.form.get('username')  # запрос к данным формы

        #if comment == request.form.get('comment'):
        comment = request.form.get('comment')
        comments.append(comment)

        users.append(user)
        #comments.append(comment)
        print(users,comments)
        #print(comments)

        df = pd.DataFrame({"name": users,"comment": comments})
        df.to_excel('C:/Users/Arsbul Programming/Documents/the cave of arsbul/app/users.xlsx')

    return render_template('comment.html',
                           title='comment')

