from PageObjects.main_page import click_fantasy_category
from PageObjects.search_results_page import find_comments_filter, find_all_counters, check_comments_order, find_books, \
    fantasy_check


def test_litgorod_sort_comments_by_desc():
    click_fantasy_category
    find_comments_filter
    find_all_counters
    check_comments_order


def test_litgorod_filter_by_fantasy():
    click_fantasy_category
    find_books
    fantasy_check
