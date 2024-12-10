from fastapi import APIRouter, Form, Response
from src.controllers import login_controller as controller

router = APIRouter()

@router.post("/login")
async def login(
    response: Response,
    email: str = Form(...),
    password: str = Form(...)
):
    return await controller.login(response=response, email=email, password=password)
