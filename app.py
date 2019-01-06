from flask import (Flask, render_template, g, flash, redirect, url_for)

import models
import forms
from config import config

app = Flask(__name__)
app.secret_key = config['secret']

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


@app.route('/entry/add', methods=['GET', 'POST'])
def add_entry():
	form = forms.NewEntryForm()
	if form.validate_on_submit():
		models.JournalEntry.create(
			title = form.title.data,
			date = form.date.data,
			time_spent = form.time_spent.data,
			what_i_learned = form.what_i_learned.data,
			resources_to_remember = form.resources_to_remember.data
		)
		flash('New journal entry was added!', 'success')
		return redirect(url_for('index'))
	return render_template('new.html', form=form)


@app.route('/edit')
def edit_entry():
	return render_template('edit.html')


if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, host=HOST, port=PORT)
