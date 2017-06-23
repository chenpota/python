#!/usr/bin/env python3

import logging
import logging.config

from dict_config import logger
from dict_config.module import library


LOGGER = logging.getLogger('dict_config.app')


def main():
    LOGGER.debug('enter main()')

    library.do_something()

    LOGGER.debug('exit main()')


if __name__ == '__main__':
    logging.config.dictConfig(logger.CONFIG)

    main()
