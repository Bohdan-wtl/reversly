class SignUpPageLocators:

    def __init__(self, page):
        self.email_input = page.locator("//input[@id='input']")
        self.continue_button = page.locator("//div[@class='submit-btn-modal']")
        self.payment_form_iframe = page.locator("//form[@id='payment-form']//iframe")
        self.payment_frame = self.payment_form_iframe.content_frame
        self.card_number_input = self.payment_frame.locator("//input[@id='Field-numberInput']")
        self.exp_date_input = self.payment_frame.locator("//input[@id='Field-expiryInput']")
        self.cvc_input = self.payment_frame.locator("//input[@id='Field-cvcInput']")
        self.country_select = self.payment_frame.locator("//select[@id='Field-countryInput']")
        self.submit_button = self.payment_frame.locator("//button[@id='submit']")
        self.payment_email_input = self.payment_frame.locator("//input[@id='Field-linkEmailInput']")
        self.payment_phone_number_input = self.payment_frame.locator("//input[@id='Field-linkMobilePhoneInput']")
        self.payment_country_select = self.payment_frame.locator("//select[@id='Field-linkMobilePhoneCountryInput']")
        self.payment_legal_name_input = self.payment_frame.locator("//input[@id='Field-linkLegalNameInput']")
        self.alert = page.locator("//div[@role='alert']")
        self.payment_spinner = page.locator("//div[contains(@class, 'spinning')]")