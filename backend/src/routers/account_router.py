from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from src.controllers import account_controller as controller

router = APIRouter()


@router.post("/account/{user_id}")
async def get_account(user_id: str):
    result = await controller.get_account(user_id = user_id)
    return result


@router.post("/account")
async def update_account(
    email: str = Form(...),
    first_name: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    user_id: str = Form(...)
):
    result =  await controller.update_account(
        email = email,
        user_name = first_name,
        update_password = password,
        confirm_password = confirm_password,
        user_id = user_id
    )
    print("account_router.py result:", result)

    is_registered = result["result"]
    message = result["message"]
    return JSONResponse(content={"result": is_registered, "message": message})