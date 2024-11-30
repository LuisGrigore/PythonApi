# extensions.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializar SQLAlchemy aquí, sin necesidad de usar 'app' aún
app = Flask(__name__)
db = SQLAlchemy()
