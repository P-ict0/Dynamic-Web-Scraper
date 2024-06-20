import logging
from colorlog import ColoredFormatter


class Logger:
    """
    A simple console logger class that outputs colorized logs.
    """

    def __init__(self, name: str, verbose: bool = False) -> None:
        """
        Initialize a colorized console logger.

        Parameters:
        name (str): Name of the logger which is typically the name of the module creating the logger.
        verbose (bool): If True, the logger will output debug messages. Default is False.
        """
        # Create a logger
        self.logger = logging.getLogger(name)
        if verbose:
            self.logger.setLevel(
                logging.DEBUG
            )  # Set the threshold of logger to debug level
        else:
            self.logger.setLevel(
                logging.INFO
            )  # Set the threshold of logger to debug level

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create colored formatter
        formatter = ColoredFormatter(
            "%(log_color)s%(asctime)s => [%(levelname)s]%(reset)s %(white)s%(message)s",
            datefmt="%H:%M:%S",
            reset=True,
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
            secondary_log_colors={},
            style="%",
        )

        # Add formatter to console handler
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def get_logger(self) -> logging.Logger:
        """
        Returns the configured logger with colorized output.
        """
        return self.logger


if __name__ == "__main__":
    logger = Logger(__name__).get_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
