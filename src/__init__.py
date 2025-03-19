from flask import Flask
from config import Config
from flask_moment import Moment

app = Flask(__name__)

app.config.from_object(Config)
moment = Moment(app)
moment.init_app(app)

from src import routes