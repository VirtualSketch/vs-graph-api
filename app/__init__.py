from flask import Flask
from flask_cors import CORS
from whitenoise import WhiteNoise

from app.utils.get_static_path import get_static_path

STATIC_DIR = get_static_path()

app = Flask(__name__)
app.wsgi_app = WhiteNoise(
    app.wsgi_app,
    root=STATIC_DIR,
    prefix='static/'
)
CORS(app)

from app import routes

