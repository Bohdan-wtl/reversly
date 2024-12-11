from pages.locators.unsubscribe_page_locators import UnsubscribePageLocators
from base.base_page import BasePage

class UnsubscribePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = UnsubscribePageLocators