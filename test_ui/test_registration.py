import re
import time

import allure
import pytest

from client.client import Client
from client.client_email import EmailClient
from client.postgres_client import PostgresClient
from pages.registration_page import RegistrationPage
from utils.config import AbraLoginConfig, AbraRegistrationConfig
from utils import generator
from models.models import ConfirmEmailResponse


@allure.title('[Positive] Registration Test')
@allure.severity(allure.severity_level.CRITICAL)
class TestRegistration:

    @pytest.mark.positive
    @allure.title('[UI][Positive] Registration test')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('role', ['buyer', 'seller'])
    def test_registration(self, page, role: str, email: str = None, password: str = None):
        registration_page = RegistrationPage(page)

        with allure.step('Open base url'):
            registration_page.open_page(AbraLoginConfig.BASE_PAGE_URL)

        with allure.step('Click on registration button'):
            registration_page.click_registration_button()

        with allure.step('Create test data to registration'):
            email = generator.random_temporary_email()
            password = generator.random_password()

        with allure.step(f'Create temporary email by email {email}'):
            email_client = EmailClient(temporary_email=email)

        if role == 'buyer':
            registration_page.click_be_buyer_button()
        elif role == 'seller':
            registration_page.click_be_seller_button()


        with allure.step(f'Fill login field by data: {email}'):
            registration_page.fill_login_field(email)

        with allure.step(f'Fill password field by data: {password}'):
            registration_page.fill_password_field(password)

        with allure.step('Click on create account button'):
            registration_page.click_start_buying_text()
            registration_page.click_create_account_button()

        with allure.step('Check post registration message'):
            registration_page.check_post_registration_text()

        with allure.step('Get user token'):
            token = email_client.get_registration_token()

        with allure.step('Confirm email by send user token'):
            response = Client().confirm_email(token=token, expected_model=ConfirmEmailResponse())

        # with allure.step('Check created user on db'):
        #     PostgresClient().get_user(email=email.lower(), is_deleted=False, is_verified=False)



@pytest.mark.negative
@allure.title('[UI][Negative] Registration test')
@allure.severity(allure.severity_level.NORMAL)
class TestRegistrationNegative:
    @pytest.mark.negative
    @allure.title('[UI][Negative] Registration by incorrect data')
    @pytest.mark.parametrize('role', ['buyer', 'seller'])
    @pytest.mark.parametrize('email, password', [('', 'qwe123'), ('qwe123', ''), ('@gmail.com', 'a')])
    def test_registration_incorrect_data(self, page, role: str, email: str, password: str):
        registration_page = RegistrationPage(page)

        with allure.step('Open base url'):
            registration_page.open_page(AbraLoginConfig.BASE_PAGE_URL)

        with allure.step('Click on registration button'):
            registration_page.click_registration_button()

        if role == 'buyer':
            registration_page.click_be_buyer_button()
        elif role == 'seller':
            registration_page.click_be_seller_button()

        with allure.step(f'Fill login field by data: {email}'):
            registration_page.fill_login_field(email)
            registration_page.click_start_buying_text()

        with allure.step('Check the error message for email field'):
            if len(email) == 0:
                registration_page.check_empty_email_error_message()
            else:
                registration_page.check_invalid_email_error_message()

        with allure.step(f'Fill password field by data: {password}'):
            registration_page.fill_password_field(password)
            registration_page.click_start_buying_text()

        with allure.step('Check the error message for password field'):
            if len(password) == 0:
                registration_page.check_empty_password_error_message()
            else:
                registration_page.check_invalid_password_error_message()
