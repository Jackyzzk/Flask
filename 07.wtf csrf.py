import base64
import os

from flask import Flask, request, render_template, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_pyfile('static/config.ini')
# wtf
CsrfProtect(app)


class RegForm(FlaskForm):
    username = StringField('用户名：', validators=[InputRequired('请输入用户名')],
                           render_kw={'placeholder': 'username'})
    pwd = PasswordField('密码：', validators=[InputRequired('请输入密码')])
    submit = SubmitField('注册')


@app.route('/')
def index():
    return 'index'


@app.route('/wtf', methods=['POST', 'GET'])
def wtf():
    form_wtf = RegForm()
    print(request.method)
    if form_wtf.validate_on_submit():
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        print(username)
        print(pwd)
        return 'wtf success'
    return render_template('reg.html', form=form_wtf)


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    form_wtf = RegForm()
    csrf_set = csrf_gen()

    if request.method == 'POST':  # 注意判断的时候不能用小写的 post
        csrf_cookie = request.cookies.get('csrf_token')
        csrf_form = request.form.get('csrf_token')
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        if csrf_cookie != csrf_form:
            return 'error'
        print(username)
        print(pwd)
        print(csrf_cookie)
        return 'original success'

    res = make_response(render_template('reg.html', form=form_wtf, csrf_token=csrf_set))
    res.set_cookie('csrf_token', csrf_set)
    return res


def csrf_gen():
    return bytes.decode(base64.b64encode(os.urandom(48)))


if __name__ == '__main__':
    app.run()

