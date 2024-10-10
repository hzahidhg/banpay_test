from fastapi import APIRouter
from app.api import user_controller
from app.api import auth_controller

router = APIRouter()

router.include_router(user_controller.router, prefix="/users", tags=["users"])
router.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
