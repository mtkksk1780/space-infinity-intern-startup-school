from fastapi import APIRouter, Response, Cookie
from typing import Annotated
from uuid import uuid4

router = APIRouter()

# Server-side session store
session_store = {}

def set_user_cookie(response: Response, user_id: str, role: str, user_name: str):
    # Create a unique session ID
    session_id = str(uuid4())
    # Set user data
    user_data = {
        "user_id": user_id,
        "role": role,
        "user_name": user_name
    }
    # Save user data in session store
    session_store[session_id] = user_data
    # Set session ID in cookies
    response.set_cookie(key="session_id", value=session_id, httponly=True, secure=True)
    print("auth_middleware.py set_user_cookie:", user_data)
    return {"message": "Session ID is set in cookies."}

@router.get("/get-cookie")
def get_user_cookie(session_id: str = Cookie(None)):
    # Get user data from session store
    user_data = session_store.get(session_id)
    if user_data:
        print("auth_middleware.py get_user_cookie:", user_data)
        return user_data
    else:
        return {"message": "Session ID is not found in cookies."}