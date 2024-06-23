# 😁 Welcome!!

# Contents
- [😁 Welcome!!](#-welcome)
- [Contents](#contents)
- [🌐 Dynamic Web Scraper](#-dynamic-web-scraper)
- [🚀 Quick start](#-quick-start)
- [💡 Use case examples](#-use-case-examples)
- [✨ Features](#-features)
- [📦 Installation](#-installation)
- [📲 Usage](#-usage)
- [⚙ Options](#-options)
- [✏ Manual Installation](#-manual-installation)
- [❌ Common errors](#-common-errors)
- [👥 Contributing](#-contributing)


# 🌐 Dynamic Web Scraper

💻 **Windows and Linux compatible.** 💻

This is a dynamic web scraper specifically designed for websites that have to wait for certain elements to load (such as AngularJS).
It runs at specified time intervals.
This can be used to monitor when a new element is added to the website instead of having to manually refresh it.

Instead of looking at the source, it waits until all elements are loaded to retrieve the results by using selenium and a Firefox driver.

Whenever a new element is discovered, it will notify you and save it to a file so that it doesn't notify you again for that same element in the future.

# 🚀 Quick start

```bash
pipx install dynamic-scraper
dynamic-scraper -u "https://www.example.com" -s "search this text"
```

# 💡 Use case examples
This is useful, for example to notify you when a certain keyword is found on a website, such as:

- New job on a job board
- New product on an online store
- New article on a blog post
- ...

# ✨ Features

- **Automated Scraping:** Runs at user-defined intervals, extracting data without manual input.
- **Notification System:** Notifies users via Windows notifications when new data is found.
- **Robust Parsing:** Utilizes customizable search strings and regular expressions for data extraction.


# 📦 Installation

(Go [below](#-manual-installation) for manual installation.)

From [PyPI](https://pypi.org/project/dynamic-scraper/)

`pipx` is optional but recommended, you can use `pip` instead.

`pipx`:
```bash
pipx install dynamic-scraper
```

`pip`:
```bash
pip install dynamic-scraper
```

<hr>

You can also clone the repository and install:
```bash
git clone https://github.com/P-ict0/Dynamic-Web-Scraper.git
cd Dynamic-Web-Scraper
pipx install .
```

# 📲 Usage

For help:
```bash
dynamic-scraper --help
```

General usage:
```bash
dynamic-scraper -u "https://www.example.com" -s "search this text"
```

Also see [common errors](#-common-errors) if you encounter any issues with the browser.

# ⚙ Options

| Option            | Short Form | Requirement | Default                                | Description                                                                                      |
|-------------------|------------|-------------|----------------------------------------|--------------------------------------------------------------------------------------------------|
| `--url`           | `-u`       | Required    | None                                   | The URL of the webpage from which to fetch data.                                                 |
| `--search-string` | `-s`       | Required    | None                                   | The string you want to search for within the webpage.                                            |
| `--version` | `-V`       | Optional    | None | Get current version                                                              |
| `--regex`         | `-r`       | Optional    | `search_string`                        | The regular expression pattern used to store the results nicely.                                 |
| `--interval`      | `-i`       | Optional    | `5`                                    | The interval in minutes at which the script should run repeatedly.                               |
| `--json_path`     | `-j`       | Optional    | Windows: `%APPDATA%/Roaming/Dynamic-Scraper/results.json`<br>Linux: `$HOME/.dynamic_scraper_results.json` | The file path where the found results will be saved as JSON.|
| `--use-previous`  | `-p`       | Optional    | `False`                                | Use results from previous runs, if present.                                                      |
| `--no-headless`   | None       | Optional    | `False`                                | Disable headless mode for the webdriver and run maximized.                                       |
| `--verbose`       | `-v`       | Optional    | None (thresshold: `WARNING`)           | Increase verbosity level (`-v`, `-vv`, etc.). INFO for `-v`, DEBUG for `-vv`.                    |
| `--quiet`         | `-q`       | Optional    | `False`                                | Suppress all notifications, only get output in the console.                                      |
| `--locator-type`  | `-t`       | Optional    | `xpath`                                | Type of locator to wait for the element to load. Options include various HTML attribute types.   |
| `--locator-value` | `-l`       | Optional    | `//section[@class='list-item ng-scope']` | Value of the locator to search for.                                                              |


# ✏ Manual Installation

```bash
git clone https://github.com/P-ict0/AngularJS-Dynamic-Web-Scraper.git
```

Recommended to use a virtual environment:
```bash
python3 -m venv venv

source venv/bin/activate  # Linux
venv\Scripts\activate  # Windows
```

```bash
pip install -r requirements.txt
```

You can now run:
```bash
python src/web_scraper/scraper.py [args]
```

# ❌ Common errors

You may also need to install the latest geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and add it to your PATH.

# 👥 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your suggested changes.
