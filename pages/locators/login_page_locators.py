class LoginPageLocators:

    def __init__(self, page):
        self.email_input = page.locator("//input[@id='email']")
        self.password_input = page.locator("//input[@id='password']")
        self.continue_button = page.locator("//div[@class='submit-btn-modal']")
        self.reset_password_button = page.locator("//div[@class='forget-pass-modal']")
        self.modal_title = page.locator("//div[@class='login-modal-title']")