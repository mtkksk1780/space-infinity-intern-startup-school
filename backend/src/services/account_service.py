import os
import asyncpg
from fastapi import HTTPException

DATABASE_URL = os.getenv("DATABASE_URL")

async def get_account(
    user_id: str
):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = "SELECT * FROM app.user WHERE id = $1"
        result = await conn.fetchrow(query, user_id)
        if result is None:
            raise HTTPException(status_code = 404, detail = "User not found")
        return dict(result)
    except Exception as e:
        print({e})
        raise HTTPException(status_code = 500, detail = "Error fetching account (Service)")
    finally:
        await conn.close()


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
