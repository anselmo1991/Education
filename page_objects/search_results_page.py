import allure
from selene import query
from hamcrest import assert_that, equal_to, is_in, has_length
from selene.support.conditions import be, have
from selene.support.shared import browser
from selenium.webdriver import Keys

from page_objects.book_items import BookElement

comments_filter = browser.element('//a[text()=" По количеству комментариев "]')
books = browser.all("//div[@class='b-book_item']")
search_field = browser.element("//div[@class='b-input b-input-block']//input")
search_button = browser.element("//div[@class='b-input b-input-block']//a")


@allure.step("Find a book by title")
def get_book_by_title(book_title):
    book = books.should(have.size_greater_than(0)).by_their(lambda x: BookElement(x).title(),
                                                            have.text(book_title)).should(have.size(1))[0]
    return BookElement(book)


@allure.step("Sort books by number of comments")
def sort_books_by_comments_number():
    comments_filter.should(be.visible).click()


@allure.step("Create a list of 20 comment counters")
def get_list_of_comments_counters():
    list_of_comments = [int(BookElement(book).number_of_comments().get(query.text)) for book in books]
    assert_that(list_of_comments, has_length(20))
    return list_of_comments


@allure.step("Form a list of 20 books found")
def should_see_twenty_books_in_search_results():
    return books.should(have.size(20))


@allure.step("Check if the comments are arranged in descending order")
def books_should_be_sorted_by_comments_descending():
    comments_list = get_list_of_comments_counters()
    comments_sorted = sorted(comments_list, reverse=True)
    assert_that(comments_list, equal_to(comments_sorted), "Error: lists do not match")


@allure.step("Check if the selected genre is present in the book")
def books_genre_should_match_with_genre_filter(genre):
    for book_element in books:
        genre = genre.lower()
        tags = [element.get(query.text).strip().lower() for element in book_element.all('a')]
        assert_that(genre, is_in(tags), f"Genre '{genre}' is not found in book tags")


@allure.step("Fill book's name in search field")
def fill_book_name_in_search_field(book_title):
    search_field.should(be.visible).send_keys(book_title, Keys.ENTER)


@allure.step("Click search button")
def click_search_button():
    search_button.should(be.visible).click()
