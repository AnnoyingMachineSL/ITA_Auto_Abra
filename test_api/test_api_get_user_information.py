import allure
import pytest

from client.client import Client
from client.client_email import EmailClient


@allure.title('[Positive] Get user information')
@pytest.mark.positive
@pytest.mark.API
class TestGetUserInformation:

    @allure.title('[Api test] Get user information')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.MINOR)
    #@pytest.mark.parametrize('registration_new_account', ['seller', 'supplier'], indirect=True)
    def test_api_registration(self):
        # with allure.step('Create new account'):
        #     random_email, random_password = registration_new_account
        #
        # response, status_code = Client().get_user_information()
        # print(response)
        pass
