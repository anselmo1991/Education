from selene import query
from selene.support.conditions import be, have
from selene.support.shared import browser


def range_comments():
    comments_filter = browser.element('//a[text()=" По количеству комментариев "]')
    comments_filter.should(be.visible).click()


def counters_list():
    all_counters = browser.all('//div[contains(@class,"b-btn-mobile_none")]//div['
                               '@class="b-book_item__counters"]/div/div[2]//div[@class="_cnt"]')
    all_counters.should(have.size(20))
    return all_counters


def books_list():
    books = browser.all('//div[@class="b-book_item__info"]/div/div[2]')
    books.should(have.size(20))
    return books


def check_comments_order(counters):
    comments_list = [int(element.get(query.text)) for element in counters]
    comments_sorted = sorted(comments_list, reverse=True)
    assert comments_list == comments_sorted, "Error: lists do not match"


def fantasy_check(books):
    for book_element in books:
        tags = list()
        for element in book_element.all('a'):
            tags.append(element.get(query.text).strip())
        is_fantasy = any(("фэнтези" in item.lower()) for item in tags)
        assert is_fantasy
