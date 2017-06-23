#!/usr/bin/env python3

import logging
import logging.config

from app import library
from app import logger


def main():
    LOGGER = logging.getLogger('app.main')

    LOGGER.debug('enter main()')

    library.do_something()

    LOGGER.debug('exit main()')


if __name__ == '__main__':
    logging.config.dictConfig(logger.CONFIG)

    main()
