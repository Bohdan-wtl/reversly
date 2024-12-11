from pages.main_page import MainPage
from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from pages.pricing_page import PricingPage
from pages.reset_password_page import ResetPasswordPage
from pages.unsubscribe_page import UnsubscribePage
from pages.faq_page import FaqPage


from pytest import fixture


class BaseTest:
    _main_page = None
    _contact_page = None
    _login_page = None
    _pricing_page = None
    _reset_password_page = None
    _unsubscribe_page = None
    _faq_page = None

    @fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page

    @property
    def main_page(self):
        if self._main_page is None:
            self._main_page = MainPage(self.page)
        return self._main_page

    @property
    def contact_page(self):
        if self._contact_page is None:
            self._contact_page = ContactPage(self.page)
        return self._contact_page

    @property
    def login_page(self):
        if self._login_page is None:
            self._login_page = LoginPage(self.page)
        return self._login_page

    @property
    def pricing_page(self):
        if self._pricing_page is None:
            self._pricing_page = PricingPage(self.page)
        return self._pricing_page

    @property
    def reset_password_page(self):
        if self._reset_password_page is None:
            self._reset_password_page = ResetPasswordPage(self.page)
        return self._reset_password_page

    @property
    def unsubscribe_page(self):
        if self._unsubscribe_page is None:
            self._unsubscribe_page = UnsubscribePage(self.page)
        return self._unsubscribe_page

    @property
    def faq_page(self):
        if self._faq_page is None:
            self._faq_page = FaqPage(self.page)
        return self._faq_page