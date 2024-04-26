import pytest
from selene import browser
from selenium import webdriver
from tests.constants import TEST_URL


# browser.config.driver_name = os.getenv("DEFAULT_BROWSER", "firefox")
def setup(self):
    options = webdriver.ChromeOptions()
    self.driver = webdriver.Remote(
        command_executor="https://USERNAME:localhost",
        options=options
    )
    self.driver.implicitly_wait(30)


@pytest.fixture(autouse=True)
def open_browser():
    """
    Open browser
    """
    browser.open(TEST_URL)
    yield browser
    browser.quit()
