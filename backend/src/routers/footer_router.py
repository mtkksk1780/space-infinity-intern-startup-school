from fastapi import APIRouter, Form
from src.controllers import footer_controller as controller

router = APIRouter()

@router.post("/footer")
async def register_email(email: str = Form(...)):
    is_registered = await controller.register_email(email=email)
    print("footer_router.py result:", is_registered)
    return is_registered
