from flask import Flask, render_template
import blueprints.ajax as ajax


app = Flask(__name__)
app.config.from_pyfile('static/config.ini')

# 3.把蓝图注册到app上
app.register_blueprint(ajax.bp)


@app.route('/')
def index():
    return render_template('ajax.html')


if __name__ == '__main__':
    app.run()

# redis-server.exe redis.windows.conf

# Ajax 三部曲
# 1.编写对应处理的 Controller，返回消息或者字符串或者 json 格式的数据
# 2.编写 Ajax 请求
# 2.1. url：Controller 请求
# 2.2. data：键值对
# 2.3. success：回调函数
# 3.给 Ajax 绑定事件，例如点击 click，失去焦点 onblur， 键盘弹起 keyup

# json：是一种数据格式，是纯字符串，是对象。可以被解析成Python的dict或者其他形式。取值相当于获取对象属性。
# dict：是一个完整的数据结构，是对Hash Table这一数据结构的一种实现，是一套从存储到提取都封装好了的方案。
# 它使用内置的哈希函数来规划key对应value的存储位置，从而获得O（1）的数据读取速度。
