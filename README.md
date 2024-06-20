# Contents
- [Contents](#contents)
- [AngularJS Dynamic Web Scraper](#angularjs-dynamic-web-scraper)
- [Use case examples](#use-case-examples)
- [Features](#features)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Setup](#setup)
- [Usage](#usage)
  - [Help:](#help)
  - [Basic Usage:](#basic-usage)
  - [Options](#options)
- [Contributing](#contributing)


# AngularJS Dynamic Web Scraper

This is a dynamic web scraper specifically designed for AnsularJS websites that runs at specified time intervals.
This can be used to monitor when a new element is added to the website instead of having to manually refresh it.

Instead of looking at the source, it waits until all elements are loaded to retrieve the results by using a browser driver

Whenever a new element is discovered, it will notify you and save it to a file so that it doesn't notify you again for that same element in the future.

# Use case examples
This is useful, for example to notify you when a certain keyword is found on a website, such as:

- New job on a job board
- New product on an online store
- New article on a blog post
- ...

# Features

- **Automated Scraping:** Runs at user-defined intervals, extracting data without manual input.
- **Notification System:** Notifies users via Windows notifications when new data is found.
- **Robust Parsing:** Utilizes customizable search strings and regular expressions for data extraction.


# Installation

## Requirements

```bash
git
```

You also need to install the latest geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and add it to your PATH.

## Setup

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

# Usage

## Help:
```bash
python src/web_scraper.py --help
```

## Basic Usage:

```bash
python scraper.py -u "https://www.example.com" -s "search this text"
```

## Options

- `--url, -u`: Required. The URL of the webpage from which to fetch data.

- `--search_string, -s`: Required. The string you want to search for within the webpage.

- `--regex, -r`: Optional. The regular expression pattern used to search within the webpage. Default = `search_string`.

- `--interval, -i`: Optional. The interval in minutes at which the script should run repeatedly. Default is 5 minutes. Default = `5`.

- `--json_path, -j`: Optional. The file path where the found results will be saved as JSON. Default is a path relative to the script location. Default = `data/results.json`.

- `--verbose, -v`: Optional. Enable verbose mode to receive more detailed output in the terminal during script execution.


_Note: The results will be appended to the specified JSON file, creating a historical data log if run repeatedly._


# Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your suggested changes.
