import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.users import Users

def create_user_database(db_session: Session, data):
    try:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(
            data["password"].encode('utf-8'),
            salt
        )

        new_user = Users(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            password=hashed_password.decode('utf-8'),
            role_id=data["role_id"],
            active=data["active"]
        )
        
        db_session.add(new_user)
        db_session.commit()
        db_session.refresh(new_user)
    except Exception as error:
        print(error)
        raise HTTPException(500, "Internal Server Error")
    
    return new_user

def list_users(db_session: Session):
    try:
        aux_users = []
        users = db_session.query(Users).all()
        
        for user in users:
            aux_users.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "role_id": user.role_id,
                "role_name": user.role.name,
                "active": user.active,
            })
        
        return aux_users
    except Exception as error:
        print(error)
        raise HTTPException(500, "Internal Server Error")
    
def user_detail(id_user, db_session: Session):
    try:
        user = db_session.query(Users).filter(
            Users.id==id_user
        ).first()
        
        return user
    except Exception as error:
        print(error)
        raise HTTPException(500, "Internal Server Error")
    
def user_update(user, data, db_session):
    try:
        for key, value in data.items():
            setattr(user, key, value)
            
        db_session.commit()
        db_session.refresh(user)
        
        return user
    except Exception as error:
        print(error)
        raise HTTPException(500, "Internal Server Error")

def user_delete(user, db_session: Session):
    try:
        db_session.delete(user)
        db_session.commit()
        
        return True
    except Exception as error:
        print(error)
        raise HTTPException(500, "Internal Server Error")
