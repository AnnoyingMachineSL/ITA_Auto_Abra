import allure
import pytest
from pages.login_page import LoginPage
from utils.config import AbraLoginConfig


@allure.title('[Positive] Search elements in login page')
@allure.severity(allure.severity_level.TRIVIAL)
class TestSearchLoginPageElements:

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Search elements in login page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_login_page_elements(self, page):
        login_page = LoginPage(page)

        with allure.step('Open login page url'):
            login_page.open_page(AbraLoginConfig.LOGIN_PAGE_URL)

        with allure.step('Search abra logo element'):
            login_page.find_abra_logo_element()

        with allure.step('Search start buying text'):
            login_page.find_start_buying_text()

        with allure.step('Search login field'):
            login_page.find_login_field()

        with allure.step('Search password field'):
            login_page.find_password_field()

        with allure.step('Search log in button'):
            login_page.find_login_button()

        with allure.step('Search google login button'):
            login_page.find_google_login_button()

        with allure.step('Search forgot password button'):
            login_page.find_forgot_password_button()

        with allure.step('Search create account button'):
            login_page.find_create_account_button()

        with allure.step('Search abra copyright'):
            login_page.find_abra_copyright()

        with allure.step('Search link to terms and condition page'):
            login_page.find_terms_and_conditions_link()

        with allure.step('Search link to privacy policy'):
            login_page.find_privacy_policy_link()
