from flask import Flask
from flask_cors import CORS
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(
    app.wsgi_app,
    root='static',
    prefix='static/'
)
CORS(app)

from app import routes

