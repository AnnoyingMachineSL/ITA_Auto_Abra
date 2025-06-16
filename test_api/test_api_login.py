import allure
import pytest
from utils.config import APILogin
from models.models import LoginModel, LoginResponseModel, NegativeLoginResponseModel
from client.client import Client


@allure.title('[Positive] Authorization test')
@pytest.mark.positive
@pytest.mark.API
class TestApiLogin:

    @allure.title('[Api test] Authorization')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', [APILogin.LOGIN])
    @pytest.mark.parametrize('password', [APILogin.PASSWORD])
    def test_login(self, email: str, password: str):
        with allure.step(f'Create LoginModel by email:{email}'):
            login_model = LoginModel(email=email, password=password)

        with allure.step(f'Log in by models: {login_model} and {LoginResponseModel}'):
            Client().login(request=login_model, expected_model=LoginResponseModel())


@allure.title('[Negative] Authorization test')
@pytest.mark.API
@pytest.mark.negative
class TestApiLoginNegative:

    @allure.title('[Api test] Authorization by incorrect data')
    @pytest.mark.negative
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', ['', '!@#', '@mail.com', 'qwe@qwe'])
    @pytest.mark.parametrize('password', ['', 'a', 'zxc', '123123'])
    def test_login_negative(self, email: str, password: str):
        with allure.step(f'Create LoginModel by email:{email}'):
            login_model = LoginModel(email=email, password=password)

        with allure.step(f'Log in by models: {login_model} and {NegativeLoginResponseModel}'):
            Client().login(request=login_model, expected_model=NegativeLoginResponseModel(), status_code=422)
