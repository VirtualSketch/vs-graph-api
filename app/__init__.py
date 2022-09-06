from flask import Flask
from flask_cors import CORS

from app.utils.get_static_path import get_static_path

STATIC_DIR = get_static_path()

app = Flask(__name__)
CORS(app)

from app import routes

