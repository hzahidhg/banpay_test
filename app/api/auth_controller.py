from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from app.database import get_session
from app.schemas.auth import AuthUser
from app.services import user_service
from app.services import auth_service

router = APIRouter()

@router.post('/login', status_code=status.HTTP_200_OK)
def create_new_user(data: AuthUser, db_session: Session = Depends(get_session)):
    data = data.model_dump()
    user = user_service.user_by_email(data["email"], db_session)
    
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    
    is_valid_psw = auth_service.validate_password(user, data["password"])
    
    if not is_valid_psw:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized access")
    
    token = auth_service.create_auth_token({
        "id": user.id,
        "email": user.email,
        "role_id": user.role_id
    })
    
    return {
        "status_code": status.HTTP_200_OK,
        "data": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "active": user.active,
            "role_id": user.role_id,
            "role_name": user.role.name,
            "token": token
        }
    }
