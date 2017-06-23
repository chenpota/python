import logging


LOGGER = logging.getLogger(__name__)


def do_something():
    LOGGER.debug('enter do_something()')

    LOGGER.debug('exit do_something()')
