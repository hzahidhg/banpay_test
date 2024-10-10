import bcrypt
import jwt
import datetime
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

secret_key = os.environ.get('JWT_SECRET_KEY')

def validate_password(user, password):
    try:
        is_valid = bcrypt.checkpw(
            password.encode('utf-8'),
            user.password.encode('utf-8')
        )

        return is_valid
    except Exception as error:
        print(error)
        raise HTTPException(500, "Internal Server Error")

def create_auth_token(data):
    try:
        expiration = datetime.datetime.now(datetime.timezone.utc) \
            + datetime.timedelta(minutes=1440)
        print(expiration)
        payload = data.copy()
        payload.update({"exp": expiration})
        
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        
        return token
    except Exception as error:
        print(error)
        raise HTTPException(500, "Internal Server Error")