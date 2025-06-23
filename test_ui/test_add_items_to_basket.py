import time

import allure
import pytest

from pages import main_page
from pages.login_page import LoginPage
from utils.config import AbraLoginConfig
from pages.main_page import MainPage


@allure.title('[Positive] Search and add goods to basket')
@allure.severity(allure.severity_level.CRITICAL)
class TestAddItemsToBasket:

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.smoke
    @allure.title('[UI][Positive] Search and add items')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_and_add_items_to_basket(self, login):
        main_page = MainPage(login)

        with allure.step('Click on All categories button'):
            main_page.click_on_all_categories_button()

        with allure.step('Click on Clothes button in All categories window'):
            main_page.click_on_all_categories_clothes_button()

        with allure.step('Click on Sportswear button in Clothes category'):
            main_page.click_on_all_categories_clothes_sportswear_button()

        with allure.step('Click on change location button'):
            main_page.click_on_change_location_button()
            main_page.click_on_change_location_button()

        with allure.step('Wait all items'):
            main_page.wait_items()

        first_item, second_item = main_page.get_two_random_items_from_list()
        first_item_name = main_page.get_item_name_from_item(first_item)
        second_item_name = main_page.get_item_name_from_item(second_item)

        main_page.click_on_item(first_item_name)
        main_page.click_on_item_color()
        main_page.click_on_add_to_cart_button()
        main_page.get_back()

        main_page.click_on_item(second_item_name)
        main_page.click_on_item_color()
        main_page.click_on_add_to_cart_button()
        main_page.get_back()
