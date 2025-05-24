from pydantic import BaseModel
from typing import Optional, Union

class UserModel(BaseModel):
    email: Optional[str] = None
    is_deleted: Optional[bool] = None
    is_verified: Optional[bool] = None