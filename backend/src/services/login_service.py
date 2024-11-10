from fastapi import HTTPException
from src import prisma

async def login(
    email: str,
    password: str
):
    try:
        result = await prisma.user.find_unique(where={
            "email": email,
            "password": password
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error with user login (Service)")
