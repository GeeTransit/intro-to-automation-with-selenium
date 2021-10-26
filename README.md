# intro-to-automation-with-selenium
 Automatically fills a Google Form using Selenium

## Setup

Clone this repository.

Get Python here: https://www.python.org/downloads/

Get Poetry here: https://python-poetry.org/docs/#installation

Install dependencies using: `poetry install`

Get the Firefox Selenium webdriver here: https://github.com/mozilla/geckodriver/releases

Move the Selenium webdriver into the same folder.

## Run

Run the script using: `poetry run python script.py`

## Notes

There can be multiple CSS selectors that all find the same element. Don't worry
if your code uses a different way of reaching an element.

For a different browser, you can change the code from `webdriver.Firefox()` to
user some other class, including `Chrome`, `Edge`, `Safari`, and more.

Get other webdrivers: https://selenium-python.readthedocs.io/installation.html#drivers
