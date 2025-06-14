from pages.base_page import BasePage
from playwright.sync_api import expect


class TermsAndConditionsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.TERMS_TITLE_TEXT = self.page.locator('//*[@id="root"]/div/div/div/h1')

    def find_title_text(self):
        self.TERMS_TITLE_TEXT.to_be_visible()
