from page_objects.main_page import go_to_genre
from page_objects.search_results_page import range_comments, counters_list
from page_objects.search_results_page import check_comments_order, books_list, genre_check


def test_litgorod_sort_comments_by_desc():
    go_to_genre()
    range_comments()
    counters = counters_list()
    check_comments_order(counters)


def test_litgorod_filter_by_fantasy():
    go_to_genre()
    books_lit = books_list()
    genre_check(books_lit)
