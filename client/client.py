import json
from typing import Union
import allure
import requests
from models.models import LoginModel, LoginResponseModel, RegistrationResponseModel, NegativeLoginResponseModel, \
    NegativeRegistrationResponseModel, ResetPasswordRequest, ForgotPasswordResponse, ResetPasswordNegativeResponse, LoginResponseNotVerifiedUserNegative
from utils.validate_response import ValidateResponse


# from dotenv import load_dotenv


class ClientApi:
    def __init__(self):
        self.base_url = 'https://api.dev.abra-market.com'
        self.session = self._initialize_session()

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self, method: str, url: str, json=None, headers: str = None):
        response = self.session.request(method=method,
                                        url=self.base_url + url,
                                        headers=headers,
                                        json=json)
        return response


class Client(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step('POST /auth/sign-in')
    def login(self, request: LoginModel,
              expected_model: Union[LoginResponseModel, NegativeLoginResponseModel, LoginResponseNotVerifiedUserNegative],
              status_code: int = 200):
        response = self.request(method='post', url='/auth/sign-in', json=request.model_dump())
        return ValidateResponse.validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('POST /auth/sign-up/user_type')
    def registration(self, request: LoginModel,
                     expected_model: Union[RegistrationResponseModel, NegativeRegistrationResponseModel],
                     user_type: str, status_code: int = 200):
        response = self.request(method='post', url=f'/auth/sign-up/{user_type}', json=request.model_dump())
        return ValidateResponse.validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('GET /auth/sign-up/confirmEmail')
    def confirm_email(self, token: str, expected_model, status_code=200):
        response = self.request(method='get', url=f'/auth/sign-up/confirmEmail?token={token}')
        return ValidateResponse.validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('POST /users/password/forgot')
    def forgot_password(self, email: str, expected_model, status_code=200):
        response = self.request(method='post', url=f'/users/password/forgot?email={email}')
        return ValidateResponse.validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('POST /users/password/reset')
    def reset_password(self, token: str,
                       request: ResetPasswordRequest,
                       expected_model: Union[ForgotPasswordResponse, ResetPasswordNegativeResponse],
                       status_code=200):
        response = self.request(method='post', url=f'/users/password/reset?token={token}', json=request.model_dump())
        return ValidateResponse.validate_response(response=response, model=expected_model, status_code=status_code)

    # @allure.step('GET /auth/sign-in/current')
    # def get_user_information(self):
    #     response = self.request(method='get', url='/auth/sign-in/current')
    #     return response.json(), response.status_code
