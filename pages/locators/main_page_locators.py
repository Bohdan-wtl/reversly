class MainPageLocators:

    def __init__(self, page):
        self.login_button = page.locator("//div[@class='header-login-btn']")
        self.phone_number_input = page.locator("//div[@class='HomeBanner__Content']//input[@id='phone_input']")
        self.first_country_code_input = page.locator("(//div[@class='reverslyInputDesktop']//input[@name='phone'])[1]")
        self.second_country_code_input = page.locator("(//div[@class='reverslyInputDesktop']//input[@name='phone'])[2]")
        self.logo_in_header = page.locator("//div[@class='HeaderLogo__wrapper']")
        self.languages_dropdown = page.locator("//div[@class='header-lang-drop']")
        self.faq_button = page.locator("(//div[@class='HeaderMenuList']//li)[1]")
        self.pricing_button = page.locator("(//div[@class='HeaderMenuList']//li)[2]")
        self.contact_button = page.locator("(//div[@class='HeaderMenuList']//li)[3]")
        self.unsubscribe_button = page.locator("(//div[@class='HeaderMenuList']//li)[4]")