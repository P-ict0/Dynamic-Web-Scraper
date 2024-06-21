import os


def is_windows() -> bool:
    """
    Check the OS and send the notification

    :return: True if the OS is Windows, False otherwise
    """
    return True if os.name == "nt" else False
