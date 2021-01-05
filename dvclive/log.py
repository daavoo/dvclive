import logging
import logging.config
import os

from dvclive import env


def log_setup():
    level = int(os.environ.get(env.DVCLIVE_LOG_LEVEL, str(logging.WARNING)))
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s %(levelname)s %(name)s: %(message)s"
            },
        },
        "handlers": {
            "default": {
                "level": "DEBUG",
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "dvclive": {
                "handlers": ["default"],
                "level": level,
                "propagate": False,
            },
        },
    }
    logging.config.dictConfig(LOGGING_CONFIG)
