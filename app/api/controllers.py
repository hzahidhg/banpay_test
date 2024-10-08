from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from starlette import status
from app.database import get_session
from app.schemas.users import NewUser

router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_new_user(data: NewUser, db_session: Session = Depends(get_session)):
    print(data)
    
    return {
        "status_code": status.HTTP_201_CREATED,
        "data": {} 
    }
