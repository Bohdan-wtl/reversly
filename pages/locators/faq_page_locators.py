class FaqPageLocators:

    def __init__(self, page):
        self.questions_box = page.locator("//div[@class='question-collapse']")