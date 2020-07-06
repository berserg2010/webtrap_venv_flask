from flask import request
import logging
from functools import wraps


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)-5s - %(name)s:%(funcName)-12s:%(lineno)d - %(message)s"
)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

fh = logging.FileHandler("webtrap.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


def log_info(func):
    @wraps(func)
    def _log_info(*args, **kwargs):

        logger_info(func)

        return func(*args, **kwargs)
    return _log_info


def log_error_all_url(func):
    @wraps(func)
    def _log_error_all_url(*args, **kwargs):

        logger_error(func, "method_ne_get")
        logger_error(func, "request_path_ne_api")
        logger_error(func, "parameters_invalid_e_1")

        return func(*args, **kwargs)
    return _log_error_all_url


def log_error_notawaiting(func):
    @wraps(func)
    def _log_error_api_url(*args, **kwargs):

        logger_error(func, "parameters_notawaiting_e_1")

        return func(*args, **kwargs)
    return _log_error_api_url


def logger_info(func):

    def _formatter(x: (str, dict)) -> str: return f" - {x}"

    method: str = _formatter(get_options("method"))
    url: str = _formatter(request.base_url)
    parameters: str = _formatter(get_options("parameters")) if get_options("parameters") else ""

    logger.info(f"{func_formatter(func)}{method}{url}{parameters}")


def logger_error(func, params: str):
    param: tuple = get_options("point_logging").get(params)

    if param[0]:
        logger.error(f"{func_formatter(func)} - Invalid {param[1]}")


def func_formatter(func) -> str:
    return f"{func.__module__}:{func.__name__}"


def get_options(params: str) -> (str, dict, tuple):

    method = request.method
    request_path = request.path
    parameters = dict(request.args)

    options = {
        "method": method,
        "request_path": request_path,
        "parameters": parameters,
        "point_logging": {
            "method_ne_get": (
                method != "GET",
                method,
            ),
            "request_path_ne_api": (
                request_path != "/api" and request_path != "/api/",
                request_path,
            ),
            "parameters_invalid_e_1": (
                parameters.get("invalid") == "1",
                {"invalid": parameters.get("invalid")},
            ),
            "parameters_notawaiting_e_1": (
                parameters.get("notawaiting") == "1",
                {"notawaiting": parameters.get("notawaiting")},
            ),
        },
    }

    return options.get(params)
