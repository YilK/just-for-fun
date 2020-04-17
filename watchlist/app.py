#-*-coding: utf-8 -*-
from flask import Flask,render_template
app=Flask(__name__)
name='YilK'#准备虚拟数据
movies=[
    {'title':'My Neighbor Totoro','year':'1988'},
    {'title':'Dead Poet society','year':'1989'},
    {'title':'A Perfect	World','year':'1993'},
    {'title':'Leon','year':'1994'},
    {'title':'Mahjong','year':'1996'},
    {'title':'Swallowtail Butterfly','year':'1996'},
    {'title':'King of Comedy','year':'1999'},
    {'title':'Devils on	the	Doorstep','year':'1999'},
    {'title':'WALL-E','year':'2008'},
    {'title':'The Pork of Music','year':'2012'},
]
@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)

# def hello():
#     return '<h1>Hello	Totoro!</h1><img	src="http://helloflask.com/totoro.gif">'

#使用了内置的开发服务器来运行程序，这个服务器默认监听本地机的5000端口
#note 内置的开服务器只能用于开发时使用，部署上线的时候要换性能更好的服务器