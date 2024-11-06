from fastapi import HTTPException
from src import prisma

async def register_email(email: str):
    try:
        result = await prisma.user.create(data={
            "email": email,
            "password": None,
            "name": None,
            "role": "Guest"
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering email (Service)")
