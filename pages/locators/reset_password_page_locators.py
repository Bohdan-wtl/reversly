class ResetPasswordPageLocators:

    def __init__(self, page):
        self.email_field = page.locator("//input[@name='email']")