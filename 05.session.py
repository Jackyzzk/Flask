from flask import Flask, make_response, session

app = Flask(__name__)
app.config.from_pyfile('static/config.ini')


@app.route('/')
def index():
    # 后面跟一个空字符表示如果获取不到 user_id 就返回空
    user_id = session.get('user_id', '')  # request.cookie.get
    return user_id if user_id else 'no'


@app.route('/login/<int:user_id>')
def login(user_id):
    session['user_id'] = str(user_id)
    return 'success'


@app.route('/logout')
def logout():
    # 加一个 None 可以在已经清除过 session 后返回空而不是报错
    session.pop('user_id', None)
    return 'success'


if __name__ == '__main__':
    app.run()

