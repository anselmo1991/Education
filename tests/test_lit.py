import comments as comments
from selene import query
from selene.support.conditions import be, have
from tests.selectors import SELECTOR_FILTER_BY_FANTASY, SELECTOR_SORT_BY_COMMENTS, SELECTOR_COUNTERS, SELECTOR_BOOK_INFO
from selene.support.shared import browser


def test_litgorod_sort_comments_by_desc(open_browser):
    browser.element(SELECTOR_FILTER_BY_FANTASY).should(be.visible).click()
    browser.element(SELECTOR_SORT_BY_COMMENTS).should(be.visible).click()
    browser.all(SELECTOR_COUNTERS).should(have.size(20))

    comments_list = [element.get(query.text) for element in open_browser.all(SELECTOR_COUNTERS) if element.get(query.text) != '']


    # flag = 0
    # i = 1
    # while i < len(comments):
    #     if comments[i] >= comments[i - 1]:
    #         flag = 1
    #     i += 1
    #
    # assert flag == 0

    comments_sorted = sorted(comments_list, reverse=True)

    assert sorted(comments_list) == sorted(comments_sorted), "Error: lists do not match"


def test_litgorod_filter_by_fantasy(open_browser):
    browser.element(SELECTOR_FILTER_BY_FANTASY).should(be.visible).click()
    browser.all(SELECTOR_BOOK_INFO).should(have.size(20))

    for book_element in open_browser.all(SELECTOR_BOOK_INFO):
        tags = list()
        for element in book_element.all('a'):
            tags.append(element.get(query.text).strip())
        is_fantasy = any(("фэнтези" in item.lower()) for item in tags)
        assert is_fantasy
