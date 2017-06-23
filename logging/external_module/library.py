import logging

from external_module import LOGGER_NAME


def external_library():
    logger = logging.getLogger(LOGGER_NAME)

    logger.debug('enter external_library()')

    logger.debug('exit external_library()')
