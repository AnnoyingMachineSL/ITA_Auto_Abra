import allure
import playwright
import pytest

from  client.client import Client
from client.client_email import EmailClient
from models.models import ConfirmEmailResponse, RegistrationResponseModel, LoginModel
from utils import generator


@pytest.fixture
def registration_new_account(request):
    user_type = request.param
    random_email = generator.random_temporary_email()
    random_password = generator.random_password()
    email_client = EmailClient(temporary_email=random_email)
    registration_model = LoginModel(email=random_email, password=random_password)
    response = Client().registration(request=registration_model, expected_model=RegistrationResponseModel(),
                                     user_type=user_type, status_code=200)

    token = email_client.get_registration_token()
    confirm_email_response = Client().confirm_email(token=token, expected_model=ConfirmEmailResponse())
    return random_email, random_password
