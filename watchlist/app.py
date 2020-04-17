from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/hjk_is_dsb')
@app.route('/yilk')
def hello():
    return '<h1>Hello	Totoro!</h1><img	src="http://helloflask.com/totoro.gif">'

#使用了内置的开发服务器来运行程序，这个服务器默认监听本地机的5000端口
#note 内置的开服务器只能用于开发时使用，部署上线的时候要换性能更好的服务器