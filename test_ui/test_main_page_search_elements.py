import allure
import pytest

from pages import main_page
from pages.login_page import LoginPage
from utils.config import AbraLoginConfig
from pages.main_page import MainPage


@allure.title('[Positive] Search elements on main page')
@allure.severity(allure.severity_level.TRIVIAL)
class TestSearchLoginPageElements:

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Search elements on main page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_login_page_elements(self, login):
        main_page = MainPage(login)

        with allure.step('Search main logo'):
            main_page.search_main_logo()

        with allure.step('Search searching field'):
            main_page.search_searching_field()

        with allure.step('Search post login header actions'):
            main_page.search_login_header_actions()

        with allure.step('Search all categories button'):
            main_page.search_all_categories_button()

        with allure.step('Search last news button'):
            main_page.search_last_news_button()

        with allure.step('Search tutorial for buyers button'):
            main_page.search_tutorial_for_buyers_button()

        with allure.step('Search sell on abra button'):
            main_page.search_sell_on_abra_button()

        with allure.step('Search contact support button'):
            main_page.search_contact_support_button()

        with allure.step('Search faq button'):
            main_page.search_faq_button()

        with allure.step('Search about us button'):
            main_page.search_about_us_button()

        with allure.step('Search change language button'):
            main_page.search_change_language_button()

        with allure.step('Search change location button'):
            main_page.search_change_location_button()

        with allure.step('Search main image'):
            main_page.search_main_image()

        with allure.step('Search first block image'):
            main_page.search_first_block_image()

        with allure.step('Search second block image'):
            main_page.search_second_block_image()

        with allure.step('Search third block image'):
            main_page.search_third_block_image()

        with allure.step('Search fourth block image'):
            main_page.search_fourth_block_image()

        with allure.step('Search new arrivals button'):
            main_page.search_new_arrivals_button()

        with allure.step('Search highest rating button'):
            main_page.search_highest_rating_button()

        with allure.step('Search hot deals button'):
            main_page.search_hot_deals_button()

        with allure.step('Search clothes category block'):
            main_page.search_clothes_category_block()

        # with allure.step('Search clothes right button'):
        #     main_page.search_clothes_category_right_button()
        #
        # with allure.step('Search clothes left button'):
        #     main_page.search_clothes_category_left_button()

        # with allure.step('Search clothes view more button'):
        #     main_page.search_clothes_category_view_more_button()

        with allure.step('Search kids category block'):
            main_page.search_kids_category_block()

        # with allure.step('Search kids right button'):
        #     main_page.search_kids_category_right_button()
        #
        # with allure.step('Search kids left button'):
        #     main_page.search_kids_category_left_button()
        #
        # with allure.step('Search kids view more button'):
        #     main_page.search_kids_category_view_more_button()

        with allure.step('Search title email mailing'):
            main_page.search_title_email_mailing()

        with allure.step('Search enter email field'):
            main_page.search_enter_email_field()

        with allure.step('Search subscribe button'):
            main_page.search_subscribe_button()

        with allure.step('Search contact us title'):
            main_page.search_contact_us_title()

        with allure.step('Search phone number'):
            main_page.search_phone_number()

        with allure.step('Search social media links title'):
            main_page.search_social_media_links_title()

        with allure.step('Search telegram link'):
            main_page.search_telegram_link()

        with allure.step('Search instagram link'):
            main_page.search_instagram_link()

        with allure.step('Search vk link'):
            main_page.search_vk_link()

        with allure.step('Search google link'):
            main_page.search_google_link()

        with allure.step('Search bottom abra logo'):
            main_page.search_bottom_abra_logo()

        with allure.step('Search bottom last news button'):
            main_page.search_bottom_last_news_button()

        with allure.step('Search bottom contact support button'):
            main_page.search_bottom_contact_support_button()

        with allure.step('Search bottom tutorial for buyers button'):
            main_page.search_bottom_tutorial_for_buyers_button()

        with allure.step('Search bottom faq button'):
            main_page.search_bottom_faq_button()

        with allure.step('Search bottom sell on abra button'):
            main_page.search_bottom_sell_on_abra_button()

        with allure.step('Search bottom about us button'):
            main_page.search_bottom_about_us_button()

        with allure.step('Search bottom change language button'):
            main_page.search_bottom_change_language_button()

        with allure.step('Search bottom change location button'):
            main_page.search_bottom_change_location_button()

        with allure.step('Search abra copyright'):
            main_page.search_abra_copyright()

        with allure.step('Search terms and conditions button'):
            main_page.search_terms_and_conditions_button()

        with allure.step('Search privacy policy button'):
            main_page.search_privacy_policy_button()

        # with allure.step('Search question window'):
        #     main_page.search_question_window()
