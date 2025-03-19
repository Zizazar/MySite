from flask import request
from src import app

def get_locale():
    user_lang = request.cookies.get('lang')
    if user_lang in app.config['LANGUAGES']:
        return user_lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_next_lang():
    languages = app.config['LANGUAGES']
    next_index = languages.index(get_locale()) + 1
    print(next_index)
    if next_index < len(languages):
        return languages[next_index]
    else:
        return languages[0]
    


def update_json(original, update):
    if isinstance(original, dict) and isinstance(update, dict):
        for key, value in update.items():
            if key in original:
                if isinstance(value, (dict, list)) and isinstance(original[key], type(value)):
                    update_json(original[key], value)
                else:
                    original[key] = value
            else:
                original[key] = value
    elif isinstance(original, list) and isinstance(update, list):
        for i, item in enumerate(update):
            if i < len(original):
                if isinstance(item, (dict, list)) and isinstance(original[i], type(item)):
                    update_json(original[i], item)
                else:
                    original[i] = item
            else:
                original.append(item)
    return original
