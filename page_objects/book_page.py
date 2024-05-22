import allure
from selene.support.conditions import be
from page_objects.utils import element

forward_button = element({
    "PC": "//div[@class='b-paging__container']//div[@class='_next']//a",
    "MOBILE": "//div[@class='b-paging__container']//div[@class='_next']//a"})
in_library_button = element({
    "PC": "//div[@class='b-annotation_button']/a",
    "MOBILE": "//div[@class='b-annotation_button']/a"})
sign_in_button = element({
    "PC": "//div[@class='register__signin']//a",
    "MOBILE": "//div[@class='register__signin']//a"})


@allure.step("Click forward button")
def click_forward_button():
    forward_button.should(be.visible).click()


@allure.step("Click 'In library' button")
def click_in_library_button():
    in_library_button.should(be.visible).click()


@allure.step("Click Sign in button")
def click_sign_in_button():
    sign_in_button.should(be.visible).click()
