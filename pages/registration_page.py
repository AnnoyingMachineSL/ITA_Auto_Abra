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
        self.EMPTY_EMAIL_ERROR_MESSAGE = self.page.get_by_text('Email is required')
        self.INVALID_EMAIL_ERROR_MESSAGE = self.page.get_by_text('Invalid email')
        self.EMPTY_PASSWORD_ERROR_MESSAGE = self.page.get_by_text('Password is required')
        self.INVALID_PASSWORD_ERROR_MESSAGE = self.page.get_by_text('Password must match the next requirements')
        self.ABRA_LOGO = self.page.locator('//*[@id="root"]/div/div/div/a')
        self.PASSWORD_RULES_TEXT = self.page.locator('//*[@id="root"]/div/div/div/form/div[4]')
        self.GOOGLE_REGISTRATION_BUTTON = self.page.locator('//*[@id="bg-search"]')
        self.LOGIN_LINK = self.page.locator('//*[@id="root"]/div/div/div/div[3]/a')
        self.ABRA_COPYRIGHT = self.page.locator('//*[@id="root"]/div/div/footer/div/div/p')
        self.TERMS_AND_CONDITIONS_LINK = self.page.locator('//*[@id="root"]/div/div/footer/div/div/a[1]')
        self.PRIVACY_POLICY_LINK = self.page.locator('//*[@id="root"]/div/div/footer/div/div/a[2]')

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

    def check_empty_email_error_message(self):
        expect(self.EMPTY_EMAIL_ERROR_MESSAGE).to_be_visible()

    def check_invalid_email_error_message(self):
        expect(self.INVALID_EMAIL_ERROR_MESSAGE).to_be_visible()

    def check_empty_password_error_message(self):
        expect(self.EMPTY_PASSWORD_ERROR_MESSAGE).to_be_visible()

    def check_invalid_password_error_message(self):
        expect(self.INVALID_PASSWORD_ERROR_MESSAGE).to_be_visible()

    def find_abra_logo(self):
        expect(self.ABRA_LOGO).to_be_visible()

    def find_start_buying_text(self):
        expect(self.START_BUYING_TEXT).to_be_visible()

    def find_buyer_button(self):
        expect(self.BE_BUYER_BUTTON).to_be_visible()

    def find_seller_button(self):
        expect(self.BE_SELLER_BUTTON).to_be_visible()

    def find_email_field(self):
        expect(self.LOGIN_FIELD).to_be_visible()

    def find_password_field(self):
        expect(self.PASSWORD_FIELD).to_be_visible()

    def find_password_rules_text(self):
        expect(self.PASSWORD_RULES_TEXT).to_be_visible()

    def find_create_account_button(self):
        expect(self.CREATE_ACCOUNT_BUTTON).to_be_visible()

    def find_google_registration_button(self):
        expect(self.GOOGLE_REGISTRATION_BUTTON).to_be_visible()

    def find_login_link(self):
        expect(self.LOGIN_LINK).to_be_visible()

    def find_abra_copyright(self):
        expect(self.ABRA_COPYRIGHT).to_be_visible()

    def find_terms_and_conditions_link(self):
        expect(self.TERMS_AND_CONDITIONS_LINK)

    def find_privacy_policy_link(self):
        expect(self.PRIVACY_POLICY_LINK).to_be_visible()

    def click_on_login_page_link(self):
        self.LOGIN_LINK.click()

    def click_on_terms_and_conditions_link(self):
        self.TERMS_AND_CONDITIONS_LINK.click()

    def click_on_privacy_policy_link(self):
        self.PRIVACY_POLICY_LINK.click()


