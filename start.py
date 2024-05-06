from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/') #127.0.0.1/css/b.css
def index():
    return send_from_directory('html','index.html')

@app.route('/<path:name>') #127.0.0.1/css/b.css
def start(name):
    return send_from_directory('html', name)