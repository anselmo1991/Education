import pytest
import os
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from tests.constants import TEST_URL


def choose_browser():
    browser_name = os.getenv("DEFAULT_BROWSER", "firefox")
    if browser_name == 'chrome':
        options = ChromeOptions()
    elif browser_name == 'firefox':
        options = FirefoxOptions()
    elif browser_name == 'edge':
        options = EdgeOptions()
    else:
        raise ValueError("Unsupported browser name")

    browser.config.driver_remote_url = 'http://localhost:4444'
    browser.config.driver_options = options


@pytest.fixture(autouse=True)
def open_browser():
    choose_browser()
    browser.open(TEST_URL)
    yield browser
    browser.quit()
