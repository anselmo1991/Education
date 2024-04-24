import allure
from selene import query
from selene.support.conditions import be, have
from selene.support.shared import browser

comments_filter = browser.element('//a[text()=" По количеству комментариев "]')
all_counters = browser.all('//div[contains(@class,"b-btn-mobile_none")]//div['
                           '@class="b-book_item__counters"]/div/div[2]//div[@class="_cnt"]')
books = browser.all('//div[@class="b-book_item__info"]/div/div[2]')


@allure.step("Comment sorting")
def sort_books_by_comments_number():
    comments_filter.should(be.visible).click()


@allure.step("List of the number of comments")
def find_list_of_comments_counters():
    return all_counters.should(have.size(20))


@allure.step("List of books")
def should_see_twenty_books_in_search_results():
    return books.should(have.size(20))


@allure.step("Comparing the order of numbers in comments")
def books_should_be_sorted_by_comments_descending():
    comments_list = [int(element.get(query.text)) for element in all_counters]
    comments_sorted = sorted(comments_list, reverse=True)
    assert comments_list == comments_sorted, "Error: lists do not match"


@allure.step("A comparison of the book's genre")
def books_genre_should_match_with_genre_filter(genre):
    for book_element in books:
        tags = list()
        for element in book_element.all('a'):
            tags.append(element.get(query.text).strip())
        is_genre = any((genre.lower() in item.lower()) for item in tags)
        assert is_genre
