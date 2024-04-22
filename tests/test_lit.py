from selene import query
from selene.support.conditions import be, have
from tests.main_page import fantasy_category
from tests.search_results_page import comments_filter, books, all_counters

def test_litgorod_sort_comments_by_desc():
    fantasy_category.should(be.visible).click()
    comments_filter.should(be.visible).click()
    all_counters.should(have.size(20))

    comments_list = [int(element.get(query.text)) for element in all_counters]

    comments_sorted = sorted(comments_list, reverse=True)

    assert comments_list == comments_sorted, "Error: lists do not match"


def test_litgorod_filter_by_fantasy():
    fantasy_category.should(be.visible).click()
    books.should(have.size(20))

    for book_element in books:
        tags = list()
        for element in book_element.all('a'):
            tags.append(element.get(query.text).strip())
        is_fantasy = any(("фэнтези" in item.lower()) for item in tags)
        assert is_fantasy
