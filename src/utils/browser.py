from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    """
    Class to handle the browser
    """

    def __init__(self, url: str, logger, no_headless: bool = True) -> None:
        """
        Initialize the browser with the URL

        :param url: URL to load in the browser
        :param logger: Logger object
        :param no_headless: Run the browser in headless
        """

        self.url = url
        self.no_headless = no_headless
        self.logger = logger
        self.browser = self.init_browser()

    def init_browser(self) -> webdriver.Firefox:
        """
        Initialize the firefox browser with the correct options
        """

        self.logger.debug("Browser: Initializing the browser")
        options = webdriver.FirefoxOptions()
        if self.no_headless:
            self.logger.debug("Browser: Running in normal mode")
            options.add_argument("--start-maximized")
        else:
            self.logger.debug("Browser: Running in headless mode")
            options.add_argument("--headless")

        browser = webdriver.Firefox(options=options)

        return browser

    def load_page(self) -> str:
        """
        Load the page and return the source
        """

        self.logger.debug(f"Browser: Loading the page {self.url}")
        self.browser.get(self.url)
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[@class='list-item ng-scope']")
            )
        )
        return self.browser.page_source

    def close_browser(self) -> None:
        """
        End the browser session
        """

        self.logger.debug("Browser: Closing the browser")
        self.browser.quit()
