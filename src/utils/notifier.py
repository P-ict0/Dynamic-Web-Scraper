from win11toast import notify


def notify_user(message: str, url: str) -> None:
    """
    Send a notification to the user

    :param message: The message to display in the notification
    :param url: The URL to open when the notification is clicked
    """

    # Notify as a windows toast notification
    notify(
        f"Found: {message}",
        "click to open the page",
        on_click=url,
        duration="long",
    )

# Testing
if __name__ == "__main__":
    notify_user(message="Test notification", url="https://www.google.com")
