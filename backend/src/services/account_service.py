from fastapi import HTTPException
from src import prisma

async def get_account(
    user_id: str
):
    try:
        result = await prisma.user.find_unique(where = {"id": user_id})
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code = 500, detail = "Error fetching account (Service)")


async def update_account(
    email: str,
    user_name: str,
    password: str,
    user_id: int
):
    try:
        result = await prisma.user.update(
            data = {
                "email": email,
                "password": password,
                "name": user_name,
            },
            where = {"id": user_id}
        )
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code = 500, detail = "Error updating user account (Service)")
