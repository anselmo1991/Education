from selene.support.conditions import be
from selene.support.shared import browser


def fantasy_category():
    fantasy_category_element = browser.element('//a[text()="Фэнтези"]')
    fantasy_category_element.should(be.visible).click()
