import allure
import pytest

from client.client import Client
from client.client_email import EmailClient
from models.models import LoginModel, RegistrationResponseModel, ConfirmEmailResponse, \
    NegativeRegistrationResponseModel, ForgotPasswordResponse, ResetPasswordRequest, ResetPasswordNegativeResponse


@allure.title('[Positive] Reset password test')
@pytest.mark.positive
@pytest.mark.API
class TestResetPassword:
    @allure.title('[Api test] Reset forgotten password')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('registration_new_account', ['seller', 'supplier'], indirect=True)
    @pytest.mark.parametrize('new_password', ['ZXCzxc123!'])
    def test_api_reset_password(self, registration_new_account, new_password: str):
        with allure.step('Create new account'):
            random_email, random_password = registration_new_account

        with allure.step('Make response about forgot password'):
            Client().forgot_password(email=random_email, expected_model=ForgotPasswordResponse(), status_code=200)

        with allure.step('Get token for reset password'):
            forgot_password_token = EmailClient(temporary_email=random_email).get_change_password_token()

        with allure.step('Make model to reset password'):
            reset_password_request_model = ResetPasswordRequest(new_password=new_password,
                                                                confirm_password=new_password)

        with allure.step('Make request to change password'):
            Client().reset_password(token=forgot_password_token, request=reset_password_request_model,
                                    expected_model=ForgotPasswordResponse(), status_code=200)


@allure.title('[Negative] Reset password test')
@pytest.mark.negative
@pytest.mark.API
class TestResetPasswordNegative:
    @allure.title('[Api test] Reset forgotten password')
    @pytest.mark.negative
    @pytest.mark.API
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('registration_new_account', ['seller', 'supplier'], indirect=True)
    @pytest.mark.parametrize('new_password, confirm_password',
                             [('ZXCzxc123!', ''), ('', ''), ('', 'ZXCzxc123!'), ('qwe123@', 'qwe123@')])
    def test_api_reset_password_negative(self, registration_new_account, new_password: str, confirm_password: str):
        with allure.step('Create new account'):
            random_email, random_password = registration_new_account

        with allure.step('Make response about forgot password'):
            Client().forgot_password(email=random_email, expected_model=ForgotPasswordResponse(), status_code=200)

        with allure.step('Get token for reset password'):
            forgot_password_token = EmailClient(temporary_email=random_email).get_change_password_token()

        with allure.step('Make model to reset password'):
            reset_password_request_model = ResetPasswordRequest(new_password=new_password,
                                                                confirm_password=confirm_password)

        with allure.step('Make request to change password'):
            Client().reset_password(token=forgot_password_token, request=reset_password_request_model,
                                    expected_model=ResetPasswordNegativeResponse(), status_code=422)
