class UnsubscribePageLocators:

    def __init__(self, page):
        self.email_field = page.locator("//input[@name='email']")
        self.main_title = page.locator("//div[@class='pricing-main-title']")
        self.unsubscribe_confirmation_text = page.locator("//div[@class='unsubscribe-confirmation']")
        self.email_field_title = page.locator("//div[@class='unsubscribe-input-email']/label")
        self.submit_button = page.locator("//div[@class='unsubscribe-email-submit']/button")
        self.unsubscribe_modal_text = page.locator("//div[@class='unsubscribe-text']")
        self.unsubscribe_confirm_button = page.locator("(//div[@class='submit-btn-modal']/button)[1]")
        self.unsubscribe_cancel_button = page.locator("(//div[@class='submit-btn-modal']/button)[2]")
        self.unsubscribe_modal_title = page.locator("//div[@class='login-modal-title']/p")
        self.unsubscribe_modal_close_button = page.locator("//button[@aria-label='Close']")