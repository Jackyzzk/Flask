from flask import Flask, render_template
import blueprints.captcha as captcha


app = Flask(__name__)
app.config.from_pyfile('static/config.ini')

# 3.把蓝图注册到app上
app.register_blueprint(captcha.bp)


@app.route('/')
def index():
    return render_template('captcha.html')


if __name__ == '__main__':
    app.run()

# redis-server.exe redis.windows.conf
