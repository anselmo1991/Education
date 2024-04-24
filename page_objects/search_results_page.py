import allure
from selene import query
from selene.support.conditions import be, have
from selene.support.shared import browser

comments_filter = browser.element('//a[text()=" По количеству комментариев "]')
all_counters = browser.all('//div[contains(@class,"b-btn-mobile_none")]//div['
                           '@class="b-book_item__counters"]/div/div[2]//div[@class="_cnt"]')
books = browser.all('//div[@class="b-book_item__info"]/div/div[2]')


@allure.title("Comment sorting")
@allure.description("Sorting comments in descending order")
def sort_books_by_comments_number():
    comments_filter.should(be.visible).click()


@allure.title("List of the number of comments")
@allure.description("Get a list with the number of comments")
def find_list_of_comments_counters():
    return all_counters.should(have.size(20))


@allure.title("List of books")
@allure.description("Get a list of books")
def should_see_twenty_books_in_search_results():
    return books.should(have.size(20))


@allure.title("Comparing the order of numbers in comments")
@allure.description("We compare whether the list with the number of comments received on the site coincides with the "
                    "descending list of the number of comments.")
def books_should_be_sorted_by_comments_descending():
    comments_list = [int(element.get(query.text)) for element in all_counters]
    comments_sorted = sorted(comments_list, reverse=True)
    assert comments_list == comments_sorted, "Error: lists do not match"


@allure.title("A comparison of the book's genre")
@allure.description("We compare whether at least one genre of the book matches the selected one")
def books_genre_should_match_with_genre_filter(genre):
    for book_element in books:
        tags = list()
        for element in book_element.all('a'):
            tags.append(element.get(query.text).strip())
        is_genre = any((genre.lower() in item.lower()) for item in tags)
        assert is_genre
