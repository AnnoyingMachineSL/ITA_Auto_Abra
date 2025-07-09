import allure
import pytest

from client.postgres_client import PostgresClient
from models.models import PersonalInfoResponseModel, PersonalInfoResultModel
from utils.common_cheker import check_difference_between_objects
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
        with allure.step('Get personal token for user'):
            user_tokens, user_email = login_access_token_cookie

        with allure.step(f'Get personal information after log in'):
            api_response = Client().get_personal_info(token=user_tokens['access_token_cookie'],
                                                      expected_model=PersonalInfoResponseModel())

        with allure.step('Get personal information from DB'):
            database_response = PostgresClient().get_user_information(email=user_email)

        with allure.step('Prepare Data models for comparing'):
            personal_info_result = PersonalInfoResultModel(id=database_response[0][-1],
                                                           created_at=str(database_response[0][8]),
                                                           updated_at=str(database_response[0][9]),
                                                           email=database_response[0][3],
                                                           is_verified=database_response[0][0],
                                                           is_deleted=database_response[0][1],
                                                           is_supplier=database_response[0][2])

            database_data_model = PersonalInfoResponseModel(ok=True, result=personal_info_result)

            api_response.result['created_at'] = api_response.result['created_at'].replace("T", " ")
            api_response.result['updated_at'] = api_response.result['updated_at'].replace("T", " ")

        with allure.step('Check difference between models'):
            check_difference_between_objects(database_data_model, api_response)

