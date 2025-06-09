import time

import allure
import playwright
import pytest
from playwright.sync_api import sync_playwright
from Client.client import Client
from Client.client_email import EmailClient
from Client.postgres_client import PostgresClient
from utils.config import APILogin
from models.models import LoginModel, LoginResponseModel, RegistrationResponseModel, NegativeLoginResponseModel, \
    NegativeRegistrationResponseModel, ConfirmEmailToken
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

        PostgresClient().get_user(email=email, is_deleted=False, is_verified=True)
        return response

    @allure.title('[Api test] Registration')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('user_type', ['seller', 'supplier'])
    def test_registration(self, user_type: str):
        #random_email = generator.random_email()
        random_email = generator.random_temporary_email()
        random_password = generator.random_password()

        email_client = EmailClient(temporary_email=random_email)

        with allure.step(f'Create RegistrationModel by email:{random_email} and password {random_password}'):
            registration_model = LoginModel(email=random_email, password=random_password)
        with allure.step(f'Registration by models: {registration_model} and {RegistrationResponseModel}'):
            response = Client().registration(request=registration_model, expected_model=RegistrationResponseModel(),
                                             user_type=user_type, status_code=200)
        time.sleep(5)
        token = email_client.get_registration_token()
        token_model = ConfirmEmailToken(token=token)
        print(token_model)

        _, confirm_email_status_code = Client().confirm_email(request=token_model)
        print(confirm_email_status_code)

        PostgresClient().get_user(email=random_email.lower(), is_deleted=False, is_verified=False)
        return response


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
