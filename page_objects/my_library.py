import allure
from hamcrest import assert_that
from selene.support.conditions import be, have
from selene.support.shared import browser
from page_objects.book_items import BookElement

books = browser.all("//div[@class='b-book_item']")
confirm_delete = browser.element("//div[@class='col-6 mb-2']/a")
exit_menu_button = browser.element("//div[@class='b-menu_side']/ul/li[14]/a")
exit_button = browser.element("//div[@class='col-6 mb-2']/a")
dropdown_menu = browser.element("//div[@class='ui-select w-auto mb-2']/button")
prochitano = browser.element("//div[@class='options-wrapper hidden visible']/div/div[4]")


@allure.step("Find the book in the library")
def find_book_in_the_library(book_title):
    assert_that(books.by_their(lambda x: BookElement(x).title(), have.exact_text(book_title)).should(have.size(1)))


@allure.step("Confirm deletion of the book")
def confirm_deletion():
    confirm_delete.should(be.visible).click()


@allure.step("Open exit from profile menu")
def open_exit_from_profile_menu():
    exit_menu_button.should(be.visible).click()


@allure.step("Push exit button")
def push_exit_button():
    exit_button.should(be.visible).click()


@allure.step("Click dropdown menu")
def click_dropdown_menu():
    dropdown_menu.should(be.visible).click()


@allure.step("Click Prochitano")
def click_prochitano():
    prochitano.should(be.visible).click()
