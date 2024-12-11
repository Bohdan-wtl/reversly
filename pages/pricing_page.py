from pages.locators.pricing_page_locators import PricingPageLocators
from base.base_page import BasePage

class PricingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = PricingPageLocators