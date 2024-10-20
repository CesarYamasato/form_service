import os
from flask import Flask, request, Response
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import session
    current_session = session.Session()
    app.route('/responses', methods=['GET'])(current_session.get_all_user_responses)
    app.route('/metadata', methods=['GET'])(current_session.get_form_metadata)
    app.route('/add_responses', methods=['GET'])(current_session.add_responses_to_db)
    
    return app