"""
This file have the routes
for use the server.

"""

from flask import (
    Blueprint,
    render_template,
)

from helpers.utils import get_json_data, CONFIG


routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    """
    Principal routes to use.
    """

    # getting information to show in the page
    information = get_json_data(CONFIG['DATA_FILE_PATH'])

    return render_template('index.html', information = information)


@routes.route('/about')
def about():
    """
    Route for get information about
    the app.
    """

    return 'About'

