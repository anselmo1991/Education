import pytest


@pytest.mark.parametrize('open_browser', ["https://www.google.com"], indirect=True)
def test_browser(open_browser):
    open_browser.close()


@pytest.mark.parametrize('open_browser', ["https://www.google.com"], indirect=True)
def test_browser2(open_browser):
    open_browser.close()
