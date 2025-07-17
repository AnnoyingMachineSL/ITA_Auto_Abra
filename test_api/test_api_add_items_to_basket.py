import json

import allure
import pytest

from models.models import ProductTypeDataModel
from utils.config import APILogin
from client.client import Client
from client.postgres_client import PostgresClient
from pprint import pprint

from utils.product_data_scripts import extract_product_styles, prepare_products_names_and_ids


@allure.title('[Positive] Add product to basket')
@pytest.mark.positive
@pytest.mark.API
class TestGetPersonalInfo:

    @allure.title('[Api test] Add products to basket of authorized user')
    @pytest.mark.positive
    @pytest.mark.API
    @pytest.mark.parametrize('login_access_token_cookie', [(APILogin.LOGIN, APILogin.PASSWORD)], indirect=True)
    @pytest.mark.parametrize('item_limit', [2])
    @allure.severity(allure.severity_level.MINOR)
    def test_api_update_personal_info(self, login_access_token_cookie, item_limit: int):
        with allure.step('Get personal token for user'):
            user_tokens, user_email = login_access_token_cookie

        with allure.step('Get products list'):
            products_list = Client().get_products_list(token=user_tokens['access_token_cookie'],
                                                       limit=item_limit, status_code=200).split('\n')[1:-2]

        with allure.step('Prepare products data'):
            products_data_model_list = []
            products_data = prepare_products_names_and_ids(products_list)

            for product_id, product_name in products_data:
                product_info = Client().get_product_info(token=user_tokens['access_token_cookie'],
                                                         product_id=product_id).json()
                product_style_ids = extract_product_styles(product_info)

                products_data_model_list.append(ProductTypeDataModel(id=product_id, name=product_name,
                                                                     variation_value_to_product_id=product_style_ids))

        with allure.step('Add product to basket'):
            for product in products_data_model_list:
                print(type(product.variation_value_to_product_id[0]))
                response = Client().add_product_to_basket(token=user_tokens['access_token_cookie'],
                                                          amount=1,
                                                          variation_value_to_product_id=
                                                          product.variation_value_to_product_id[0],
                                                          bundle_id=product.id)
