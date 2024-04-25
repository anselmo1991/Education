import os
import pytest
from selene import browser
from tests.constants import TEST_URL


@pytest.fixture(autouse=True)
def browser_instance():
    default_browser = os.getenv("DEFAULT_BROWSER", "firefox")
    browser.config.driver = default_browser
    yield browser
    browser.quit()


def open_browser(browser_instance, browser_name=None):
    browser.config.driver = browser_name
    browser_instance.open(TEST_URL)

