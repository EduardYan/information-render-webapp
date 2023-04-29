"""
This file have the routes
for the server not execute this file.
Execute the file './main.py'

For default the server is running in 5000 port.

"""

from flask import Flask
from routes.routes_server import routes


app = Flask(__name__)

# some settings here


app.register_blueprint(routes)
