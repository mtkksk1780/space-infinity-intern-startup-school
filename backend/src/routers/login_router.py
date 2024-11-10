from fastapi import APIRouter, Form
from src.controllers import login_controller as controller

router = APIRouter()

@router.get("/login")
async def login(
    email: str = Form(...),
    password: str = Form(...)
):
    is_loggedIn =  await controller.login(
        email=email,
        password=password
    )
    print("login_router.py result:", is_loggedIn)
    return is_loggedIn