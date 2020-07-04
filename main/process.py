from flask import request

from .logger import logger, log


@log
def process1():
    pass


@log
def process2():

    parameters = dict(request.args)

    if parameters.get("notawaiting") == "1":
        logger.error(f"Invalid parameters: {parameters}")
    pass


@log
def process3():
    pass
