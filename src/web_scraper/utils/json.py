import json
import os


class Json:
    def __init__(self, path: str, use_previous: bool, logger) -> None:
        """
        Initialize the JSON file with the path and logger.

        :param path: Path to the JSON file
        :param logger: Logger object
        """

        self.path = path
        self.use_previous = use_previous
        self.logger = logger
        self.ensure_json()

    def save_results(self, result: str) -> None:
        """
        Save a single result to the JSON file.

        :param result: Result to save to the JSON file
        """

        self.logger.debug(f"Saving result: {result} to {self.path}")
        with open(self.path, "w") as file:
            json.dump(result, file)

    def new_results(self, results: list[str]) -> list[str]:
        """
        Add multiple results to JSON file if not already present, returns True if all were already present.

        :param results: List of results to add to the JSON file
        :return: list of results that were not already present
        """

        self.logger.debug(f"Checking for new results in {self.path}")
        with open(self.path, "r+") as file:
            data = json.load(file)
            found = []
            for result in results:
                if result not in data:
                    self.logger.info(f"(JSON) New result found: {result}")
                    data.append(result)
                    found.append(result)

            if found:
                file.seek(0)
                json.dump(data, file)
                file.truncate()
                print(f"Updated results: ")
                self.print_json()
            else:
                self.logger.info("(JSON) No new results found")

            return found

    def create_empty_json(self) -> None:
        """
        Create an empty JSON file.
        """
        self.logger.debug(f"(JSON) Creating empty JSON file: {self.path}")
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as file:
            json.dump([], file)

    def print_json(self) -> None:
        """
        Print the contents of the JSON file.
        """
        self.logger.debug(f"(JSON) Printing JSON file content: {self.path}")
        with open(self.path, "r") as file:
            data = json.load(file)
            pretty_data = json.dumps(data, indent=4)
            print(pretty_data)

    def ensure_json(self) -> None:
        """
        Ensure a JSON file exists and contains a list.
        """

        # Check if file exists and create with an empty list if it does not exist
        self.logger.debug(f"(JSON) Ensuring JSON file exists: {self.path}")
        if os.path.exists(self.path):
            self.logger.debug(f"(JSON) JSON file exists: {self.path}")
            if not self.use_previous:
                self.logger.debug(f"(JSON) Removing existing JSON file: {self.path}")
                os.remove(self.path)
                self.create_empty_json()
        else:
            self.logger.debug(f"(JSON) JSON file doesnt exist, creating: {self.path}")
            self.create_empty_json()

        # Open the file to check and modify content if necessary
        self.logger.debug(f"(JSON) Checking JSON file content: {self.path}")
        with open(self.path, "r+") as file:
            try:
                data = json.load(file)
                # If data is a single string, convert it to a list containing that string
                if isinstance(data, str):
                    data = [data]
                # If the file is empty or data is None, initialize to an empty list
                elif not data:
                    data = []
                # If data is not a list, log an error and initialize to an empty list
                elif not isinstance(data, list):
                    self.logger.warning(
                        "(JSON) JSON file content is not a list, initializing to an empty list"
                    )
                    data = []
            except json.JSONDecodeError:
                self.logger.error(
                    "(JSON) JSON file is corrupted, initializing to an empty list"
                )
                # If the file is empty or corrupted, initialize to an empty list
                data = []

            # Rewrite the file with the correct list data
            self.logger.debug(f"(JSON) Rewriting JSON file content: {self.path}")
            file.seek(0)
            json.dump(data, file)
            file.truncate()
