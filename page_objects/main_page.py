import allure
from selene.support.shared import browser
from selene.support.conditions import be


@allure.step("Go to genre page")
def go_to_genre(genre_name):
    browser.element(f'//a[text()="{genre_name}"]').should(be.visible).click()


@allure.step("Go to novels page")
def go_to_novels():
    browser.element(f'//a[text()="Современный любовный роман"]').should(be.visible).click()
