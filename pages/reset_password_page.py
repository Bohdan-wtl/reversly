from pages.locators.reset_password_page_locators import ResetPasswordPageLocators
from base.base_page import BasePage

class ResetPasswordPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = ResetPasswordPageLocators