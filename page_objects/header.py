import allure
from selene.support.shared import browser
from selene.support.conditions import be, have
from tests.web_tests.constants import TEST_PASSWORD, TEST_LOGIN, PLATFORM
from page_objects.utils import element, elements

login_form = element({
    "PC": '//div[@class ="b-header__auth"]//a',
    "MOBILE": '//div[@class="b-header__menu_mobile"]//li[5]/a'})
email_input = element({
    "PC": '//input[@id="authorization_form_field_email"]',
    "MOBILE": '//input[@id="authorization_form_field_email"]'})
password_input = element({
    "PC": '//input[@id="authorization_form_field_pass"]',
    "MOBILE": '//input[@id="authorization_form_field_pass"]'})
login_button = element({
    "PC": '//a[@id="authorization_form_button_login"]',
    "MOBILE": '//a[@id="authorization_form_button_login"]'})
my_library = element({
    "PC": "//div[@class='b-header__menu']//a[contains(@href, 'https://litgorod.ru/user/library?status=1')]",
    "MOBILE": "//div[@class='b-header__menu_mobile']//a[contains(@href, 'https://litgorod.ru/user/library?status=1')]"})
books_dropdown = browser.element("//div[@class='b-header__menu']//li[1]/a")
genre_dropdown = elements({
    "PC": "//li[@class='b-header_dropdown__link']/a",
    "MOBILE": '//li[contains(@class,"b-header_sidebar__genre_link")]/a'})
burger_menu = browser.element('//div[@class="b-header__menu_mobile"]//li[1]/a')
list_of_burger_menu = browser.element('//div[@class="b-header_sidebar__list"]//li[6]/a')


@allure.step("Open login form")
def open_login_form():
    login_form.should(be.visible).click()


@allure.step("Fill email form")
def fill_email_form():
    email_input.set_value(TEST_LOGIN)


@allure.step("Fill password form")
def fill_password_form():
    password_input.set_value(TEST_PASSWORD)


@allure.step("Click login button")
def click_login_button():
    login_button.should(be.visible).click()


@allure.step("Go to my library")
def go_to_my_library():
    my_library.should(be.visible).click()


@allure.step("Open books dropdown")
def open_books_dropdown():
    if PLATFORM == "PC":
        books_dropdown.should(be.visible).click()
    if PLATFORM == "MOBILE":
        burger_menu.should(be.visible).click()
        list_of_burger_menu.should(be.visible).click()
        books_dropdown.should(be.visible).click()


@allure.step("Find genre in dropdown")
def click_genre_in_dropdown(genre):
    genre_dropdown.by_their(lambda x: x, have.text(genre)).should(have.size(1))[0].click()
