from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)

class Todo(db.Model):
	"""docstring for Todo"""
	__tablename__ = 'todos'
	id = db.Column('todo_id', db.Integer, primary_key=True)
	title = db.Column(db.String(60))
	text = db.Column(db.String)
	done = db.Column(db.Boolean)
	pub_date = db.Column(db.Datetime)

	def __init__(self, title, text):
		self.title = title
		self.text = text
		self.done = False
		self.pub_date = datetime.utcnow()
		

@app.route('/')
def index():
	pass

if __name__ == '__main__':
	app.run()

