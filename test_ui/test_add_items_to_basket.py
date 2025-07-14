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
    @pytest.mark.parametrize('num_items', [3])
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_and_add_items_to_basket(self, login, num_items):
        m_page = MainPage(login)

        with allure.step('Click on All categories button'):
            m_page.click_on_all_categories_button()

        with allure.step('Click on Clothes button in All categories window'):
            m_page.click_on_all_categories_clothes_button()

        with allure.step('Click on Sportswear button in Clothes category'):
            m_page.click_on_all_categories_clothes_sportswear_button()

        with allure.step('Click on change location button'):
            m_page.click_on_change_location_button()
            m_page.click_on_change_location_button()

        with allure.step('Wait all items'):
            m_page.wait_items()

        all_items = m_page.get_all_items_op_page()
        req_items = m_page.get_the_required_number_of_items(all_items=all_items, num_items=num_items)
        item_names_list = [m_page.get_item_name_from_item(item) for item in req_items]

        with allure.step('Add items to basket'):
            for item in item_names_list:
                m_page.click_on_item(item)
                m_page.fill_item_quantity_field()
                m_page.click_on_add_to_cart_button()
                m_page.get_back()
                m_page.page_moving(y=0, x=-10000)
                m_page.wait_items()

        with allure.step('Go to basket and search items'):
            m_page.click_on_basket_button()
            m_page.reload_page()
            item_names_from_basket = m_page.get_items_names_from_basket()

        with allure.step('Compare item names from store page and basket'):
            m_page.compare_items_names(item_names_from_store_page=item_names_list,
                                       item_names_from_basket=item_names_from_basket)
        #
        # # with allure.step('Compare item count and number from item counter'):
        # #     ma_page.compare_items_count_and_item_counter(item_count=len(item_names_from_basket))
        #
        with allure.step('Delete all items from basket'):
            m_page.delete_all_item_from_basket()

        with allure.step('Search message about empty basket'):
            m_page.search_empty_basket_message()
