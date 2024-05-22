import allure
import pytest

from page_objects.header import open_login_form, fill_email_form, fill_password_form, click_login_button, go_to_my_library
from page_objects.main_page import go_to_novels
from page_objects.search_results_page import get_book_by_title
from page_objects.my_library import find_book_in_the_library, open_exit_from_profile_menu
from page_objects.my_library import push_exit_button, confirm_deletion


@allure.title("Checking whether a book has been added to the library")
@allure.description(
    'We go to the site, add the selected book to the library, check whether the added book is in the user’s library')
@pytest.mark.web
def test_the_book_has_been_added_to_the_library():
    book_title = 'Помощница для большого босса'
    open_login_form()
    fill_email_form()
    fill_password_form()
    click_login_button()
    go_to_novels()
    book = get_book_by_title(book_title)
    book.click_to_library_button()
    go_to_my_library()
    find_book_in_the_library(book_title)
    book.click_menu_in_library_button()
    book.click_delete_from_library_button()
    confirm_deletion()
    open_exit_from_profile_menu()
    push_exit_button()
