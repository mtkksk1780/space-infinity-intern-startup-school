from fastapi import HTTPException
from src.services import footer_service as service

async def register_email(email: str):
    try:
        result = await service.register_email(email=email)
        print("footer_controller.py result:", result)
        if not result:
            raise HTTPException(status_code=404, detail="Error registering email (Controller)")
        return "Email registered successfully"
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering email (Controller)")
