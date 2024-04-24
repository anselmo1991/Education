import allure
from selene.support.conditions import be
from selene.support.shared import browser


@allure.step("go_to_genre_page")
def go_to_genre(genre_name):
    browser.element(f'//a[text()="{genre_name}"]').should(be.visible).click()
