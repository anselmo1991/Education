from selene import browser, Element
import allure
from page_objects.utils import locator_for_platform


class BookElement(Element):

    def __init__(self, locator):
        super().__init__(locator, browser.config)

    def title(self):
        return self.element(locator_for_platform({
            "PC": ".//div[@class='h2']/a",
            "MOBILE": ".//div[@class='h2']/a"
        }))

    def description(self):
        return self.element(locator_for_platform({
            "PC": ".//div[@class='b-book_item__description']/div[1]",
            "MOBILE": ".//div[@class='b-book_item__description']/div[1]"
        }))

    def to_library_button(self):
        return self.element(locator_for_platform({
            "PC": ".//div[@class='b-btn-mobile_none']/div/a",
            "MOBILE": ".//div[@class='b-btn-desktop_none']/div/a"
        }))

    def number_of_comments(self):
        return self.element(locator_for_platform({
            "PC": './/div[contains(@class,"b-btn-mobile_none")]//div[@class="b-book_item__counters"]/div/div[2]//div[@class="_cnt"]',
            "MOBILE": './/div[contains(@class,"b-btn-desktop_none")]//div[@class="b-book_item__counters"]/div/div[2]//div[@class="_cnt"]'
        }))

    def book_menu_button(self):
        return self.element(locator_for_platform({
            "PC": ".//div[@class='col-12 col-xl-auto b-btn-mobile_none']//div[@class='status-library__button']//a[1]",
            "MOBILE": ".//div[@class='b-btn-desktop_none']//div[@class='status-library__button']//a[1]"
        }))

    def delete_button(self):
        return self.element(locator_for_platform({
            "PC": ".//div[@class='b-menu_drop active']/ul/li[6]/a",
            "MOBILE": ".//div[@class='b-menu_drop active']/ul/li[6]/a"
        }))

    @allure.step("Add book to the library")
    def click_to_library_button(self):
        self.to_library_button().click()

    @allure.step("Delete book from the library")
    def click_delete_from_library_button(self):
        self.delete_button().click()

    @allure.step("Open book menu in library")
    def click_menu_in_library_button(self):
        self.book_menu_button().click()

    def read_button(self):
        return self.element(locator_for_platform({
            "PC": ".//div[@class='mb-05 mb-sm-1']/a",
            "MOBILE": ".//div[@class='mb-05 mb-sm-1']/a"
        }))

    @allure.step("Click read button")
    def click_read_button(self):
        self.read_button().click()

    def prochitano_button(self):
        return self.element(locator_for_platform({
            "PC": ".//div[@class='b-menu_drop active']/ul/li[3]/a",
            "MOBILE": ".//div[@class='b-menu_drop active']/ul/li[3]/a"
        }))

    @allure.step("Click Prochitano button")
    def click_prochitano_button(self):
        self.prochitano_button().click()
