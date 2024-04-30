import allure
from selene.support.conditions import be
from selene.support.shared import browser

book_search = browser.element("//div[@class='h2']//a[contains(text(), ' Сын маминой подруги')]")
read_button = browser.element("//div[@class='h2']//a[contains(text(), ' Сын маминой подруги')]//ancestor::div[@class='b-book_item__header']/following-sibling::div[2]//div[@class='status-library__button']//a")
delete_button = browser.element("//div[@class='h2']//a[contains(text(), ' Сын маминой подруги')]//ancestor::div[@class='b-book_item__header']/following-sibling::div[2]//div[@class='b-menu_drop active']/ul/li[6]/a")
confirm_delete = browser.element("//div[@class='col-6 mb-2']/a")
exit_menu_button = browser.element("//div[@class='b-menu_side']/ul/li[14]/a")
exit_button = browser.element("//div[@class='col-6 mb-2']/a")


@allure.step("Find the book in the library")
def find_book_in_the_library():
    assert book_search.should(be.visible), "Expected 1 book to be found in the library"


@allure.step("Open book menu")
def click_menu_button():
    read_button.should(be.visible).click()


@allure.step("Delete the book from the library")
def delete_book_from_the_library():
    delete_button.should(be.visible).click()


@allure.step("Confirm deletion of the book")
def confirm_deletion():
    confirm_delete.should(be.visible).click()


@allure.step("Open exit from profile menu")
def open_exit_from_profile_menu():
    exit_menu_button.should(be.visible).click()


@allure.step("Push exit button")
def push_exit_button():
    exit_button.should(be.visible).click()
