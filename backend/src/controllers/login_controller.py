from fastapi import HTTPException, Response
from src.services import login_service as service
from src.middlewares import auth_middleware as auth

async def login(
    response: Response,
    email: str,
    password: str,
):
    try:
        result = await service.login(
            email=email,
            password=password
        )
        print("login_controller.py result:", result)
        if not result:
            raise HTTPException(status_code=404, detail="Error with user login (Controller)")
        user_id = result.id
        role = result.role
        user_name = result.name
        # Set user data in cookies
        auth.set_user_cookie(response=response, user_id=user_id, role=role, user_name=user_name)
        return True
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error with user login (Controller)")
