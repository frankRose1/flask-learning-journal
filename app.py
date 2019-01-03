from flask import Flask

app = Flask(__name__)

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

@app.route('/')
def index():
	return 'Hellooooo'

if __name__ == '__main__':
	app.run(debug=DEBUG, host=HOST, port=PORT)