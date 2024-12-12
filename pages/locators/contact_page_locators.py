class ContactPageLocators:

    def __init__(self, page):
        self.title = page.locator("//div[@class='pricing-main-title']")
        self.contact_box = page.locator("//div[@class='box-contact']")
        self.contact_box_title = page.locator("//div[@class='box-contact-title']")
        self.cantact_box_description = page.locator("//div[@class='box-contact-desc']")