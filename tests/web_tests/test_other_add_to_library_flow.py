import allure
from page_objects.header import fill_password_form, fill_email_form, click_login_button, open_books_dropdown, \
    click_genre_in_dropdown, go_to_my_library
from page_objects.search_results_page import get_book_by_title, fill_book_name_in_search_field
from page_objects.my_library import find_book_in_the_library, open_exit_from_profile_menu
from page_objects.my_library import push_exit_button, confirm_deletion, click_dropdown_menu, click_prochitano
from page_objects.book_page import click_forward_button, click_in_library_button, click_sign_in_button


@allure.title("Checking whether a book has been added in 'Прочитано' folder")
@allure.description(
    'We go to the site, add the selected book to the library, change status of book, check that book is in '
    '"Прочитано" folder in user"s library')
def test_the_book_has_been_added_to_the_library():
    book_title = 'Это всегда был он'
    genre = 'Молодёжный роман'
    open_books_dropdown()
    click_genre_in_dropdown(genre)
    fill_book_name_in_search_field(book_title)
    book = get_book_by_title(book_title)
    book.click_read_button()
    for _ in range(3):
        click_forward_button()
        pass
    click_in_library_button()
    click_sign_in_button()
    fill_email_form()
    fill_password_form()
    click_login_button()
    click_in_library_button()
    go_to_my_library()
    find_book_in_the_library(book_title)
    book.click_menu_in_library_button()
    book.click_prochitano_button()
    click_dropdown_menu()
    click_prochitano()
    book = get_book_by_title(book_title)
    book.click_menu_in_library_button()
    book.click_delete_from_library_button()
    confirm_deletion()
    open_exit_from_profile_menu()
    push_exit_button()
