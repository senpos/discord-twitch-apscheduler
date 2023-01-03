import logging


def setup_logging(*, debug):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level)
