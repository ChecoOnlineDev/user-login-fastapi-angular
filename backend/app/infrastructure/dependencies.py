from sqlalchemy.orm import Session
from fastapi import Depends
from app.infrastructure.database import get_db
from app.domain.interfaces import UserRepository
from app.infrastructure.repositories import SqlAlchemyUserRepository 

#Dependencia para obtener el repositorio de usuarios
def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return SqlAlchemyUserRepository(db)