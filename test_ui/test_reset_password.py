import time

import allure
import pytest

from client.client import Client
from client.client_email import EmailClient
from client.postgres_client import PostgresClient
from pages.account_info_page import AccountInfoPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.forgor_password_page import ForgotPasswordPage
from pages.create_new_password_page import CreateNewPasswordPage
from utils.config import AbraLoginConfig, AbraRegistrationConfig
from utils import generator
from models.models import ConfirmEmailResponse


@allure.title('[Positive] Reset password Test')
@allure.severity(allure.severity_level.NORMAL)
class TestResetPassword:

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Reset password test')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('role', ['buyer', 'seller'])
    def test_reset_password(self, page, role: str):
        registration_page = RegistrationPage(page)
        login_page = LoginPage(page)
        forgot_password_page = ForgotPasswordPage(page)
        create_new_password_page = CreateNewPasswordPage(page)

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

        with allure.step(f'Open login page'):
            login_page.open_page(AbraLoginConfig.LOGIN_PAGE_URL)

        with allure.step('Click on forgot password button'):
            login_page.click_on_forgot_password_button()
            forgot_password_url = login_page.get_url()

        with allure.step('Open forgot password page'):
            forgot_password_page.open_page(forgot_password_url)

        with allure.step('Fill email field in forgot password page'):
            forgot_password_page.fill_forgot_password_email_field(email)

        with allure.step('Click on enter email text'):
            forgot_password_page.click_on_enter_email_text()

        with allure.step('Click on reset password button'):
            forgot_password_page.click_on_reset_password_button()

        with allure.step('Search post reset message'):
            forgot_password_page.find_post_reset_password_text()

        with allure.step('Get link for reset password'):
            reset_password_link = email_client.get_reset_password_link()

        with allure.step('Redirection to create new password page'):
            create_new_password_page.open_page(reset_password_link)

        with allure.step('Search create new password title'):
            create_new_password_page.find_create_new_password_title()

        with allure.step('Create a new password'):
            new_password = AbraLoginConfig.NEW_PASSWORD

        with allure.step(f'Fill new password field by {new_password}'):
            create_new_password_page.fill_new_password_field(new_password)

        with allure.step('Fill confirm new password field'):
            create_new_password_page.fill_confirm_password_field(new_password)

        with allure.step('Click on save button'):
            create_new_password_page.click_on_enter_new_password_text()
            create_new_password_page.click_on_save_new_password_button()

        with allure.step('Go to login page'):
            login_page.open_page(AbraLoginConfig.LOGIN_PAGE_URL)

        with allure.step('Fill login field'):
            login_page.fill_login_field(email)

        with allure.step('Fill password field by new password'):
            login_page.fill_password_field(new_password)

        with allure.step('Click on text on the page'):
            login_page.click_on_start_buying_text()

        with allure.step('Click log in button'):
            login_page.click_log_in_button()

        with allure.step('Search post login header'):
            if role == 'buyer':
                login_page.check_post_log_in_header()
            elif role == 'seller':
                login_page.search_account_info_logo()
