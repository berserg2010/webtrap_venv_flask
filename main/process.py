from .logger import log_info, log_error_all_url, log_error_notawaiting


@log_info
@log_error_all_url
def process1():
    pass


@log_info
@log_error_all_url
@log_error_notawaiting
def process2():
    pass


@log_info
@log_error_all_url
def process3():
    pass
