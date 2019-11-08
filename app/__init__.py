"""
Initialization file for web application. Instantiates instance of Flask framework.
Loads configuration before setting up webpage routes.
"""

from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
