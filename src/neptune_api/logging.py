__all__ = ["LOGGER"]

import logging


def build_logger() -> logging.Logger:
    logger = logging.getLogger("neptune-api")
    logger.setLevel(logging.DEBUG)
    return logger


LOGGER = build_logger()
