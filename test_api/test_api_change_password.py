import allure
import pytest

from models.models import ChangePasswordRequestModel, ChangePasswordResponseModel, LoginModel, \
    NegativeLoginResponseModel, LoginResponseNotVerifiedUserNegative, LoginResponseModel, ChangePasswordNegativeResponse
from utils.config import APILogin
from client.client import Client
from client.postgres_client import PostgresClient
from pprint import pprint

from utils.generator import random_password


@allure.title('[Positive] Change password after authorization')
@pytest.mark.positive
@pytest.mark.API
class TestChangePassword:

    @allure.title('[Api test] Change password')
    @pytest.mark.positive
    @pytest.mark.API
    @pytest.mark.parametrize('login_access_token_cookie', [(APILogin.LOGIN, APILogin.PASSWORD)], indirect=True)
    @pytest.mark.parametrize('new_password', [random_password() for i in range(4)])
    @allure.severity(allure.severity_level.MINOR)
    def test_api_change_password(self, login_access_token_cookie, new_password):
        with allure.step('Get personal token for user'):
            user_tokens, user_email = login_access_token_cookie

        with allure.step('Prepare data model to change password'):
            request_model = ChangePasswordRequestModel(old_password=APILogin.PASSWORD,
                                                       new_password=new_password)

        with allure.step(f'Change password by new password: {new_password}'):
            Client().change_password(token=user_tokens['access_token_cookie'],
                                     request=request_model,
                                     expected_model=ChangePasswordResponseModel())

        with allure.step('Prepare login data model using old data'):
            old_authorization_data = LoginModel(email=APILogin.LOGIN,
                                                password=APILogin.PASSWORD)

        with allure.step('Try to authorization using old password'):
            Client().login(request=old_authorization_data, expected_model=LoginResponseNotVerifiedUserNegative(),
                           status_code=403)

        with allure.step('Prepare login data model using new data'):
            new_authorization_data = LoginModel(email=APILogin.LOGIN,
                                                password=new_password)

        with allure.step('Try to authorization using new password'):
            Client().login(request=new_authorization_data, expected_model=LoginResponseModel(),
                           status_code=200)

        with allure.step('Get back to old password'):
            request_model = ChangePasswordRequestModel(old_password=new_password,
                                                       new_password=APILogin.PASSWORD)

            Client().change_password(token=user_tokens['access_token_cookie'],
                                     request=request_model,
                                     expected_model=ChangePasswordResponseModel())


@allure.title('[Negative] Change password after authorization')
@pytest.mark.negative
@pytest.mark.API
class TestChangePasswordNegative:
    @allure.title('[Api test] Change password negative')
    @pytest.mark.positive
    @pytest.mark.API
    @pytest.mark.parametrize('login_access_token_cookie', [(APILogin.LOGIN, APILogin.PASSWORD)], indirect=True)
    @pytest.mark.parametrize('new_password', ['', '123', 'qwe', 'QWEqwe123'])
    @allure.severity(allure.severity_level.MINOR)
    def test_api_negative_change_password(self, login_access_token_cookie, new_password):
        with allure.step('Get personal token for user'):
            user_tokens, user_email = login_access_token_cookie

        with allure.step('Prepare data model to change password'):
            request_model = ChangePasswordRequestModel(old_password=APILogin.PASSWORD,
                                                       new_password=new_password)

        with allure.step(f'Try to change password by uncorrected password: {new_password}'):
            Client().change_password(token=user_tokens['access_token_cookie'],
                                     request=request_model,
                                     expected_model=ChangePasswordNegativeResponse(),
                                     status_code=422)

        with allure.step('Try to authorization using uncorrected password'):
            uncorrected_authorization_data = LoginModel(email=APILogin.LOGIN,
                                                        password=new_password)
            Client().login(request=uncorrected_authorization_data,
                           expected_model=LoginResponseNotVerifiedUserNegative(),
                           status_code=403)
