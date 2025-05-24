from pages.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.LOGIN_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/a[2]')
        self.LOGIN_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/input')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[2]/input')
        self.LOG_IN_BUTTON = self.page.locator('//*[@id="root"]/div/div/div/form/button')
        self.HEADER_ACTIONS = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]')
        self.START_BUYING_TEXT = self.page.get_by_text('Start buying in bulk now!')

    def click_login_button(self):
        self.LOGIN_BUTTON.click()

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)

    def click_log_in_buttom(self):
        self.LOG_IN_BUTTON.click()

    def check_post_log_in_header(self):
        expect(self.HEADER_ACTIONS).to_be_visible()

    def click_on_start_buying_text(self):
        self.START_BUYING_TEXT.click()

