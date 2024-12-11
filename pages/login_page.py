from pages.locators.login_page_locators import LoginPageLocators
from base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = LoginPageLocators