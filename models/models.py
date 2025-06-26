from typing import Optional, Union
import json
from pydantic import BaseModel, Field


# Components
class NegativeLoginModelComponents(BaseModel):
    loc: Optional[list]
    msg: Optional[str]
    type: Optional[str]


class NegativeRegistrationModelSecondComponents(BaseModel):
    loc: Optional[list]
    msg: Optional[str]
    type: Optional[str]
    ctx: Optional[dict]


# Request models
class LoginModel(BaseModel):
    email: Optional[str]
    password: Optional[str]


# Response models
class LoginResponseModel(BaseModel):
    ok: Optional[bool] = True
    result: Optional[bool] = True


class LoginResponseNotVerifiedUserNegative(BaseModel):
    detail: Optional[str] = 'Wrong email or password, maybe email was not confirmed or account was deleted?'


class RegistrationResponseModel(BaseModel):
    ok: Optional[bool] = True
    result: Optional[bool] = None
    detail: Optional[dict] = {}


# Negative response models
class NegativeLoginResponseModel(BaseModel):
    # detail: Optional[list] = [NegativeLoginModelComponents]
    detail: Optional[list[NegativeLoginModelComponents]] = None


class NegativeRegistrationResponseModel(BaseModel):
    detail: Optional[list] = [NegativeLoginModelComponents, NegativeRegistrationModelSecondComponents]


# Confirm email response model
class ConfirmEmailResponse(BaseModel):
    ok: Optional[bool] = True
    result: Optional[bool] = True


class ResetPasswordRequest(BaseModel):
    new_password: Optional[str]
    confirm_password: Optional[str]


class ForgotPasswordResponse(BaseModel):
    ok: Optional[bool] = True
    result: Optional[bool] = True
    detail: Optional[str] = ''
    error: Optional[str] = ''
    error_code: Optional[int] = 0


class ResetPasswordNegativeResponse(BaseModel):
    detail: Optional[list[NegativeLoginModelComponents]] = None
