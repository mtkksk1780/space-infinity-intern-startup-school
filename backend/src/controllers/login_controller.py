from fastapi import HTTPException, Response
from fastapi.responses import JSONResponse
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
            return JSONResponse(content={"result": False, "message": "The email or password is incorrect."})
        
        # Set user data in cookies
        user_id = result['id']
        role = result['role']
        user_name = result['name']
        session_id = auth.set_user_cookie(response=response, user_id=user_id, role=role, user_name=user_name)

        print("login_controller.py session_id:", session_id)

        return JSONResponse(content={"result": True, "session_id": session_id, "message": "Login successful!"})
    except Exception as e:
        print("login_controller.py", {e})
        return JSONResponse(content={"result": False, "message": "Login failed!"})

