from pages.locators.account_page_locators import AccountPageLocators
from base.base_page import BasePage

class AccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = AccountPageLocators