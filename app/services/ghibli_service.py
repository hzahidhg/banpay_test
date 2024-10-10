import requests
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

external_api_url = os.environ.get('EXTERNAL_API_URL')

def get_external_categories(role_name):
    try:
        request = requests.get(f"{external_api_url}/{role_name}")
        response = request.json()
        
        return response
    except Exception as error:
        print(error)
        raise HTTPException(500, "Internal Server Error")
