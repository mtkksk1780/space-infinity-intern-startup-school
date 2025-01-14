from fastapi import HTTPException

# Note: Need duplication check (email) before registering user information
async def signup(
    email: str,
    user_name: str,
    password: str,
    role: str
):
    from src.server import prisma
    try:
        result = await prisma.user.create(data={
            "email": email,
            "password": password,
            "name": user_name,
            "role": role,
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering user information (Service)")
