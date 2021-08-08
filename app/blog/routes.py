
from flask import render_template
from. import bp



import pandas as pd


@bp.route('/blog')
def index():
    names = []
    comment = []
    a = pd.read_excel('C:/Users/Arsbul Programming/Documents/the cave of arsbul/app/users.xlsx')
    comments = a.head()
    for i in range(len(a)):

        comment.append(a["comment"].get(i))
        names.append(a["name"].get(i))
    print(a,len(a))
    return render_template('blog.html',
                           title='Блог',comments=comment,names=names,len_list=len(a))

