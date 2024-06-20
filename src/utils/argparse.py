import argparse
import pathlib


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
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose mode in the terminal",
    )

    parser.add_argument(
        "--search_string",
        "-s",
        required=True,
        type=str,
        help="String to search for in the webpage",
    )

    parser.add_argument(
        "--regex",
        "-r",
        required=False,
        type=str,
        help="Regex pattern to search for in the webpage",
    )

    parser.add_argument(
        "--interval",
        "-i",
        required=False,
        type=int,
        default=5,
        help="Interval in minutes to run the script repeatedly",
    )

    parser.add_argument(
        "--json_path",
        "-j",
        required=False,
        type=str,
        default=fr"{pathlib.Path(__file__).parent.parent.parent.resolve()}\data\results.json",
        help="Path to save the found results as JSON",
    )

    args = parser.parse_args()
    return args