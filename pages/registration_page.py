from pages.base_page import BasePage
from playwright.sync_api import expect


class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.REGISTRATION_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/a[1]')
        self.LOGIN_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[2]/input')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[3]/input')
        self.BE_BUYER_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/button[1]')
        self.BE_SELLER_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/button[2]')
        self.CREATE_ACCOUNT_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/form/button')
        self.START_BUYING_TEXT = self.page.get_by_text('Start buying in bulk now!')
        self.POST_REGISTRATION_TEXT = self.page.get_by_text('A link for sign up has been sent to your email address.')
    def click_registration_button(self):
        self.REGISTRATION_BUTTON.click()

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)

    def click_be_buyer_button(self):
        self.BE_BUYER_BUTTON.click()

    def click_be_seller_button(self):
        self.BE_SELLER_BUTTON.click()

    def click_create_account_button(self):
        self.CREATE_ACCOUNT_BUTTON.click()

    def click_start_buying_text(self):
        self.START_BUYING_TEXT.click()

    def check_post_registration_text(self):
        expect(self.POST_REGISTRATION_TEXT).to_be_visible()
