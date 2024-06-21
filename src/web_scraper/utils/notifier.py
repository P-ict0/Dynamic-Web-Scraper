from .helpers import is_windows

try:
    from win11toast import notify
except (ImportError, ModuleNotFoundError):  # Linux
    pass


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
