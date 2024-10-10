from pydantic import BaseModel
from typing import Optional

class NewUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    role_id: int
    active: bool

class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role_id: Optional[int] = None 
    active: Optional[bool] = None
