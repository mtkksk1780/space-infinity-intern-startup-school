import os
import asyncpg
from fastapi import HTTPException

DATABASE_URL = os.getenv("DATABASE_URL")

async def register_feedback(
    evaluation_rate: int,
    evaluation_comment: str,
    submission_id: str,
    user_id: str,
    is_anonymous: bool,
):
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        
        query = """
            INSERT INTO app.feedback (evaluation_rate, evaluation_comment, submission_id, user_id, is_anonymous)
            VALUES ($1, $2, $3, $4, $5) RETURNING *;
        """
        result = await conn.fetchrow(query, evaluation_rate, evaluation_comment, submission_id, user_id, is_anonymous)
        
        await conn.close()

        if result:
            return dict(result)

        raise HTTPException(status_code=500, detail="Error registering feedback (Service)")

    except Exception as e:
        print(f"Error in register_feedback: {e}")
        raise HTTPException(status_code=500, detail="Error registering feedback (Service)")
