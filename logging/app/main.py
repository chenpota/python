#!/usr/bin/env python3

import logging
import logging.config
import os

import yaml

from app import library
from app import logger


def load_logger_yaml():
    logger_cfg_path = os.path.dirname(__file__) + '/logger.yaml'

    with open(logger_cfg_path) as file_desc:
        return yaml.load(file_desc.read())


def main():
    LOGGER = logging.getLogger('app.main')

    LOGGER.debug('enter main()')

    library.do_something()

    LOGGER.debug('exit main()')


if __name__ == '__main__':

    # logging.config.dictConfig(logger.CONFIG)
    logging.config.dictConfig(load_logger_yaml())

    main()
