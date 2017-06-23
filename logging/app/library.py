import logging

from external_module.library import external_library


LOGGER = logging.getLogger(__name__)


def do_something():
    LOGGER.debug('enter do_something()')

    external_library()

    LOGGER.debug('exit do_something()')
