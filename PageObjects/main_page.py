from selene.support.conditions import be
from selene.support.shared import browser

fantasy_category = browser.element('//a[text()="Фэнтези"]')

click_fantasy_category = fantasy_category.should(be.visible).click()