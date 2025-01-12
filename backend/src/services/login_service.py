from fastapi import HTTPException

async def login(
    email: str,
    password: str
):
    from src.server import prisma
    try:
        result = await prisma.user.find_unique(where={
            "email": email,
            "password": password
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error with user login (Service)")
