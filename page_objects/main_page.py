import allure
from selene.support.shared import browser
from selene.support.conditions import be

from tests.web_tests.constants import PLATFORM


@allure.step("Go to genre page")
def go_to_genre(genre_name):
    if PLATFORM == "PC":
        browser.element(f'//a[text()="{genre_name}"]').should(be.visible).click()
    if PLATFORM == "MOBILE":
        browser.element('//div[@class="b-genres__header_mobile"]//a').click()
        browser.element(f'//a[text()="{genre_name}"]').should(be.visible).click()


@allure.step("Go to novels page")
def go_to_novels():
    if PLATFORM == "PC":
        browser.element(f'//a[text()="Современный любовный роман"]').should(be.visible).click()
    if PLATFORM == "MOBILE":
        browser.element('//div[@class="b-genres__header_mobile"]//a').click()
        browser.element(f'//a[text()="Современный любовный роман"]').should(be.visible).click()
