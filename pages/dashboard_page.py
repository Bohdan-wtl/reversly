from pages.locators.dashboard_page_locators import DashboardPageLocators
from base.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = DashboardPageLocators