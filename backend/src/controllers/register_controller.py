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
            password=password
        )
        print("register_controller.py result:", result)
        if not result:
            raise HTTPException(status_code=404, detail="Error registering user information (Controller)")
            return "Error registering user information"
        return "User registered successfully"
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering user information (Controller)")
