import allure
from selene.support.conditions import have, be
from selene.support.shared import browser

book_search = browser.element("//div[@class='h2']//a[contains(text(), ' Сын маминой подруги')]")
delete_button = browser.element(
    "//div[@class='h2']//a[contains(text(), ' Сын маминой подруги')]//ancestor::div[@class='b-book_item__header']/following-sibling::div[2]//li[6]/a")


@allure.step("Find the book in the library")
def find_book_in_the_library():
    assert book_search.should(have.size_greater_than(0)), "Book not found in the library"


@allure.step("Delete the book from the library")
def delete_book_from_the_library():
    delete_button.should(be.visible).click()
