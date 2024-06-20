import os

try:
    from win11toast import notify
except (ImportError, ModuleNotFoundError):  # Linux
    pass


def is_windows() -> bool:
    """
    Check the OS and send the notification

    :return: True if the OS is Windows, False otherwise
    """
    return True if os.name == "nt" else False


def notify_user(message: str, url: str) -> None:
    """
    Send a notification to the user

    :param message: The message to display in the notification
    :param url: The URL to open when the notification is clicked (Windows only)
    """

    windows = is_windows()

    if windows:
        # Notify as a windows toast notification
        notify(
            f"Found: {message}",
            "click to open the page",
            on_click=url,
            duration="long",
        )
    else:
        # Notify Linux users
        os.system(f"notify-send 'Found new result' '{message}'")


# Testing
if __name__ == "__main__":
    notify_user(message="Test notification", url="https://www.google.com")
