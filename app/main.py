from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)



class Todo(db.Model):
    __tablename__ = "todos"

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title       = db.Column(db.Text())
    content     = db.Column(db.Text())
    #commit      = db.Column(db.Integer, autoincrement=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    todo = Todo(title='title', content='test content')
    db.session.add(todo)
    db.session.commit()

    return render_template("index.html", todos=Todo.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        app.logger.info(request.form)
        return 'POST'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)