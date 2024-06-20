import re
from bs4 import BeautifulSoup


class Parser:
    """
    Class to parse the page source and return any new results
    """

    def __init__(self, string_to_search: str, regex: str, logger) -> None:
        """
        Initialize the parser with the string to search and the regex pattern

        :param string_to_search: String to search for in the page
        :param regex: Regex pattern to search for in the page
        :param logger: Logger object
        """

        self.string_to_search = string_to_search
        self.logger = logger
        self.regex = re.compile(regex)

    def parse_page(self, page_source: str) -> list:
        """
        Parse the page source and return any new results

        :param page_source: Page source to parse
        :return: List of new results
        """
        soup = BeautifulSoup(page_source, "lxml")
        results = []
        for item in soup.find_all("section", class_="list-item ng-scope"):
            if self.string_to_search in item.text:
                results.append(self.regex.search(item.text).group())
        return results
