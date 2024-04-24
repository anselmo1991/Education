import pytest
import allure
from page_objects.main_page import go_to_genre
from page_objects.search_results_page import should_see_twenty_books_in_search_results, find_list_of_comments_counters
from page_objects.search_results_page import sort_books_by_comments_number, \
    books_should_be_sorted_by_comments_descending, books_genre_should_match_with_genre_filter


@allure.title("Comparing the order of numbers in comments")
@allure.description("We compare whether the list with the number of comments received on the site coincides with the "
                    "descending list of the number of comments.")
@pytest.mark.parametrize("genre_name", ["Фэнтези", "Боевик"])
def test_litgorod_sort_comments_by_desc(genre_name):
        go_to_genre(genre_name)
        sort_books_by_comments_number()
        find_list_of_comments_counters()
        books_should_be_sorted_by_comments_descending()


@allure.title("A comparison of the book's genre")
@allure.description("We compare whether at least one genre of the book matches the selected one")
@pytest.mark.parametrize("genre_name", ["Фэнтези", "Боевик"])
def test_litgorod_filter_by_fantasy(genre_name):
        go_to_genre(genre_name)
        should_see_twenty_books_in_search_results()
        books_genre_should_match_with_genre_filter(genre_name)
