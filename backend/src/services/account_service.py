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
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = """
            UPDATE app.user
            SET email = $1, name = $2, password = $3
            WHERE id = $4
            RETURNING id, email, name;
        """
        result = await conn.fetchrow(query, email, user_name, password, user_id)
        return dict(result)
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error updating user account (Service)")
    finally:
        await conn.close()
