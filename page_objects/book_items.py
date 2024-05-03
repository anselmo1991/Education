from selene import browser, Element
import allure


class BookElement(Element):

    def __init__(self, locator):
        super().__init__(locator, browser.config)

    def title(self):
        return self.element(".//div[@class='h2']/a")

    def description(self):
        return self.element(".//div[@class='b-book_item__description']/div[1]")

    def to_library_button(self):
        return self.element(".//div[@class='b-btn-mobile_none']/div/a")

    def number_of_comments(self):
        return self.element('.//div[contains(@class,"b-btn-mobile_none")]//div[@class="b-book_item__counters"]/div/div[2]//div[@class="_cnt"]')

    def book_menu_button(self):
        return self.element(".//div[@class='col-12 col-xl-auto b-btn-mobile_none']//div[@class='status-library__button']//a[1]")

    def delete_button(self):
        return self.element(".//div[@class='b-menu_drop active']/ul/li[6]/a")

    @allure.step("Add book to the library")
    def click_to_library_button(self):
        self.to_library_button().click()

    @allure.step("Delete book from the library")
    def click_delete_from_library_button(self):
        self.delete_button().click()

    @allure.step("Open book menu in library")
    def click_menu_in_library_button(self):
        self.book_menu_button().click()
