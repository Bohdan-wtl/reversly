from pages.locators.sign_up_page_locators import SignUpPageLocators
from base.base_page import BasePage

class SignUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = SignUpPageLocators