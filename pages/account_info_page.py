import time
from pages.base_page import BasePage
from playwright.sync_api import expect


class AccountInfoPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.ACCOUNT_INFO_LOGO = self.page.locator('//*[@id="root"]/div/div/div/div/p[1]')
        self.FIRST_NAME_FIELD = self.page.locator('//*[@id="firstName"]')
        self.LAST_NAME_FIELD = self.page.locator('//*[@id="lastName"]')
        self.PHONE_NUMBER_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/fieldset/div[2]/label/div/input')
        self.CONTINUE_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/form/button')

    def search_account_info_logo(self):
        expect(self.ACCOUNT_INFO_LOGO).to_be_visible()
