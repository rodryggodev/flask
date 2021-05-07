from flask import Flask
from flas_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app= .config['SQLAlchemy_DATABSE_URI'] = 'sqlite///storage.db'
db = SQLAlchemy(app)

from app.controllers import default
