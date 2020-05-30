# 为了在index函数中返回html页面而引入render_template，request可以拿提交到服务器的值
from flask import Flask, render_template, request, redirect, url_for

# __name__在这里会指向这个模块名(MyFlask)
app = Flask(__name__)
# 加载配置的三种方式：从文件，从类对象，从环境变量
app.config.from_pyfile('static/config.ini')


@app.route('/')
def index():
    start = 'hello'
    rec = [1, 2, 3, 4]
    return render_template('index.html', start=start, rec=rec)  # 此时会自动的找templates目录下的对应文件


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/check', methods=['post'])
# 默认的方法是get，加上 post 才能获得页面提交过来的数据
def check():
    name = request.form.get('username')
    pwd = request.form.get('pwd')
    if name == pwd == '110':
        return '成功'
    else:
        return render_template('login.html', msg='失败')


@app.route('/user/<int:user_id>')  # int过滤器 尖括号表示动态的内容
def user(user_id):
    if user_id == 110:
        # return redirect('/login')
        return redirect(url_for('login'))
    return request.method + str(user_id)


if __name__ == '__main__':
    app.run()

