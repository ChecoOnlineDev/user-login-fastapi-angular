from sqlalchemy.orm import Session
from app.domain.interfaces import UserRespository
from app.domain.schemas import UserCreate, UserResponse
from app.infrastructure.models import UserModel

class SqlAlchemyUserRepository(UserRespository):
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
        #busca al usuario por email, si existe lo retorna como UserResponse, si no retorna None
    def get_user_by_email(self, email: str) -> UserResponse | None:
        user_exists = self.db_session.query(UserModel).filter(UserModel.email == email).first() #busca el usuario por email
        if user_exists:
            return UserResponse.model_validate(user_exists)
        return None
        
        #crea un nuevo usuario en la base de datos y retorna al usuario creado como UserResponse
    def create_user(self, user_create: UserCreate) -> UserResponse:
        new_user = UserModel(
            email=user_create.email,
            hashed_password=user_create.password,
            full_name = user_create.full_name,
            is_active = user_create.is_active
        )
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
            
        return UserResponse.model_validate(new_user)