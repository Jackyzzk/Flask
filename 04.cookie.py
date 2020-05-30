from flask import Flask, request, make_response

app = Flask(__name__)
app.config.from_pyfile('static/config.ini')


@app.route('/')
def index():
    user_id = request.cookies.get('user_id')
    return user_id if user_id else 'no'


@app.route('/login/<int:user_id>')
def login(user_id):
    res = make_response('success')
    res.set_cookie('user_id', str(user_id))
    return res


if __name__ == '__main__':
    app.run()

