from selene import query
from selene.support.conditions import be, have
from selene.support.shared import browser

comments_filter = browser.element('//a[text()=" По количеству комментариев "]')
all_counters = browser.all('//div[contains(@class,"b-btn-mobile_none")]//div['
                           '@class="b-book_item__counters"]/div/div[2]//div[@class="_cnt"]')
books = browser.all('//div[@class="b-book_item__info"]/div/div[2]')


def range_comments():
    comments_filter.should(be.visible).click()


def counters_list():
    return all_counters.should(have.size(20))


def books_list():
    return books.should(have.size(20))


def check_comments_order():
    comments_list = [int(element.get(query.text)) for element in all_counters]
    comments_sorted = sorted(comments_list, reverse=True)
    assert comments_list == comments_sorted, "Error: lists do not match"


def genre_check(genre):
    for book_element in books:
        tags = list()
        for element in book_element.all('a'):
            tags.append(element.get(query.text).strip())
        is_genre = any((genre.lower() in item.lower()) for item in tags)
        assert is_genre
