import os
import asyncpg
from fastapi import HTTPException

DATABASE_URL = os.getenv("DATABASE_URL")

async def signup(
    email: str,
    user_name: str,
    password: str,
    role: str
):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query_check = "SELECT 1 FROM app.user WHERE email = $1"
        existing_user = await conn.fetchrow(query_check, email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        query_insert = """
            INSERT INTO app.user (email, password, name, role) 
            VALUES ($1, $2, $3, $4)
            RETURNING id, email, name, role
        """
        result = await conn.fetchrow(query_insert, email, password, user_name, role)

        return dict(result)
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering user information (Service)")
    finally:
        await conn.close()
