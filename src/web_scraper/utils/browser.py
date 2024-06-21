from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .config import locator_map


class Browser:
    """
    Class to handle the browser
    """

    def __init__(
        self,
        url: str,
        logger,
        locator_type: str,
        locator_value: str,
        no_headless: bool = True,
    ) -> None:
        """
        Initialize the browser with the URL

        :param url: URL to load in the browser
        :param logger: Logger object
        :param locator_type: The type of locator to use
        :param locator_value: The value of the locator to search for until the page loads
        :param no_headless: Run the browser in headless
        """

        self.url = url
        self.no_headless = no_headless
        self.logger = logger

        # Set the locator
        self.locator = (locator_map[locator_type], locator_value)

        # Initialize the browser
        self.browser = self.init_browser()

    def init_browser(self) -> webdriver.Firefox:
        """
        Initialize the firefox browser with the correct options
        """

        self.logger.debug("(Browser) Initializing the browser")
        options = webdriver.FirefoxOptions()
        if self.no_headless:
            self.logger.debug("(Browser) Running in normal mode")
            options.add_argument("--start-maximized")
        else:
            self.logger.debug("(Browser) Running in headless mode")
            options.add_argument("--headless")

        browser = webdriver.Firefox(options=options)

        return browser

    def load_page(self) -> str:
        """
        Load the page and return the source
        """

        self.logger.debug(f"(Browser) Loading the page {self.url}")
        self.browser.get(self.url)
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.locator)
        )
        return self.browser.page_source

    def close_browser(self) -> None:
        """
        End the browser session
        """

        self.logger.debug("(Browser) Closing the browser")
        self.browser.quit()
