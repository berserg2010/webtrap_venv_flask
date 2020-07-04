from flask import request
import logging
from functools import wraps


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s:%(funcName)s:%(lineno)d - %(message)s"
)
ch.setFormatter(formatter)

logger.addHandler(ch)


def log(func):
    @wraps(func)
    def _log(*args, **kwargs):

        method = request.method
        request_path = request.path
        url = request.base_url
        parameters = dict(request.args)

        logger.info(f"{func.__module__}:{func.__name__} - {method} - {url}{ f' - {parameters}' if parameters else ''}")

        if method == "GET":
            logger.error(f"{func.__module__}:{func.__name__} - Invalid method: {method}")

        if parameters.get("invalid") == "1":
            logger.error(f"{func.__module__}:{func.__name__} - Invalid parameters: {parameters}")

        if request_path != "/api":
            logger.error(f"{func.__module__}:{func.__name__} - Invalid path: {request_path}")

        return func(*args, **kwargs)

    return _log
