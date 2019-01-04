from flask import Flask, render_template

app = Flask(__name__)

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/edit')
def edit_entry():
	return render_template('edit.html')

if __name__ == '__main__':
	app.run(debug=DEBUG, host=HOST, port=PORT)