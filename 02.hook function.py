from flask import Flask, request


app = Flask(__name__)
app.config.from_pyfile('static/config.ini')


@app.route('/')
def index():
    print('index')
    return 'index'


# 钩子函数测试
@app.before_first_request
def hook1():
    print('1')


@app.before_request
def hook2():
    print('2')


@app.after_request
def hook3(ret):
    print('3')
    return ret


@app.teardown_request
def hook4(err):
    print('4')
    return err


if __name__ == '__main__':
    app.run()

