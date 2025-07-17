from typing import Optional, Union
import json
from pydantic import BaseModel, Field
from typing_extensions import TypedDict


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


# Get Personal Information Models

class PersonalInfoResultModel(TypedDict):
    id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    email: Optional[str]
    is_verified: Optional[bool]
    is_deleted: Optional[bool]
    is_supplier: Optional[bool]


class PersonalInfoResponseModel(BaseModel):
    ok: Optional[bool] = True
    result: Optional[dict] = PersonalInfoResultModel


class UpdatePersonalInfoRequestModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    country_id: Optional[int]
    phone_number: Optional[str]


class UpdatePersonalInfoResponseModel(BaseModel):
    ok: Optional[bool] = True
    result: Optional[bool] = True


class UpdatePersonalInformationComparingModel(BaseModel):
    is_verified: Optional[bool]
    is_deleted: Optional[bool]
    is_supplier: Optional[bool]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    country_id: Optional[int]
    phone_number: Optional[str]
    created_at: Optional[str]
    id: Optional[int]


class ChangePasswordRequestModel(BaseModel):
    old_password: Optional[str]
    new_password: Optional[str]


class ChangePasswordResponseModel(BaseModel):
    ok: Optional[bool] = True
    result: Optional[bool] = True


class ChangePasswordNegativeResponseDetail(TypedDict):
    loc: Optional[list]
    msg: Optional[str]
    type: Optional[str]
    ctx: Optional[dict]


class ChangePasswordNegativeResponse(BaseModel):
    detail: Optional[list] = ChangePasswordNegativeResponseDetail()


class CheckPasswordResponseModel(BaseModel):
    ok: Optional[bool] = True
    result: Optional[bool] = True


class CheckPasswordNegativeResponse(BaseModel):
    detail: Optional[str]


class CheckPasswordInvalidPasswordDetails(TypedDict):
    loc: Optional[list]
    msg: Optional[str]
    type: Optional[str]


class CheckPasswordInvalidPasswordResponse(BaseModel):
    detail: Optional[list] = CheckPasswordInvalidPasswordDetails()


class ProductTypeDataModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    variation_value_to_product_id: Optional[list]