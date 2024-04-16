import pytest
from selene import browser


browser.config.driver_name = 'firefox'


@pytest.fixture(autouse=True)
def open_browser(request):
    """
    Open browser
    """
    browser.open(request.param)
    yield browser
    browser.quit()
