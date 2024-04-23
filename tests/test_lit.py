import pytest
from page_objects.main_page import go_to_genre
from page_objects.search_results_page import sort_books_by_comments_number, counters_list
from page_objects.search_results_page import check_comments_order, books_list, genre_check


@pytest.mark.parametrize("genre_name", ["Фэнтези", "Боевик"])
def test_litgorod_sort_comments_by_desc(genre_name):
    go_to_genre(genre_name)
    sort_books_by_comments_number()
    counters_list()
    books_should_be_sorted_by_comments_descending()


@pytest.mark.parametrize("genre_name", ["Фэнтези", "Боевик"])
def test_litgorod_filter_by_fantasy(genre_name):
    go_to_genre(genre_name)
    should_see_twenty_books_in_search_results()
    genre_check(genre_name)
