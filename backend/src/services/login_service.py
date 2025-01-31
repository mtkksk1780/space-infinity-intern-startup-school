import os
import asyncpg
from fastapi import HTTPException

DATABASE_URL = os.getenv("DATABASE_URL")

async def login(
    email: str,
    password: str
):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = "SELECT * FROM app.user WHERE email = $1 AND password = $2"
        result = await conn.fetchrow(query, email, password)
        
        if result is None:
            raise HTTPException(status_code=404, detail="Invalid email or password")
        
        return dict(result)
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error with user login (Service)")
    finally:
        await conn.close()
