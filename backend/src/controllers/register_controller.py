from fastapi import HTTPException
from src.services import register_service as service

async def register(
    email: str,
    user_name: str,
    password: str
):
    try:
        result = await service.register(
            email=email,
            user_name=user_name,
            password=password,
            role="Member"
        )
        print("register_controller.py result:", result)
        if not result:
            raise HTTPException(status_code=404, detail="Error registering user information (Controller)")
        return True
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering user information (Controller)")
