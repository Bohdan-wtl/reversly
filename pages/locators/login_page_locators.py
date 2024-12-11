class LoginPageLocators:

    def __init__(self, page):
        self.email_field = page.locator("//input[@id='email']")
        self.password_field = page.locator("//input[@id='password']")
        self.continue_button = page.locator("//div[@class='submit-btn-modal']")