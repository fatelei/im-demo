# -*- coding: utf8 -*-
"""
    imdemo.apis.app
    ~~~~~~~~~~~~~~~

    Main app entry.
"""

import os

from flask import Flask

from imdemo.apis.handlers.thread import thread_app
from imdemo.models import db


def run():
    """Run standalone http server.
    """
    app = Flask(__name__)

    # Bind to mysql, and generate mapping.
    db.bind("mysql",
            host="localhost",
            port=3306,
            user="root",
            passwd="123456",
            db="threads")
    db.generate_mapping(check_tables=True,
                        create_tables=False)

    # Register blueprint.
    app.register_blueprint(thread_app)

    if "DEBUG" in os.environ:
        app.run(port=8888, debug=True)
    else:
        app.run(port=8888)
