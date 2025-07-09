import allure
import pytest

from models.models import PersonalInfoResponseModel
from utils.config import APILogin
from client.client import Client


@allure.title('[Positive] Get Personal Information about authorized user')
@pytest.mark.positive
@pytest.mark.API
class TestGetPersonalInfo:

    @allure.title('[Api test] Get personal info')
    @pytest.mark.positive
    @pytest.mark.API
    @pytest.mark.parametrize('login_access_token_cookie', [(APILogin.LOGIN, APILogin.PASSWORD)], indirect=True)
    @allure.severity(allure.severity_level.MINOR)
    def test_api_get_personal_info(self, login_access_token_cookie):
        #cookies = login_access_token_cookie
        with allure.step(f'Get personal information after log in'):
            print(Client().get_personal_info(token=login_access_token_cookie['access_token_cookie'], expected_model=PersonalInfoResponseModel()))