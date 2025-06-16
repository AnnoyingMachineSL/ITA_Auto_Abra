import time

import allure
import playwright
import pytest
from playwright.sync_api import sync_playwright
from client.client import Client
from client.client_email import EmailClient
from client.postgres_client import PostgresClient
from utils.config import APILogin
from models.models import LoginModel, LoginResponseModel, RegistrationResponseModel, NegativeLoginResponseModel, \
    NegativeRegistrationResponseModel, ConfirmEmailResponse, ResetPasswordRequest, ForgotPasswordResponse, \
    ResetPasswordNegativeResponse
from utils import generator
import psycopg2


@allure.title('[Positive] Api Tests')
class TestApi:

    @allure.title('[Api test] Login')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', [APILogin.LOGIN])
    @pytest.mark.parametrize('password', [APILogin.PASSWORD])
    def test_login(self, email: str, password: str):
        with allure.step(f'Create LoginModel by email:{email}'):
            login_model = LoginModel(email=email, password=password)
        with allure.step(f'Log in by models: {login_model} and {LoginResponseModel}'):
            response = Client().login(request=login_model, expected_model=LoginResponseModel())

        return response

    @allure.title('[Api test] Registration')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('user_type', ['seller', 'supplier'])
    def test_registration(self, user_type: str):
        with allure.step('Create test data to registration'):
            random_email = generator.random_temporary_email()
            random_password = generator.random_password()

        with allure.step(f'Create temporary email by email {random_email}'):
            email_client = EmailClient(temporary_email=random_email)

        with allure.step(f'Create RegistrationModel by email:{random_email} and password {random_password}'):
            registration_model = LoginModel(email=random_email, password=random_password)

        with allure.step(f'Registration by models: {registration_model} and {RegistrationResponseModel}'):
            response = Client().registration(request=registration_model, expected_model=RegistrationResponseModel(),
                                             user_type=user_type, status_code=200)
        with allure.step('Get user token'):
            token = email_client.get_registration_token()

        with allure.step('Confirm email by user token'):
            confirm_email_response = Client().confirm_email(token=token, expected_model=ConfirmEmailResponse())

        # with allure.step('Check created user on db'):
        #     PostgresClient().get_user(email=random_email.lower(), is_deleted=False, is_verified=False)
        return random_email, random_password

    @allure.title('[Api test] Reset forgotten password')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('user_type', ['seller', 'supplier'])
    @pytest.mark.parametrize('new_password', ['ZXCzxc123!'])
    def test_change_password(self, user_type: str, new_password: str):
        with allure.step('Create new account'):
            random_email, random_password = self.test_registration(user_type=user_type)

        with allure.step('Make response about forgot password'):
            forgot_password_response_model = ForgotPasswordResponse()
            forgot_password_response = Client().forgot_password(email=random_email,
                                                                expected_model=forgot_password_response_model,
                                                                status_code=200)
        with allure.step('Get token for reset password'):
            forgot_password_token = EmailClient(temporary_email=random_email).get_change_password_token()

        with allure.step('Make model to reset password'):
            reset_password_request_model = ResetPasswordRequest(new_password=new_password,
                                                                confirm_password=new_password)

        with allure.step('Make request to change password'):
            reset_password_response = Client().reset_password(token=forgot_password_token,
                                                              request=reset_password_request_model,
                                                              expected_model=ForgotPasswordResponse(),
                                                              status_code=200)
        return reset_password_response


@allure.title('[Negative] Api Tests')
class TestApiNegative:

    @allure.title('[Api test] Authorization by incorrect data')
    @pytest.mark.negative
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', ['', '!@#', '@mail.com', 'qwe@qwe'])
    @pytest.mark.parametrize('password', ['', 'a', 'zxc', '123123'])
    def test_negative_login_incorrect_data(self, email: str, password: str):
        with allure.step(f'Create LoginModel by email:{email}'):
            login_model = LoginModel(email=email, password=password)
        with allure.step(f'Log in by models: {login_model} and {NegativeLoginResponseModel}'):
            response = Client().login(request=login_model,
                                      expected_model=NegativeLoginResponseModel(),
                                      status_code=422)
        return response

    @allure.title('[Api test] Registration by incorrect data')
    @pytest.mark.negative
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', ['', '!@#', '@mail.com', 'qwe@qwe'])
    @pytest.mark.parametrize('password', ['', 'a', 'zxc', '123123'])
    @pytest.mark.parametrize('user_type', ['seller', 'supplier'])
    def test_negative_registration(self, email: str, password: str,
                                   user_type: str, status_code: int = 422):
        with allure.step(f'Create RegistrationModel by email:{email} and password {password}'):
            registration_model = LoginModel(email=email, password=password)
        with allure.step(f'Registration by models: {registration_model} and {NegativeRegistrationResponseModel}'):
            response = Client().registration(request=registration_model,
                                             expected_model=NegativeRegistrationResponseModel(),
                                             user_type=user_type, status_code=status_code)
        return response

    @allure.title('[Api test] Reset forgotten password')
    @pytest.mark.negative
    @pytest.mark.API
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('user_type', ['seller', 'supplier'])
    @pytest.mark.parametrize('new_password, confirm_password',
                             [('ZXCzxc123!', ''), ('', ''), ('', 'ZXCzxc123!'), ('qwe123@', 'qwe123@')])
    def test_change_password_negative(self, user_type: str, new_password: str, confirm_password: str):
        with allure.step('Create new account'):
            random_email, random_password = TestApi().test_registration(user_type=user_type)

        with allure.step('Make response about forgot password'):
            forgot_password_response_model = ForgotPasswordResponse()
            forgot_password_response = Client().forgot_password(email=random_email,
                                                                expected_model=forgot_password_response_model,
                                                                status_code=200)
        with allure.step('Get token for reset password'):
            forgot_password_token = EmailClient(temporary_email=random_email).get_change_password_token()

        with allure.step('Make model to reset password'):
            reset_password_request_model = ResetPasswordRequest(new_password=new_password,
                                                                confirm_password=confirm_password)

        with allure.step('Make request to change password'):
            reset_password_response = Client().reset_password(token=forgot_password_token,
                                                              request=reset_password_request_model,
                                                              expected_model=ResetPasswordNegativeResponse(),
                                                              status_code=422)
        return reset_password_response
