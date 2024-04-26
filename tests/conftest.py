import pytest
from selene import browser
from selenium import webdriver
from tests.constants import TEST_URL


# browser.config.driver_name = os.getenv("DEFAULT_BROWSER", "firefox")
options = webdriver.ChromeOptions()
browser.config.driver_options = options
browser.config.driver_remote_url = 'http://localhost:4444'


@pytest.fixture(autouse=True)
def open_browser():
    """
    Open browser
    """
    browser.open(TEST_URL)
    yield browser
    browser.quit()
