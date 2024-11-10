from fastapi import APIRouter, Form
from src.controllers import register_controller as controller

router = APIRouter()

@router.post("/register")
async def register(
    email: str = Form(...),
    user_name: str = Form(...),
    password: str = Form(...)
):
    is_registered =  await controller.register(
        email=email,
        user_name=user_name,
        password=password
    )
    print("register_router.py result:", is_registered)
    return is_registered