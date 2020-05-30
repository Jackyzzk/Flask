from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo

app = Flask(__name__)
app.config.from_pyfile('static/config.ini')


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
    if request.method == 'POST':  # 注意判断的时候不能用小写的 post
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        print(username)
        print(pwd)
        return 'original success'
    return render_template('reg.html', form=form_wtf)


if __name__ == '__main__':
    app.run()

