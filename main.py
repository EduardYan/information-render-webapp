#!/usr/bin/env python3

"""
This is the principal file
for execute the server.
"""

from app import app
from helpers.utils import CONFIG

if __name__ == '__main__':
    # running
    app.run(
        port = CONFIG['PORT'],
        debug = True,
    )
