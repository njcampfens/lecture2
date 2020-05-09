from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Alice', 'Bob', 'Charly', 'David']
    return render_template('index.html', names=names)
