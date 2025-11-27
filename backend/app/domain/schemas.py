from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#dto base para el usuario
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True

#dto de creacion de usuario, hereda de UserBase
class UserCreate(UserBase):
    password: str

#dto de respuesta al usuario, hereda de UserBase
class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True