from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from app.database import get_session
from app.schemas.users import NewUser, UpdateUser
from app.services import user_service
from app.services import ghibli_service

router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_new_user(data: NewUser, db_session: Session = Depends(get_session)):
    data = data.model_dump()
    user = user_service.create_user_database(db_session, data)
    
    return {
        "status_code": status.HTTP_201_CREATED,
        "data": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "active": user.active,
            "role_id": user.role_id,
            "role_name": user.role.name
        }
    }
    
@router.get('/list', status_code=status.HTTP_200_OK)
def get_users(db_session: Session = Depends(get_session)):
    users = user_service.list_users(db_session)
    
    return {
        "status_code": status.HTTP_200_OK,
        "data": users
    }

@router.get('/{id_user}/detail', status_code=status.HTTP_200_OK)
def get_users(id_user: int, db_session: Session = Depends(get_session)):
    user = user_service.user_detail(id_user, db_session)
    
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    
    return {
        "status_code": status.HTTP_200_OK,
        "data": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "active": user.active,
            "role_id": user.role_id,
            "role_name": user.role.name
        }
    }
    
@router.patch('/{id_user}/update', status_code=status.HTTP_200_OK)
def update_user(id_user: int, data: UpdateUser, db_session: Session = Depends(get_session)):
    user = user_service.user_detail(id_user, db_session)
    
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    
    clean_data = data.model_dump(exclude_unset=True)
    update_user = user_service.user_update(user, clean_data, db_session)
    
    return {
        "status_code": status.HTTP_200_OK,
        "data": {
            "id": update_user.id,
            "email": update_user.email,
            "first_name": update_user.first_name,
            "last_name": update_user.last_name,
            "active": update_user.active,
            "role_id": update_user.role_id,
            "role_name": update_user.role.name
        }
    }
    
@router.delete('/{id_user}/delete', status_code=status.HTTP_200_OK)
def delete_user(id_user: int, db_session: Session = Depends(get_session)):
    user = user_service.user_detail(id_user, db_session)
    
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    
    user_service.user_delete(user, db_session)
    
    return {
        "status_code": status.HTTP_200_OK,
    }

@router.get('/{id_user}/categories', status_code=status.HTTP_200_OK)
def get_users(id_user: int, db_session: Session = Depends(get_session)):
    user = user_service.user_detail(id_user, db_session)
    
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    
    role_name = user.role.name
    external_categories = ghibli_service.get_external_categories(role_name)
    
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
            "categories": external_categories
        }
    }