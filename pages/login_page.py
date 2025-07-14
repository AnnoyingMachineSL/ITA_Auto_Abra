import time
from pages.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.LOGIN_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/a[2]')
        self.LOGIN_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/input')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[2]/input')
        self.LOG_IN_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/form/button')
        self.HEADER_ACTIONS = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/button')
        self.START_BUYING_TEXT = self.page.get_by_text('Start buying in bulk now!')
        self.EMPTY_EMAIL_ERROR_MESSAGE = self.page.get_by_text('Email is required')
        self.INVALID_EMAIL_ERROR_MESSAGE = self.page.get_by_text('Invalid email')
        self.EMPTY_PASSWORD_ERROR_MESSAGE = self.page.get_by_text('Password is required')
        self.INVALID_PASSWORD_ERROR_MESSAGE = self.page.get_by_text('Password must be at least 8 characters')
        self.ABRA_LOGO = self.page.locator('//*[@id="root"]/div/div/div/a')
        self.GOOGLE_LOGIN_BUTTON = self.page.locator('//*[@id="bg-search"]')
        self.FORGOT_PASSWORD_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/div[2]/a[1]')
        self.CREATE_ACCOUNT_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/div[2]/a[2]')
        self.ABRA_COPYRIGHT = self.page.locator('//*[@id="root"]/div/div/footer/div/div/p')
        self.TERMS_AND_CONDITIONS_LINK = self.page.locator('//*[@id="root"]/div/div/footer/div/div/a[1]')
        self.PRIVACY_POLICY_LINK = self.page.locator('//*[@id="root"]/div/div/footer/div/div/a[2]')

        #account_info page
        self.ACCOUNT_INFO_LOGO = self.page.locator('//*[@id="root"]/div/div/div/div/p[1]')



    def click_login_button(self):
        self.LOGIN_BUTTON.click()

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)

    def click_log_in_button(self):
        self.LOG_IN_BUTTON.click()

    def check_post_log_in_header(self):
        expect(self.HEADER_ACTIONS).to_be_visible()

    def click_on_start_buying_text(self):
        self.START_BUYING_TEXT.click()

    def check_empty_email_error_message(self):
        expect(self.EMPTY_EMAIL_ERROR_MESSAGE).to_be_visible()

    def check_invalid_email_error_message(self):
        expect(self.INVALID_EMAIL_ERROR_MESSAGE).to_be_visible()

    def check_empty_password_error_message(self):
        expect(self.EMPTY_PASSWORD_ERROR_MESSAGE).to_be_visible()

    def check_invalid_password_error_message(self):
        expect(self.INVALID_PASSWORD_ERROR_MESSAGE).to_be_visible()

    def find_abra_logo_element(self):
        expect(self.ABRA_LOGO).to_be_visible()

    def find_start_buying_text(self):
        expect(self.START_BUYING_TEXT).to_be_visible()

    def find_login_field(self):
        expect(self.LOGIN_FIELD).to_be_visible()

    def find_password_field(self):
        expect(self.PASSWORD_FIELD).to_be_visible()

    def find_login_button(self):
        expect(self.LOG_IN_BUTTON).to_be_visible()

    def find_google_login_button(self):
        expect(self.GOOGLE_LOGIN_BUTTON).to_be_visible()

    def find_forgot_password_button(self):
        expect(self.FORGOT_PASSWORD_BUTTON).to_be_visible()

    def find_create_account_button(self):
        expect(self.CREATE_ACCOUNT_BUTTON).to_be_visible()

    def find_abra_copyright(self):
        expect(self.ABRA_COPYRIGHT).to_be_visible()

    def find_terms_and_conditions_link(self):
        expect(self.TERMS_AND_CONDITIONS_LINK).to_be_visible()

    def find_privacy_policy_link(self):
        expect(self.PRIVACY_POLICY_LINK).to_be_visible()

    def click_on_forgot_password_button(self):
        self.FORGOT_PASSWORD_BUTTON.click()

    def click_on_create_account_button(self):
        self.CREATE_ACCOUNT_BUTTON.click()

    def click_on_terms_and_conditions_button(self):
        self.TERMS_AND_CONDITIONS_LINK.click()

    def click_on_privacy_policy_button(self):
        self.PRIVACY_POLICY_LINK.click()

    #account_info page
    def search_account_info_logo(self):
        expect(self.ACCOUNT_INFO_LOGO).to_be_visible()
