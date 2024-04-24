import allure
from selene.support.shared import browser

def pytest_exception_interact(node, call, report):
    if report.failed:
        try:
            allure.attach(browser.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")