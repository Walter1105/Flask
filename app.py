from flask import Flask 

app = Flask(__name__)
@app.route("/")
def index():
	return "hello, world!"

@app.route('/<nombre>')
def hello(nombre):
    return('<p>Hola, {}.</p>'.format(nombre))