from pages.locators.faq_page_locators import FaqPageLocators
from base.base_page import BasePage

class FaqPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = FaqPageLocators