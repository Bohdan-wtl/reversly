from pages.locators.main_page_locators import MainPageLocators
from base.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = MainPageLocators