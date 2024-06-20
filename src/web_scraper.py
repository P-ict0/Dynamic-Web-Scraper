import sys
import path
from functools import wraps
import time

# directory reach
directory = path.Path(__file__)

# setting path
sys.path.append(directory.parent)

from utils.argparse import collect_arguments
from utils.browser import Browser
from utils.notifier import notify_user
from utils.parser import Parser
from utils.json import Json
from utils.logger import Logger


# Run the script every [interval] minutes
def repeat_every(get_interval):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            interval = get_interval(*args, **kwargs)
            while True:
                start_time = time.time()
                func(*args, **kwargs)
                sleep_time = interval - (time.time() - start_time)
                if sleep_time > 0:
                    time.sleep(sleep_time)

        return wrapper

    return decorator


class Scraper:
    """
    Function to run the web scraper every x minutes and check for new results in the page
    """

    def __init__(self, script_args, verbose: bool = False) -> None:
        self.args = script_args
        self.logger = Logger(name=__name__, verbose=verbose).get_logger()

        # Initialize the iteration counter
        self.iteration = 1

    @repeat_every(lambda self: self.args.interval * 60)
    def scrape(self) -> None:
        """
        Main function to run the web scraper
        """

        self.logger.info(
            f"Starting the web scraper (iteration {self.iteration}), running every {self.args.interval} minutes"
        )

        # Load the JSON file and the webpage
        json = Json(path=self.args.json_path, logger=self.logger)
        browser = Browser(url=self.args.url, headless=True, logger=self.logger)
        page_source = browser.load_page()

        # Close the browser after loading the page
        browser.close_browser()

        # Parse the page and check for new results
        parser = Parser(self.args.search_string, self.args.regex, logger=self.logger)
        results = parser.parse_page(page_source)

        # Save new results to the JSON file and notify the user
        if results:
            found = json.new_results(results)
            if found:
                for item in found:
                    notify_user(
                        f"New result {item}!,\nClick to open url", self.args.url
                    )

        self.logger.info(
            f"Web scraper iteration {self.iteration} finished, next one starting in {self.args.interval} minutes"
        )

        self.iteration += 1


def main():
    args = collect_arguments()
    main = Scraper(
        script_args=args,
        verbose=args.verbose,
    )
    main.scrape()


if __name__ == "__main__":
    args = collect_arguments()
    main = Scraper(
        script_args=args,
        verbose=args.verbose,
    )
    main.scrape()
