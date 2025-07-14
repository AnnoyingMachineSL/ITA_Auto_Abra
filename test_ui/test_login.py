import re
import time

import allure
import pytest

from pages.login_page import LoginPage
from utils.config import AbraLoginConfig


@allure.title('[Positive] Login Test')
@pytest.mark.positive
@pytest.mark.UI
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:

    @pytest.mark.positive
    @pytest.mark.UI
    @allure.title('[UI][Positive] Login test')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, page):
        login_page = LoginPage(page)
        with allure.step('Open main page'):
            login_page.open_page(AbraLoginConfig.BASE_PAGE_URL)

        with allure.step('Click on login button'):
            login_page.click_login_button()

        with allure.step('Fill login and password'):
            login_page.fill_login_field(AbraLoginConfig.LOGIN)
            login_page.fill_password_field(AbraLoginConfig.NEW_PASSWORD)

        with allure.step('Click on text on the page'):
            login_page.click_on_start_buying_text()

        with allure.step('Click log in button'):
            login_page.click_log_in_button()

        with allure.step('Check post login header on main page'):
            login_page.check_post_log_in_header()


@allure.title('[Negative] Login Test')
@pytest.mark.negative
@pytest.mark.UI
@allure.severity(allure.severity_level.NORMAL)
class TestLoginNegative:

    @pytest.mark.negative
    @pytest.mark.UI
    @allure.title('[UI][Negative] Login test')
    @pytest.mark.parametrize('email, password', [('', 'qwe123'), ('qwe123', ''), ('@gmail.com', 'a')])
    def test_login_negative(self, page, email, password):

        login_page = LoginPage(page)
        with allure.step('Open main page'):
            login_page.open_page(AbraLoginConfig.BASE_PAGE_URL)

        with allure.step('Click on login button'):
            login_page.click_login_button()

        with allure.step(f'Fill login field by {email}'):
            login_page.fill_login_field(email)
            login_page.click_on_start_buying_text()

        with allure.step('Check error message for email field'):
            if len(email) == 0:
                login_page.check_empty_email_error_message()
            else:
                login_page.check_invalid_email_error_message()

        with allure.step(f'Fill password field by {password}'):
            login_page.fill_password_field(password)
            login_page.click_on_start_buying_text()

        with allure.step('Check error message for password field'):
            if len(password) == 0:
                login_page.check_empty_password_error_message()
            else:
                login_page.check_invalid_password_error_message()
