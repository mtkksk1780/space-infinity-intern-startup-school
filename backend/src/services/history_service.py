import os
import asyncpg
from fastapi import HTTPException

DATABASE_URL = os.getenv("DATABASE_URL")

async def get_submission_history(project_id: str):
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        
        # Query to fetch submission history
        query = """
            SELECT s.*, f.*, u.*
            FROM app.submission s
            LEFT JOIN app.feedback f ON s.id = f.submission_id
            LEFT JOIN app.user u ON f.user_id = u.id
            WHERE s.project_id = $1;
        """
        results = await conn.fetch(query, project_id)
        
        await conn.close()

        if not results:
            return []
        
        return [dict(result) for result in results]
    
    except Exception as e:
        print(f"Error in get_submission_history for project {project_id}: {e}")
        raise HTTPException(status_code=500, detail="Error fetching progress history (Service)")
