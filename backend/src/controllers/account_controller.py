from fastapi import HTTPException
from src.services import account_service as service
from src.helpers import validation_utils


async def get_account(user_id: str):
    try:
        # Get user information
        result = await service.get_account(user_id = user_id)

        # Check if user exists
        if not result:
            return {"result": False, "message": "User not found."}

        # Extract necessary information
        account_info = {
            "name": result['name'],
            "email": result['email'],
            "password": result['password'],
        }

        print("account_controller.py account_info:", account_info)
        return {"result": True, "account_info": account_info}
    except Exception as e:
        print("account_controller.py Error:", {e})
        return {"result": False, "message": "Failed to get account information.", "error": {e}}


async def update_account(
    email: str,
    user_name: str,
    update_password: str,
    confirm_password: str,
    user_id: int
):

    # Check if all fields are filled
    if not email or not user_name or not update_password or not confirm_password:
        return {"result": False, "message": "Please fill in all fields."}

    # Check if the email is valid
    email_valid = validation_utils.check_email(email)
    result = email_valid["result"]
    message = email_valid["message"]
    if not result:
        return {"result": False, "message": message}

    # Check if the password is valid
    password_valid = validation_utils.check_password(update_password, confirm_password)
    result = password_valid["result"]
    message = password_valid["message"]
    if not result:
        return {"result": False, "message": message}

    try:
        result = await service.update_account(
            email = email,
            user_name = user_name,
            password = update_password,
            user_id = user_id
        )
        print("account_controller.py result:", result)
        if not result:
            return {"result": False, "message": "Account update failed!"}
        return {"result": True, "message": "Account updated successfully!"}
    except Exception as e:
        print("account_controller.py" ,{e})
        return {"result": False, "message": "Account update failed!"}
