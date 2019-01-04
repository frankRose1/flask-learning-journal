from flask import Flask, render_template, g

import models

app = Flask(__name__)

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000


@app.before_request
def before_request():
	"""Connect to the DB before each request"""
	g.db = models.DATABASE
	g.db.connect()


@app.after_request
def after_request(request):
	"""Close DB connection after each request"""
	g.db.close()
	return request


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/edit')
def edit_entry():
	return render_template('edit.html')


if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, host=HOST, port=PORT)
