"""Initialize project settings and logging."""

import logging
import pathlib
import sys
from logging.handlers import RotatingFileHandler
from types import TracebackType
from typing import Any

PROJECT_NAME = "app-track"

HOME = pathlib.Path.home()

# load config in /home/my-user/app-store/config.toml
TOP_CONFIGDIR = pathlib.Path(HOME, pathlib.Path(".config"))
CONFIG_DIR = pathlib.Path(TOP_CONFIGDIR, pathlib.Path(PROJECT_NAME))
CONFIG_FILENAME = "config.toml"
LOG_DIR = pathlib.Path(CONFIG_DIR, pathlib.Path("logs"))


def handle_exception(
    # ruff: noqa: ANN401
    exc_type: Any,
    exc_value: BaseException,
    exc_traceback: TracebackType | None,
) -> None:
    """Handle uncaught exceptions."""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def check_config_dirs() -> None:
    """Check that config dirs exist."""
    dirs = [TOP_CONFIGDIR, CONFIG_DIR, LOG_DIR]
    for _dir in dirs:
        if not pathlib.Path.exists(_dir):
            pathlib.Path.mkdir(_dir, exist_ok=True)


def get_logger(mod_name: str, log_name: str = "dash") -> logging.Logger:
    """Create a logger for use in other modules."""
    _format = "%(asctime)s: %(name)s: %(levelname)s: %(message)s"
    check_config_dirs()
    log_dir = pathlib.Path(HOME, pathlib.Path(f".config/{PROJECT_NAME}/logs"))
    if not pathlib.Path.exists(log_dir):
        pathlib.Path.mkdir(log_dir, exist_ok=True)
        # ruff: noqa: T201
        print(f"Couldn't find {log_dir=} so it was created.")
    filename = f"{log_dir}/{log_name}.log"
    # Writes to file
    rotate_handler = RotatingFileHandler(
        filename=filename,
        maxBytes=50000000,
        backupCount=5,
    )
    logging.basicConfig(
        format=_format,
        level=logging.INFO,
        handlers=[
            rotate_handler,
        ],
    )
    logger = logging.getLogger(mod_name)
    # create logger
    logger = logging.getLogger(mod_name)
    logger.setLevel(logging.INFO)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return logger


# Set global handling of uncaught exceptions
sys.excepthook = handle_exception

logger = get_logger(__name__)

DATE_FORMAT = "%Y-%m-%d"


DATE_FORMAT = "%Y-%m-%d"
