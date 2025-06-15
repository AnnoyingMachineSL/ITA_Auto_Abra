import time
from pages.base_page import BasePage
from playwright.sync_api import expect


class CreateNewPasswordPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.NEW_PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/input')
        self.CONFIRM_NEW_PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[2]/input')
        self.CREATE_NEW_PASSWORD_TITLE = self.page.locator('//*[@id="root"]/div/div/div/div[1]')
        self.ENTER_NEW_PASSWORD_TEXT = self.page.locator('//*[@id="root"]/div/div/div/div[2]')
        self.SAVE_NEW_PASSWORD_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/form/button')

    def fill_new_password_field(self, password):
        self.NEW_PASSWORD_FIELD.fill(password)

    def fill_confirm_password_field(self, password):
        self.CONFIRM_NEW_PASSWORD_FIELD.fill(password)

    def find_create_new_password_title(self):
        expect(self.CREATE_NEW_PASSWORD_TITLE).to_be_visible()

    def click_on_enter_new_password_text(self):
        self.ENTER_NEW_PASSWORD_TEXT.click()

    def click_on_save_new_password_button(self):
        self.SAVE_NEW_PASSWORD_BUTTON.click()
        time.sleep(3)
