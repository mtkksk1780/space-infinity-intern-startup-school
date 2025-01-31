from fastapi import APIRouter, Request, Response, Cookie, Header, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4, UUID

router = APIRouter()

# Server-side session store
session_store = {}

def set_user_cookie(response: Response, user_id: str, role: str, user_name: str):
    session_id = str(uuid4())
    user_data = {
        "user_id": user_id,
        "role": role,
        "user_name": user_name
    }
    session_store[session_id] = user_data
    response.set_cookie(
        key="session_id",
        value=session_id,
    )
    print("auth_middleware.py set_user_cookie response.headers:", response.headers)
    print("auth_middleware.py set_user_cookie session_store:", session_store)

    return session_id


@router.post("/get-user-cookie/{session_id}")
def get_user_cookie(session_id: str):
    # Get user data from session store
    user_data = session_store.get(session_id)
    if user_data:
        print("auth_middleware.py get_user_data:", user_data)
        # Convert UUID to string before sending the response
        user_data_str = {k: str(v) if isinstance(v, UUID) else v for k, v in user_data.items()}
        return JSONResponse(content={"session_id": session_id, "user_data": user_data_str, "message": "User data found in cookies."})
    else:
        return JSONResponse(content={"message": "User data not found."})
