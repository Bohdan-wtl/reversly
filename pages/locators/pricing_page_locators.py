class PricingPageLocators:

    def __init__(self, page):
        self.subscribe_button = page.locator("//button[@class='hl_cta_wrap-white']")
        self.main_title = page.locator("//div[@class='pricing-main-title']")
        self.image_box = page.locator("//div[@class='img-box']")
        self.image_box_header = page.locator("//div[@class='img-box']/div[@class='box-heading']/p")
        self.image_box_description = page.locator("//div[@class='img-box']/div[@class='desc-special-span']/p")
        self.subscribe_box = page.locator("//div[@class='img-box-3']")
        self.subscribe_box_header = page.locator("//div[@class='img-box-3']/div[@class='box-heading']/p")
        self.subscribe_box_amount = page.locator("//div[@class='img-box-3']/div[@class='desc-special']/h3")
        self.subscribe_box_annual = page.locator("//div[@class='img-box-3']/div[@class='desc-special']/p")
        self.subscribe_box_description = page.locator("//div[@class='img-box-3']/div[@class='desc-special-span']/p")