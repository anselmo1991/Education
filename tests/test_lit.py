from page_objects.main_page import fantasy_category
from page_objects.search_results_page import range_comments, counters_list
from page_objects.search_results_page import check_comments_order, books_list, fantasy_check


def test_litgorod_sort_comments_by_desc():
    fantasy_category()
    range_comments()
    counters = counters_list()
    check_comments_order(counters)


def test_litgorod_filter_by_fantasy():
    fantasy_category()
    books_lit = books_list()
    fantasy_check(books_lit)
