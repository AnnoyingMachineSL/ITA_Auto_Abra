import allure
import pytest
from pages.login_page import LoginPage
from utils.config import AbraLoginConfig, AbraRegistrationConfig


@allure.title('[Positive] Following links from login page')
@allure.severity(allure.severity_level.TRIVIAL)
class TestFollowingLinksFromLoginPage:

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Following link to forgot password page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_following_to_forgot_password_page(self, page):
        login_page = LoginPage(page)

        with allure.step('Open login page'):
            login_page.open_page(AbraLoginConfig.LOGIN_PAGE_URL)

        with allure.step('Click on forgot password page link'):
            login_page.click_on_forgot_password_button()

        with allure.step('Search a correct direction'):
            login_page.correct_direction(AbraLoginConfig.FORGOT_PASSWORD_URL)

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Following link to registration page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_following_to_registration_page(self, page):
        login_page = LoginPage(page)

        with allure.step('Open login page'):
            login_page.open_page(AbraLoginConfig.LOGIN_PAGE_URL)

        with allure.step('Click on create account link'):
            login_page.click_on_create_account_button()

        with allure.step('Search a correct direction'):
            login_page.correct_direction(AbraRegistrationConfig.REGISTRATION_URL)

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Following link to terms and conditions page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_following_to_terms_and_conditions_page(self, page):
        login_page = LoginPage(page)

        with allure.step('Open login page'):
            login_page.open_page(AbraLoginConfig.LOGIN_PAGE_URL)

        with allure.step('Click on terms and conditions page link'):
            login_page.click_on_terms_and_conditions_button()

        with allure.step('Search a correct direction'):
            login_page.correct_direction(AbraRegistrationConfig.TERMS_AND_CONDITIONS_URL)

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Following link to privacy policy page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_following_to_privacy_policy_page(self, page):
        login_page = LoginPage(page)

        with allure.step('Open registration page url'):
            login_page.open_page(AbraLoginConfig.LOGIN_PAGE_URL)

        with allure.step('Click on privacy policy page link'):
            login_page.click_on_privacy_policy_button()

        with allure.step('Search a correct direction'):
            login_page.correct_direction(AbraRegistrationConfig.PRIVACY_POLICY_URL)
