class ResetPasswordPageLocators:

    def __init__(self, page):
        self.email_field = page.locator("//input[@name='email']")
        self.reset_modal_title = page.locator("//div[@class='reset-modal-title']")
        self.modal_email_label = page.locator("//label[@for='email']")
        self.close_button = page.locator("//button[@aria-label='Close']")