from fastapi import HTTPException
from src import prisma

# Note: Need duplication check (projectId and week) before registering user information
async def register(
    email: str,
    user_name: str,
    password: str
):
    try:
        result = await prisma.user.create(data={
            "email": email,
            "password": password,
            "name": user_name,
            "role": "Member",
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering user information (Service)")
