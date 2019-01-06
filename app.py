from flask import (Flask, render_template, g, flash, redirect, url_for)
from flask_login import (login_user, logout_user, login_required,
						 current_user, LoginManager)
from flask_bcrypt import check_password_hash

import models
import forms
from config import config

app = Flask(__name__)
app.secret_key = config['secret']
login_manager = LoginManager()
login_manager.init_app(app)
# which view handles logging users in
login_manager.login_view = 'login'

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000


@login_manager.user_loader
def user_loader(userId):
	"""For when the login manager needs to look up a user"""
	try:
		return models.User.get(models.User.id == userId)
	except models.DoesNotExist:
		return None


@app.before_request
def before_request():
	"""Connect to the DB and set the current user before each request"""
	g.db = models.DATABASE
	g.db.connect()
	g.user = current_user


@app.after_request
def after_request(request):
	"""Close DB connection after each request"""
	g.db.close()
	return request


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = forms.LoginForm()
	if form.validate_on_submit():
		try:
			user = models.User.get(models.User.email == form.email.data)
		except models.DoesNotExist:
			flash('Incorrect email or password.', 'error')
		else:
			if check_password_hash(user.password, form.password.data):
				# set up the session with flask login
				login_user(user)
				flash('You are now signed in!', 'success')
				return redirect(url_for('index'))
			else:
				flash('Incorrect email or password.', 'error')
	return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = forms.RegisterForm()
	if form.validate_on_submit():
		models.User.create_user(
			username=form.username.data,
			email=form.email.data,
			password=form.password.data
		)
		flash('You successfully signed up! Log in to get started.', 'success')
		# prompt the user to log in
		return redirect(url_for('login'))
	return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
	# delete the session cookie
	logout_user()
	flash('You are now logged out.', 'success')
	return redirect(url_for('index'))


@app.route('/entry/add', methods=['GET', 'POST'])
def add_entry():
	form = forms.NewEntryForm()
	if form.validate_on_submit():
		models.JournalEntry.create(
			title=form.title.data,
			date=form.date.data,
			time_spent=form.time_spent.data,
			what_i_learned=form.what_i_learned.data,
			resources_to_remember=form.resources_to_remember.data
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
