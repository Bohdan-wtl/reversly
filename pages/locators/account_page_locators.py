class AccountPageLocators:

    def __init__(self, page):
        self.account_info_title = page.locator("(//div[@class='account_title']/h2)[1]")
        self.account_billing_info_title = page.locator("(//div[@class='account_title']/h2)[2]")
        self.account_subscription_title = page.locator("(//div[@class='account_title']/h2)[3]")
        self.first_name_input = page.locator("//input[@id='first-name']")
        self.street_address_input = page.locator("//input[@id='street-address']")
        self.country_dropdown = page.locator("//div[@name='country']")
        self.city_input = page.locator("//input[@id='city']")
        self.postal_code_input = page.locator("//input[@id='postal-code']")
        self.save_button = page.locator("//button[@class='payment__account']")