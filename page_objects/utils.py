from tests.web_tests.constants import PLATFORM
from selene import browser


def locator_for_platform(selectors):
    return selectors.get(PLATFORM, 'Undefined Selector')


def element(selectors):
    return browser.element(locator_for_platform(selectors))


def elements(selectors):
    return browser.all(locator_for_platform(selectors))
