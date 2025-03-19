from src import app
from flask import render_template, make_response, request
import json
from src.utils import get_locale, deep_update

@app.route('/')
@app.route('/index')
def index():
    with open("data/content.json") as f:
        content = json.load(f)

    page_lang = get_locale()
    try:
        with open(f"data/content.{page_lang}.json", encoding='utf-8') as f:
            content_loc = json.load(f)
        content = deep_update(content, content_loc)
    except FileNotFoundError:
        print(f"[ERROR] content file for language {page_lang} not found.")
    
    
    return render_template('index.html', content=content, page_lang=page_lang)

@app.route('/change_language')
def change_language():
    lang = request.args.get('l')
    res = make_response()
    res.set_cookie('lang', lang)
    return res