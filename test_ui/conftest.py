import allure
import playwright
import pytest
#
# from config import LoginPageConfig
# from pages.login_page import LoginPage
#
#
# @pytest.fixture()
# def login(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     login_page = LoginPage(page)
#     login_page.open_page()
import pytest

from client.client_email import EmailClient
from utils import generator

