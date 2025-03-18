from src import app
from flask import render_template
import json

@app.route('/')
@app.route('/index')
def index():
    with open("data/content.json") as f:
        content = json.load(f)
    return render_template('index.html', content=content)