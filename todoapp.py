from flask import Flask, request, flash, url_for, redirect, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_bootstrap import Bootstrap

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
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
	return 'home'
 
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('new.html')

if __name__ == '__main__':
	app.run()

