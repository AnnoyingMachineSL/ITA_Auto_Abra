import allure
import pytest
from pages.registration_page import RegistrationPage
from utils.config import AbraRegistrationConfig, AbraLoginConfig


@allure.title('[Positive] Following links from registration page')
@allure.severity(allure.severity_level.TRIVIAL)
class TestFollowingLinksFromRegistrationPage:

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Following link to login page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_following_to_login_page(self, page):
        registration_page = RegistrationPage(page)

        with allure.step('Open registration page url'):
            registration_page.open_page(AbraRegistrationConfig.REGISTRATION_URL)

        with allure.step('Click on login page link'):
            registration_page.click_on_login_page_link()

        with allure.step('Search a correct direction'):
            registration_page.correct_direction(AbraLoginConfig.LOGIN_PAGE_URL)

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Following link to terms and conditions page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_following_to_terms_and_conditions_page(self, page):
        registration_page = RegistrationPage(page)

        with allure.step('Open registration page url'):
            registration_page.open_page(AbraRegistrationConfig.REGISTRATION_URL)

        with allure.step('Click on terms and conditions page link'):
            registration_page.click_on_terms_and_conditions_link()

        with allure.step('Search a correct direction'):
            registration_page.correct_direction(AbraRegistrationConfig.TERMS_AND_CONDITIONS_URL)

    @pytest.mark.positive
    @pytest.mark.UI
    @pytest.mark.regression
    @allure.title('[UI][Positive] Following link to privacy policy page')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_following_to_privacy_policy_page(self, page):
        registration_page = RegistrationPage(page)

        with allure.step('Open registration page url'):
            registration_page.open_page(AbraRegistrationConfig.REGISTRATION_URL)

        with allure.step('Click on privacy policy page link'):
            registration_page.click_on_privacy_policy_link()

        with allure.step('Search a correct direction'):
            registration_page.correct_direction(AbraRegistrationConfig.PRIVACY_POLICY_URL)
