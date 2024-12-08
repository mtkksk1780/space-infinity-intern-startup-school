from fastapi import APIRouter, Form, Response
from fastapi.responses import JSONResponse
from src.controllers import login_controller as controller

router = APIRouter()

@router.post("/login")
async def login(
    response: Response,
    email: str = Form(...),
    password: str = Form(...)
):
    print("login_router.py email:", email)
    is_loggedIn =  await controller.login(
        response = response,
        email = email,
        password = password,
    )
    print("login_router.py result:", is_loggedIn)
    
    if is_loggedIn:
        message = "Login successful!"
    else:
        message = "Login failed!"

    return JSONResponse(content={"result": is_loggedIn, "message": message})