from src import app
from flask import render_template, make_response, request, jsonify, url_for, send_file
import json
from src.utils import get_locale, update_json, get_next_lang
import os
import requests


@app.route('/')
@app.route('/index')
def index():
    with open("data/content.json") as f:
        content = json.load(f)

    page_lang = get_locale()

    next_lang= get_next_lang()

    try:
        with open(f"data/content.{page_lang}.json", encoding='utf-8') as f:
            content_loc = json.load(f)
        content = update_json(content, content_loc)
    except FileNotFoundError:
        print(f"[ERROR] content file for language {page_lang} not found.")
    
    
    return render_template('index.html', content=content, page_lang=page_lang, next_lang=next_lang)

@app.route('/change_language')
def change_language():
    lang = request.args.get('l')
    res = make_response(jsonify({"new": lang, "last": get_locale()}))
    res.set_cookie('lang', lang)
    return res