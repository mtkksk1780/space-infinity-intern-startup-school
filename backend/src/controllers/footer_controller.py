from fastapi import HTTPException
from src.services import register_service as service

async def register_email(email: str):
    try:
        result = await service.register(
            email=email,
            user_name=None,
            password=None,
            role="Guest"
        )
        print("footer_controller.py result:", result)
        if not result:
            raise HTTPException(status_code=404, detail="Error registering email (Controller)")
        return True
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering email (Controller)")
