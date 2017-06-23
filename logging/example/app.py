#!/usr/bin/env python3

import logging

from module import library


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

LOGGER_HANDLER = logging.StreamHandler()
LOGGER_HANDLER.setLevel(logging.DEBUG)
LOGGER_HANDLER.setFormatter(
    logging.Formatter(
        '%(asctime)s - %(thread)d - %(name)s - %(levelname)s: %(message)s'))

LOGGER.addHandler(LOGGER_HANDLER)


def main():
    LOGGER.debug('enter main()')

    library.do_something()


if __name__ == '__main__':
    main()
