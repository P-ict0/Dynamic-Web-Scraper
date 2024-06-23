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
from argparse import Namespace
from importlib.metadata import version


# Run the script every [interval] minutes
def repeat_every(get_interval):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            interval = get_interval(*args, **kwargs)
            while True:
                try:
                    start_time = time.time()
                    func(*args, **kwargs)
                    sleep_time = interval - (time.time() - start_time)
                    if sleep_time > 0:
                        time.sleep(sleep_time)
                # Ctrl-C
                except KeyboardInterrupt:
                    print("\nExiting web scraper...")
                    print(f"Ran {args[0].iteration} iterations")
                    sys.exit()

        return wrapper

    return decorator


class Scraper:
    """
    Function to run the web scraper every x minutes and check for new results in the page
    """

    def __init__(
        self,
        script_args: Namespace,
        logger: Logger,
        json: Json,
        parser: Parser,
    ) -> None:
        """
        Initialize the web scraper with the arguments passed to the script

        :param script_args: Arguments passed to the script
        :param logger: Logger object to log messages
        :param json: Json class object to save and load results
        :param parser: Parser object to parse the webpage
        """
        self.args = script_args
        self.logger = logger

        self.json = json
        self.parser = parser

        # Log the arguments passed to the script
        self.log_args()

        # Initialize the iteration counter
        self.iteration = 0

        # Check if first run
        self.first_run = True

    def log_args(self) -> None:
        """
        Log the arguments passed to the script
        """
        self.logger.debug("Program started with the following options:")
        for arg, value in vars(self.args).items():
            self.logger.debug(f"{arg}: {value}")

    @repeat_every(lambda self: self.args.interval * 60)
    def scrape(self) -> None:
        """
        Main function to run the web scraper every x minutes and check for new results in the page
        """
        self.iteration += 1

        self.logger.info(f"Starting web scraper iteration {self.iteration}")

        if self.first_run:
            print(f"\nStarting scraper at {time.strftime('%H:%M:%S')}...")
            self.first_run = False

        self.logger.info(f"Starting browser {self.args.url}...")
        browser = Browser(
            url=self.args.url,
            no_headless=self.args.no_headless,
            logger=self.logger,
            locator_type=self.args.locator_type,
            locator_value=self.args.locator_value,
        )

        page_source = browser.load_page()

        # Close the browser after loading the page
        browser.close_browser()

        # Parse the page and check for new results
        results = self.parser.parse_page(page_source)

        # Save new results to the JSON file and notify the user
        if results:
            found = self.json.new_results(results)
            if found:
                for item in found:
                    if not self.args.quiet:
                        notify_user(
                            f"New result {item}!,\nClick to open url", self.args.url
                        )
                    else:
                        print(f"New result found: {item}")

        self.logger.info(
            f"Web scraper iteration {self.iteration} finished, waiting {self.args.interval} minutes..."
        )


def run():
    args = collect_arguments()
    logger = Logger(name=__name__, verbosity_level=args.verbose).get_logger()
    program_version = version("dynamic-scraper")

    print(f"Initializing web scraper version {program_version}...")

    # Load the JSON file
    logger.info(f"(INIT) Loading JSON file from {args.json_path}")
    json = Json(
        path=args.json_path,
        use_previous=args.use_previous,
        logger=logger,
    )

    # Load the parser
    logger.info(
        f"(INIT) Loading parser with search string {args.search_string} and regex {args.regex}"
    )
    parser = Parser(args.search_string, args.regex, logger=logger)

    print(f"Running every {args.interval} minutes")
    main = Scraper(
        script_args=args,
        logger=logger,
        json=json,
        parser=parser,
    )
    main.scrape()


if __name__ == "__main__":
    run()
