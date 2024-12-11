from pages.locators.contact_page_locators import ContactPageLocators
from base.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = ContactPageLocators