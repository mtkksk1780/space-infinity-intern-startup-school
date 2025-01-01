from fastapi import HTTPException
from src.services import signup_service as service

async def register_email(email: str):
    try:
        result = await service.signup(
            email = email,
            user_name = None,
            password = None,
            role = "Guest"
        )
        print("footer_controller.py result:", result)
        if not result:
            return False
        return True
    except Exception as e:
        print("footer_controller.py", {e})
        return False
