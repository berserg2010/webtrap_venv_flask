from flask import Flask, make_response

from .settings import settings
from .logger import log_info, log_error_all_url
from .process import process1, process2, process3


methods = ("get", "patch", "post", "head", "put", "delete", "options", "trace")


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(settings[config_name])
    settings[config_name].init_app(app)

    @app.route("/", defaults={"path": ""}, methods=methods)
    @app.route("/<path:path>", methods=methods)
    @log_info
    @log_error_all_url
    def query(path):

        if path == "api" or path == "api/":
            process1()
            process2()
            process3()

        response = make_response()
        response.status_code = 200

        return response

    return app
