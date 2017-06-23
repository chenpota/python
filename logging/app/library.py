import logging

from external_module.library import external_library


def do_something():
    logger = logging.getLogger(__name__)

    logger.debug('enter do_something()')

    external_library()

    logger.debug('exit do_something()')
