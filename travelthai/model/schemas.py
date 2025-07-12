from pydantic import BaseModel
from typing import Optional

class RegistrationCreate(BaseModel):
    full_name: str
    citizen_id: str
    phone: str
    target_province: str

class RegistrationRead(BaseModel):
    id: int
    user_id: int
    full_name: str
    citizen_id: str
    phone: str
    target_province: str
    class Config:
        from_attributes = True
