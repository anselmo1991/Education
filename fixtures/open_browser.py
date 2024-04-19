import pytest
from selene import browser

from tests.constants import TEST_URL

browser.config.driver_name = 'firefox'


@pytest.fixture(autouse=True)
def open_browser():
    """
    Open browser
    """
    browser.open(TEST_URL)
    yield browser
    browser.quit()
