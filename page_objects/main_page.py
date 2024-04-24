import allure
from selene.support.conditions import be
from selene.support.shared import browser


@allure.title("Go to the genre page")
@allure.description("Go to the genre page")
def go_to_genre(genre_name):
    browser.element(f'//a[text()="{genre_name}"]').should(be.visible).click()
