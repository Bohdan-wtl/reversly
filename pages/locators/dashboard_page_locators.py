class DashboardPageLocators:

    def __init__(self, page):
        self.tutorial_next_button = page.locator("//button[@class='btn btn-primary']")
        self.tutorial_modal = page.locator("//div[@class='tutorial_bg_wrap']")
        self.tutorial_modal_text = page.locator("//div[@class='tutorial__cmt']/p")
        self.reciever_phone_input = page.locator("//div[@class='dashboard-locate']/input[@id='phone_input']")
        self.modal_message_input = page.locator("//div[@class='dashboard-locate']/textarea")
        self.modal_continue_button = page.locator("//button[@class='hl_cta_wrap']")
        self.modal_preview_button = page.locator("//button[@class='hl_clr_btn']")
        self.modal_close_button = page.locator("//button[@aria-label='Close']")
        self.mobile_phone_input = page.locator("//div[@class='main_container']//input[@id='phone_input']")
        self.search_button = page.locator("//button[@id='btnSubmit']")
        self.records_table = page.locator("//div[contains(@class, 'wpb_report_wrapper')]")
        self.first_record = page.locator("(//div[@class='wpb_text_content'])[1]")
        self.first_record_phone_number = page.locator("(//div[@class='wpb_text_content'])[1]//p[@class='mobile_number']")
        self.first_record_status = page.locator("(//div[@class='wpb_text_content'])[1]//span[@class]")
        self.first_record_open_report = page.locator("(//div[@class='wpb_text_content'])[1]//div[@class='vc_general_btn']")
        self.burger_menu = page.locator("//div[@class='ant-dropdown-trigger']/div[@class='openbtn']")