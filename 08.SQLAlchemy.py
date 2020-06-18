# SQLAlchemy 是 Python 中一个通过 ORM 操作数据库的框架
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('static/config.ini')
# 初始化 SQLAlchemy 对象
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'Person'
    Id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(255))

    def __repr__(self):
        return 'id: %d, email: %s <br>' % (self.Id, self.Email)


p1 = Person(Email='a@b.com')
p2 = Person(Email='c@b.com')
p3 = Person(Email='a@b.com')
db.create_all()
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.commit()
# db.drop_all()


@app.route('/')
def index():
    p = Person.query.all()
    return str(p)


if __name__ == '__main__':
    app.run()

