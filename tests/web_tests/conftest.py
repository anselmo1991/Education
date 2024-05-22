import pytest
import os
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import allure
from selene.support.shared import browser
from tests.web_tests.constants import TEST_URL, PLATFORM
from appium import webdriver as appium_driver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()


def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    return appium_driver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


def choose_device():
    browser_name = os.getenv("DEFAULT_BROWSER", "chrome")
    if browser_name == 'chrome':
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Pixel 3a API 34',
            appPackage='com.android.chrome',
            appActivity='com.google.android.apps.chrome.Main',
            language='en',
            locale='US',
            newCommandTimeout=1000
        )
        return create_android_driver(capabilities)


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

    browser.config.driver_remote_url = 'http://selenium-hub:4444'
    browser.config.driver_options = options


@pytest.fixture(autouse=True)
def open_browser():
    if PLATFORM == "PC":
        choose_browser()
        browser.open(TEST_URL)
        yield browser
        browser.quit()
    if PLATFORM == 'MOBILE':
        driver = choose_device()
        browser.config.driver = driver
        browser.element('//android.widget.Button[@resource-id="com.android.chrome:id/signin_fre_dismiss_button"]').click()
        browser.element('//android.widget.Button[@resource-id="com.android.chrome:id/negative_button"]').click()
        # browser.element('//android.widget.Button[@resource-id="com.android.chrome:id/more_button"]').click()
        # browser.element('//android.widget.Button[@resource-id="com.android.chrome:id/ack_button"]').click()
        driver.get(TEST_URL)
        yield browser
        driver.quit()


def pytest_exception_interact(node, call, report):
    if report.failed:
        try:
            allure.attach(browser.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
