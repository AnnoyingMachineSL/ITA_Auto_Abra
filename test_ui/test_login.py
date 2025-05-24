import re
import allure
import pytest

from pages.login_page import LoginPage
from utils.config import AbraLoginConfig


@allure.title('[Positive] Login Test')
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:

    @pytest.mark.positive
    @allure.title('[UI][Positive] Login test')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, page):
        login_page = LoginPage(page)
        with allure.step('Open main page'):
            login_page.open_page(AbraLoginConfig.BASE_PAGE_URL)

        with allure.step('Click on login buttom'):
            login_page.click_login_button()

        with allure.step('Fill login and password'):
            login_page.fill_login_field(AbraLoginConfig.LOGIN)
            login_page.fill_password_field(AbraLoginConfig.PASSWORD)

        with allure.step('Click on text on the page'):
            login_page.click_on_start_buying_text()

        with allure.step('Click log in buttom'):
            login_page.click_log_in_buttom()

        with allure.step('Check post login header on main page'):
            login_page.check_post_log_in_header()
