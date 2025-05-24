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
        login_page.open_page(AbraLoginConfig.BASE_PAGE_URL)
        login_page.click_login_button()
        login_page.fill_login_field(AbraLoginConfig.LOGIN)
        login_page.fill_password_field(AbraLoginConfig.PASSWORD)
        login_page.click_log_in_buttom()
        login_page.check_post_log_in_header()