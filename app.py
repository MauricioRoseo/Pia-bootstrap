from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="./", static_folder="/")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contato.sqlite3'
db = SQLAlchemy(app)