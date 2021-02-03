from fastapi import APIRouter, Body
from models.models import UserLoginSchema
from auth.auth_handler import signJWT
from app.db import get_user


router = APIRouter()


@router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    if get_user(email=user.email, password=user.password):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
