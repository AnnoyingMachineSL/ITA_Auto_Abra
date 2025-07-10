import allure
import pytest

from client.postgres_client import PostgresClient
from models.models import UpdatePersonalInfoRequestModel, UpdatePersonalInfoResponseModel, \
    UpdatePersonalInformationComparingModel
from utils.common_cheker import check_difference_between_objects
from utils.config import APILogin
from client.client import Client
from client.postgres_client import PostgresClient
from pprint import pprint


@allure.title('[Positive] Get Personal Information about authorized user')
@pytest.mark.positive
@pytest.mark.API
class TestGetPersonalInfo:

    @allure.title('[Api test] Update personal info')
    @pytest.mark.positive
    @pytest.mark.API
    @pytest.mark.parametrize('login_access_token_cookie', [(APILogin.LOGIN, APILogin.PASSWORD)], indirect=True)
    @pytest.mark.parametrize('country_id', [id[0] for id in PostgresClient().get_countries_id()])
    @pytest.mark.parametrize('first_name, last_name, phone_number', [('', '', ''), ('qwe', 'qwe', 'qwe'),('Tom', 'Hanks','123123123')])
    @allure.severity(allure.severity_level.MINOR)
    def test_api_update_personal_info(self, login_access_token_cookie, country_id: int, first_name: str,
                                      last_name: str, phone_number: str):
        with allure.step('Get personal token for user'):
            user_tokens, user_email = login_access_token_cookie

        with allure.step('Get personal information before updating'):
            personal_information_before_update = PostgresClient().get_user_information(email=user_email)

        with allure.step('Prepare data model'):
            request_model = UpdatePersonalInfoRequestModel(first_name=first_name,
                                                           last_name=last_name,
                                                           country_id=country_id,
                                                           phone_number=phone_number)

        with allure.step('Update personal info'):
            Client().update_personal_info(token=user_tokens['access_token_cookie'],
                                          request=request_model,
                                          expected_model=UpdatePersonalInfoResponseModel(),
                                          status_code=200)

        with allure.step('Prepare comparing models'):
            expected_user_information = UpdatePersonalInformationComparingModel(
                                                                                is_verified=personal_information_before_update[0][0],
                                                                                is_deleted=personal_information_before_update[0][1],
                                                                                is_supplier=personal_information_before_update[0][2],
                                                                                email=user_email,
                                                                                first_name=first_name,
                                                                                last_name=last_name,
                                                                                country_id=country_id,
                                                                                phone_number=phone_number,
                                                                                created_at=str(personal_information_before_update[0][8]),
                                                                                id=personal_information_before_update[0][-1])

            new_user_information_from_database = PostgresClient().get_user_information(email=user_email)

            actual_user_information = UpdatePersonalInformationComparingModel(
                                                                                is_verified=new_user_information_from_database[0][0],
                                                                                is_deleted=new_user_information_from_database[0][1],
                                                                                is_supplier=new_user_information_from_database[0][2],
                                                                                email=new_user_information_from_database[0][3],
                                                                                first_name=new_user_information_from_database[0][4],
                                                                                last_name=new_user_information_from_database[0][5],
                                                                                country_id=new_user_information_from_database[0][6],
                                                                                phone_number=new_user_information_from_database[0][7],
                                                                                created_at=str(new_user_information_from_database[0][8]),
                                                                                id=new_user_information_from_database[0][10])

            with allure.step('Check difference between models'):
                check_difference_between_objects(expected_user_information, actual_user_information)
