import allure
from page_objects.main_page import open_login_form, fill_password_form, fill_email_form, click_login_button
from page_objects.main_page import go_to_novels
from page_objects.search_results_page import add_book_to_the_library, go_to_my_library
from page_objects.my_library import find_book_in_the_library, delete_book_from_the_library


@allure.title("Checking whether a book has been added to the library")
@allure.description(
    'We go to the site, add the selected book to the library, check whether the added book is in the user’s library')
def test_the_book_has_been_added_to_the_library():
    open_login_form()
    fill_email_form()
    fill_password_form()
    click_login_button()
    go_to_novels()
    add_book_to_the_library()
    go_to_my_library()
    find_book_in_the_library()
    delete_book_from_the_library()
