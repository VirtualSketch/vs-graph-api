from flask import Flask
from flask_cors import CORS
from whitenoise import WhiteNoise
from pathlib import Path
import os


ROOT_DIR = Path(os.path.dirname(__file__))

app = Flask(__name__)
app.wsgi_app = WhiteNoise(
    app.wsgi_app,
    root=Path(ROOT_DIR.parent, 'static'),
    prefix='static/'
)
CORS(app)

from app import routes

if __name__ == "__main__":
    app.run()