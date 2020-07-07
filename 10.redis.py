from flask import Flask
import blueprints.test_ping as ping
import blueprints.test_redis as redis


app = Flask(__name__)
app.config.from_pyfile('static/config.ini')

# 3.把蓝图注册到app上
app.register_blueprint(ping.bp)
app.register_blueprint(redis.bp)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()