#!/usr/bin/env python3

import logging
import logging.config

from dict_config import logger
from dict_config.module import library


logging.config.dictConfig(logger.CONFIG)

LOGGER = logging.getLogger(__name__)


def main():
    LOGGER.debug('enter main()')

    library.do_something()

    LOGGER.debug('exit main()')


if __name__ == '__main__':
    main()
