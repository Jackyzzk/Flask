from flask import Flask
from flask_script import Manager

app = Flask(__name__)
app.config.from_pyfile('static/config.ini')
manager = Manager(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()

# python 03.manager.py runserver -p 5000 -d
# python 03.manager.py runserver
