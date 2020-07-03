from flask import Flask, make_response


def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_pyfile("settings.py")

    if test_config is not None:
        app.config.update(test_config)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def index(path):

        response = make_response()
        response.status_code = 200

        return response

    return app
