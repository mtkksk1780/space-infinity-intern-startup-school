from fastapi import HTTPException
from src.services import login_service as service

async def login(
    email: str,
    password: str
):
    try:
        result = await service.login(
            email=email,
            password=password
        )
        print("login_controller.py result:", result)
        if not result:
            raise HTTPException(status_code=404, detail="Error with user login (Controller)")
        # Implement authentication logic (build cookie-session)
        return True
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error with user login (Controller)")
