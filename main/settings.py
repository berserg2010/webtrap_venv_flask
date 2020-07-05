import os


class Config:

    SECRET_KEY = "ass'fgkjs/gs;'oidfjg;zlkfnjzx;lkfjgs;l/dkfgjs/"
    FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


settings = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,

    "default": DevelopmentConfig,
}
