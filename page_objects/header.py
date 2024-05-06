import allure
from hamcrest import assert_that
from selene.support.shared import browser
from selene import Element
from selene.support.conditions import be, have
from tests.constants import TEST_PASSWORD, TEST_LOGIN

login_form = browser.element('//div[@class ="b-header__auth"]//a')
email_input = browser.element('//input[@id="authorization_form_field_email"]')
password_input = browser.element('//input[@id="authorization_form_field_pass"]')
login_button = browser.element('//a[@id="authorization_form_button_login"]')
my_library = browser.element("//div[@class='b-header__menu']//a[contains(@href, "
                             "'https://litgorod.ru/user/library?status=1')]")
books_dropdown = browser.element("//div[@class='b-header__menu']//li[1]/a")
genre_dropdown = browser.all("//li[@class='b-header_dropdown__link']")


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
    books_dropdown.should(be.visible).click()


class GenreElement(Element):

    def __init__(self, locator):
        super().__init__(locator, browser.config)

    def genre_name(self):
        return self.element("./a")

    @allure.step("Click genre link")
    def click_genre_link(self):
        self.genre_name().click()


@allure.step("Find genre in dropdown")
def find_genre_in_dropdown(genre):
    assert_that(genre_dropdown.by_their(lambda x: GenreElement(x).genre_name(), have.exact_text(genre)).should(have.size(1)))
