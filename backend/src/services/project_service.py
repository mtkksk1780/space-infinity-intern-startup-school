import os
import asyncpg
from fastapi import HTTPException

DATABASE_URL = os.getenv("DATABASE_URL")

async def get_latest_project(user_id: str):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = """
            SELECT * FROM app.project
            WHERE user_id = $1
            ORDER BY register_date DESC
            LIMIT 1
        """
        result = await conn.fetchrow(query, user_id)
        if not result:
            return None
        return dict(result)
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error fetching latest project (Service)")
    finally:
        await conn.close()


async def get_project(project_id: str):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = "SELECT * FROM app.project WHERE id = $1"
        result = await conn.fetchrow(query, project_id)
        if not result:
            return None
        return dict(result)
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error fetching project (Service)")
    finally:
        await conn.close()


async def register_project(
    project_id: str,
    project_name: str,
    one_liner: str,
    description: str,
    user_id: str
):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = """
            INSERT INTO app.project (id, name, one_liner, description, user_id)
            VALUES ($1, $2, $3, $4, $5)
            RETURNING id, name, one_liner, description, user_id
        """
        result = await conn.fetchrow(query, project_id, project_name, one_liner, description, user_id)
        return dict(result)
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error registering project (Service)")
    finally:
        await conn.close()
