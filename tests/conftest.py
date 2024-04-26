import pytest
from selene import browser
from selenium import webdriver
from tests.constants import TEST_URL


# browser.config.driver_name = os.getenv("DEFAULT_BROWSER", "firefox")
def choose_browser(browser_name):
    if browser_name == 'chrome':
        option = webdriver.ChromeOptions()
    elif browser_name == 'firefox':
        option = webdriver.FirefoxOptions()
    elif browser_name == 'edge':
        option = webdriver.EdgeOptions()
    else:
        raise ValueError("Unsupported browser name")

    browser.config.driver_remote_url = 'http://localhost:444'
    browser.config.driver_options = option


@pytest.fixture(autouse=True)
def open_browser(browser_name):
    choose_browser(browser_name)
    browser.open(TEST_URL)
    yield browser
    browser.quit()
