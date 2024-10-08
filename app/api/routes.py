from fastapi import APIRouter
from app.api import controllers as user_controller

router = APIRouter()

router.include_router(user_controller.router, prefix="/users", tags=["users"])
