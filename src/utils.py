from flask import request
from src import app
import collections

def get_locale():
    print(request.accept_languages)
    user_lang = request.cookies.get('lang')
    if user_lang in app.config['LANGUAGES']:
        return user_lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = deep_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d