import time

import allure
import pytest
from pages.registration_page import RegistrationPage
from utils.config import AbraLoginConfig, AbraRegistrationConfig


@allure.title('[Positive] Search elements in registration page')
@allure.severity(allure.severity_level.TRIVIAL)
class TestSearchRegistrationElements:

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Search elements in registration page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_registration_page_elements(self, page):
        registration_page = RegistrationPage(page)

        with allure.step('Open registration page url'):
            registration_page.open_page(AbraRegistrationConfig.REGISTRATION_URL)

        with allure.step('Search abra logo element'):
            registration_page.find_abra_logo()

        with allure.step('Search start buying text'):
            registration_page.find_start_buying_text()

        with allure.step('Search be buyer button'):
            registration_page.find_buyer_button()

        with allure.step('Search be seller button'):
            registration_page.find_seller_button()

        with allure.step('Search login field '):
            registration_page.find_email_field()

        with allure.step('Search password field'):
            registration_page.find_password_field()

        with allure.step('Search password rules text'):
            registration_page.find_password_rules_text()

        with allure.step('Search create account button'):
            registration_page.find_create_account_button()

        with allure.step('Search google registration button'):
            registration_page.find_google_registration_button()

        with allure.step('Search link to login page'):
            registration_page.find_login_link()

        with allure.step('Search abra copyright text'):
            registration_page.find_abra_copyright()

        with allure.step('Search link to terms and condition page'):
            registration_page.find_terms_and_conditions_link()

        with allure.step('Search link to privacy policy'):
            registration_page.find_privacy_policy_link()
