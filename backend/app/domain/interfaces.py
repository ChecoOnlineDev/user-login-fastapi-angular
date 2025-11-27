from abc import ABC, abstractmethod
from typing import Optional
from app.domain.schemas import UserCreate, UserResponse

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserResponse]:
        pass
    
    @abstractmethod
    def create_user(self, user: UserCreate) -> UserResponse:
        pass