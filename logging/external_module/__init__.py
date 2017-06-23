import logging


LOGGER_NAME = __name__


logging.getLogger(LOGGER_NAME).addHandler(logging.NullHandler())
