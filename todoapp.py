from flask import Flask, request, flash, url_for, redirect, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_bootstrap import Bootstrap

PROJECT_ROOT = os.getcwd()
DB_NAME = 'dev.db'
DB_PATH = os.path.join(PROJECT_ROOT, DB_NAME)
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
DEBUG = True
SECRET_KEY = 'Get serious'

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)
Bootstrap(app)

class Todo(db.Model):
	"""docstring for Todo"""
	__tablename__ = 'todos'
	id = db.Column('todo_id', db.Integer, primary_key=True)
	title = db.Column(db.String(60))
	text = db.Column(db.String)
	done = db.Column(db.Boolean)
	pub_date = db.Column(db.DateTime)

	def __init__(self, title, text):
		self.title = title
		self.text = text
		self.done = False
		self.pub_date = datetime.utcnow()
		

@app.route('/')
def index():
	return render_template('index.html',
        todos=Todo.query.order_by(Todo.pub_date.desc()).all()
    )
 
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/todos/<int:todo_id>', methods = ['GET' , 'POST'])
def show_or_update(todo_id):
    todo_item = Todo.query.get(todo_id)
    if request.method == 'GET':
        return render_template('view.html',todo=todo_item)
    todo_item.title = request.form['title']
    todo_item.text  = request.form['text']
    todo_item.done  = ('done.%d' % todo_id) in request.form
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
	app.run()

