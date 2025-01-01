from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from src.controllers import signup_controller as controller

router = APIRouter()

@router.post("/signup")
async def signup(
    email: str = Form(...),
    first_name: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    result =  await controller.signup(
        email = email,
        user_name = first_name,
        password = password,
        confirm_password = confirm_password
    )
    print("signup_router.py result:", result)

    is_registered = result["result"]
    message = result["message"]
    return JSONResponse(content={"result": is_registered, "message": message})