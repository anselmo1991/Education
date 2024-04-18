import pytest
from selene import query
from selene.support.conditions import be, have

from tests.constants import TEST_URL, SELECTOR_FILTER_BY_FANTASY, SELECTOR_SORT_BY_COMMENTS, SELECTOR_COUNTERS, \
    SELECTOR_BOOK_INFO


@pytest.mark.parametrize('open_browser', [TEST_URL], indirect=True)
def test_litgorod_sort_comments_by_desc(open_browser):
    open_browser.element(SELECTOR_FILTER_BY_FANTASY).should(be.visible).click()
    open_browser.element(SELECTOR_SORT_BY_COMMENTS).should(be.visible).click()
    open_browser.all(SELECTOR_COUNTERS).should(have.size(40))

    comments = list()
    for element in open_browser.all(SELECTOR_COUNTERS):
        text = element.get(query.text)
        if text != '':
            comments.append(text)

    flag = 0
    i = 1
    while i < len(comments):
        if comments[i] >= comments[i - 1]:
            flag = 1
        i += 1

    assert flag == 0


@pytest.mark.parametrize('open_browser', [TEST_URL], indirect=True)
def test_litgorod_filter_by_fantasy(open_browser):
    open_browser.element(SELECTOR_FILTER_BY_FANTASY).should(be.visible).click()
    open_browser.all(SELECTOR_BOOK_INFO).should(have.size(20))

    for book_element in open_browser.all(SELECTOR_BOOK_INFO):
        tags = list()
        for element in book_element.all('a'):
            tags.append(element.get(query.text).strip())
        is_fantasy = any(("фэнтези" in item.lower()) for item in tags)
        assert is_fantasy
