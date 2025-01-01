from fastapi import HTTPException
from src.services import signup_service as service
from src.helpers import validation_utils

async def signup(
    email: str,
    user_name: str,
    password: str,
    confirm_password: str
):

    # Check if all fields are filled
    if not email or not user_name or not password or not confirm_password:
        return {"result": False, "message": "Please fill in all fields."}

    # Check if the email is valid
    email_valid = validation_utils.check_email(email)
    result = email_valid["result"]
    message = email_valid["message"]
    if not result:
        return {"result": False, "message": message}

    # Check if the password is valid
    password_valid = validation_utils.check_password(password, confirm_password)
    result = password_valid["result"]
    message = password_valid["message"]
    if not result:
        return {"result": False, "message": message}

    try:
        result = await service.signup(
            email = email,
            user_name = user_name,
            password = password,
            role = "Member"
        )
        print("signup_controller.py result:", result)
        if not result:
            return {"result": False, "message": "User registration failed!"}
        return {"result": True, "message": "User registered successfully!"}
    except Exception as e:
        print("signup_controller.py" ,{e})
        return {"result": False, "message": "This email address already exists."}
