import argparse
import utils.config as config
from .helpers import is_windows
import os


def collect_arguments() -> argparse.Namespace:
    """
    Collects the arguments passed to the script
    """
    parser = argparse.ArgumentParser(
        description="Search for a specific string in a webpage and save matches to a JSON file."
    )
    parser.add_argument(
        "--url",
        "-u",
        required=True,
        type=str,
        help="URL to fetch data from",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="(Optional) Increase verbosity level (-v, -vv, -vvv, etc.)",
    )

    parser.add_argument(
        "--search-string",
        "-s",
        required=True,
        type=str,
        help="String to search for in the webpage",
    )

    parser.add_argument(
        "--locator-type",
        "-t",
        type=str,
        choices=config.locator_map.keys(),
        help="(Optional) Type of locator to wait for the element to load. (Default: xpath)",
        default="xpath",
    )

    parser.add_argument(
        "--locator-value",
        "-l",
        type=str,
        default="//section[@class='list-item ng-scope']",
        help="(Optional) Value of the locator to search for. (Default: //section[@class='list-item ng-scope'])",
    )

    parser.add_argument(
        "--regex",
        "-r",
        type=str,
        help="(Optional) Regex pattern to store the results nicely, instead of the whole block",
    )

    parser.add_argument(
        "--interval",
        "-i",
        type=int,
        default=5,
        help="(Optional) Interval in minutes to run the script repeatedly. Default = 5 minutes",
    )

    parser.add_argument(
        "--use-previous",
        "-p",
        action="store_true",
        help="(Optional) Use results from previous runs, if present",
    )

    parser.add_argument(
        "--no-headless",
        action="store_true",
        help="(Optional) Don't run the browser in headless mode",
    )

    # Determine the operating system
    if is_windows():
        # Windows-specific default path
        default_path_directory = os.path.join(os.environ["APPDATA"], "Dynamic-Scraper")
        os.makedirs(os.path.dirname(default_path_directory), exist_ok=True)

        # Create a default path for Windows
        default_path = os.path.join(
            os.environ["APPDATA"], "Dynamic-Scraper", "results.json"
        )
    else:
        # Default path for Linux (and other Unix-like OS)
        default_path = os.path.join(
            os.path.expanduser("~"), ".dynamic_scraper_results.json"
        )

    parser.add_argument(
        "--json_path",
        "-j",
        required=False,
        type=str,
        default=default_path,
        help="(Optional) Specific path to save the found results as JSON.",
    )

    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        default=False,
        help="(Optional) Suppress all notifications, only get output in the console",
    )

    args = parser.parse_args()
    return args
