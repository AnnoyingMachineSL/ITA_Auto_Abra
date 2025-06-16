import time
from pages.base_page import BasePage
from playwright.sync_api import expect


class ForgotPasswordPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.FORGOT_PASSWORD_TITLE = self.page.locator('//*[@id="root"]/div/div/div/form/div/input')
        self.FORGOT_EMAIL_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div/input')
        self.RESET_PASSWORD_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/form/button')
        self.POST_RESET_PASSWORD_TEXT = self.page.locator('//*[@id="root"]/div/div/div/div[1]/div[1]')
        self.ENTER_EMAIL_TEXT = self.page.locator('//*[@id="root"]/div/div/div/div[2]')

    def find_forgot_password_title(self):
        expect(self.FORGOT_PASSWORD_TITLE).to_be_visible()

    def click_on_forgot_password_title(self):
        self.FORGOT_PASSWORD_TITLE.click()

    def fill_forgot_password_email_field(self, email):
        self.FORGOT_EMAIL_FIELD.fill(email)

    def click_on_reset_password_button(self):
        self.RESET_PASSWORD_BUTTON.click()

    def find_post_reset_password_text(self):
        expect(self.POST_RESET_PASSWORD_TEXT).to_be_visible()

    def click_on_enter_email_text(self):
        self.ENTER_EMAIL_TEXT.click()