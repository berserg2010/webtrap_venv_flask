from flask import Flask, request, make_response

from .logger import log
from .process import process1, process2, process3

PORT = 8001


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_pyfile("settings.py")

    if test_config is not None:
        app.config.update(test_config)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    @log
    def query(path):

        process1()
        process2()
        process3()

        response = make_response()
        response.status_code = 200

        return response

    # app.add_url_rule("/", "query", query,  defaults={'path': ''})
    # app.add_url_rule("/<path:path>", "query", query)

    return app
