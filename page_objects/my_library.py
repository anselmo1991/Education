import allure
from hamcrest import assert_that
from selene.support.conditions import be, have
from selene import browser

from page_objects.book_items import BookElement
from page_objects.header import burger_menu
from page_objects.utils import elements, element
from tests.web_tests.constants import PLATFORM

books = elements({
    "PC": "//div[@class='b-book_item']",
    "MOBILE": "//div[@class='b-book_item']"})
confirm_delete = element({
    "PC": "//div[@class='col-6 mb-2']/a",
    "MOBILE": "//div[@class='col-6 mb-2']/a"})
exit_menu_button = element({
    "PC": "//div[@class='b-menu_side']/ul/li[14]/a",
    "MOBILE": "//div[@class='b-header_sidebar__container']/div[2]//li[10]/a"})
exit_button = element({
    "PC": "//div[@class='col-6 mb-2']/a",
    "MOBILE": "//div[@class='col-6 mb-2']/a"})
dropdown_menu = element({
    "PC": "//div[@class='ui-select w-auto mb-2']/button",
    "MOBILE": "//div[@class='ui-select w-auto mb-2']/button"})
prochitano = element({
    "PC": "//div[@class='options-wrapper hidden visible']/div/div[4]",
    "MOBILE": "//div[@class='options-wrapper hidden visible']/div/div[4]"})
account = browser.element('//div[@class="b-header_sidebar__list"]//li[3]/a')


@allure.step("Find the book in the library")
def find_book_in_the_library(book_title):
    assert_that(books.by_their(lambda x: BookElement(x).title(), have.exact_text(book_title)).should(have.size(1)))


@allure.step("Confirm deletion of the book")
def confirm_deletion():
    confirm_delete.should(be.visible).click()


@allure.step("Open exit from profile menu")
def open_exit_from_profile_menu():
    if PLATFORM == "PC":
        exit_menu_button.should(be.visible).click()
    if PLATFORM == "MOBILE":
        burger_menu.should(be.visible).click()
        account.should(be.visible).click()
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
