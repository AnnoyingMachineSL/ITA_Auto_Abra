import allure
import pytest

from client.client import Client
from client.client_email import EmailClient
from models.models import LoginModel, RegistrationResponseModel, ConfirmEmailResponse, NegativeRegistrationResponseModel
from utils import generator


@allure.title('[Positive] Registration new account')
@pytest.mark.positive
@pytest.mark.API
class TestRegistration:

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
            Client().registration(request=registration_model, expected_model=RegistrationResponseModel(),
                                  user_type=user_type, status_code=200)

        with allure.step('Get user token'):
            token = email_client.get_registration_token()

        with allure.step('Confirm email by user token'):
            Client().confirm_email(token=token, expected_model=ConfirmEmailResponse())

        # with allure.step('Check created user on db'):
        #     PostgresClient().get_user(email=random_email.lower(), is_deleted=False, is_verified=False)


@allure.title('[Negative] Registration new account')
@pytest.mark.negative
@pytest.mark.API
class TestRegistrationNegative:

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
            Client().registration(request=registration_model,
                                  expected_model=NegativeRegistrationResponseModel(),
                                  user_type=user_type, status_code=status_code)
