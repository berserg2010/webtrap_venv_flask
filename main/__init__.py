from flask import Flask, make_response

from .settings import settings
from .logger import log
from .process import process1, process2, process3


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(settings[config_name])
    settings[config_name].init_app(app)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    @log
    def query(path):

        process1()
        process2()
        process3()

        response = make_response()
        response.status_code = 200

        return response

    return app
