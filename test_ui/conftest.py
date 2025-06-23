import allure
import playwright
import pytest

from client.client import Client
from client.client_email import EmailClient
from models.models import ConfirmEmailResponse, RegistrationResponseModel, LoginModel
from pages.login_page import LoginPage
from utils import generator
from utils.config import AbraLoginConfig


@pytest.fixture
def registration_new_account(user_type: str):
    random_email = generator.random_temporary_email()
    random_password = generator.random_password()
    email_client = EmailClient(temporary_email=random_email)
    registration_model = LoginModel(email=random_email, password=random_password)
    response = Client().registration(request=registration_model, expected_model=RegistrationResponseModel(),
                                     user_type=user_type, status_code=200)

    token = email_client.get_registration_token()
    confirm_email_response = Client().confirm_email(token=token, expected_model=ConfirmEmailResponse())
    return random_email, random_password


@pytest.fixture(scope='session')
def login(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.open_page(AbraLoginConfig.BASE_PAGE_URL)
    login_page.click_login_button()
    login_page.fill_login_field(AbraLoginConfig.LOGIN)
    login_page.fill_password_field(AbraLoginConfig.PASSWORD)
    login_page.click_on_start_buying_text()
    login_page.click_log_in_button()
    return page
