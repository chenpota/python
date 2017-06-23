import logging


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

LOGGER_HANDLER = logging.StreamHandler()
LOGGER_HANDLER.setLevel(logging.DEBUG)
LOGGER_HANDLER.setFormatter(
    logging.Formatter(
        '%(asctime)s - %(thread)d - %(name)s - %(levelname)s: %(message)s'))

LOGGER.addHandler(LOGGER_HANDLER)


def do_something():
    LOGGER.debug('enter do_something()')
