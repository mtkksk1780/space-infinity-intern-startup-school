import os
import asyncpg
from fastapi import HTTPException

DATABASE_URL = os.getenv("DATABASE_URL")


# Create submission template records for 4 weeks
async def create_submission_template(project_id: str):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        print("project_id:", project_id)
        templates = [
            {"project_id": project_id, "week": 1, "progress_rate": None, "progress_comment": None, "output_url": None, "is_active_week": True, "submission_status": "Working"},
            {"project_id": project_id, "week": 2, "progress_rate": None, "progress_comment": None, "output_url": None, "is_active_week": False, "submission_status": "Pending"},
            {"project_id": project_id, "week": 3, "progress_rate": None, "progress_comment": None, "output_url": None, "is_active_week": False, "submission_status": "Pending"},
            {"project_id": project_id, "week": 4, "progress_rate": None, "progress_comment": None, "output_url": None, "is_active_week": False, "submission_status": "Pending"},
        ]
        # Insert data into the database
        query = """
            INSERT INTO app.submission (project_id, week, progress_rate, progress_comment, output_url, is_active_week, submission_status)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
        """
        for template in templates:
            await conn.execute(query, template['project_id'], template['week'], template['progress_rate'], template['progress_comment'], template['output_url'], template['is_active_week'], template['submission_status'])

        return {"message": "Submission templates created successfully"}
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error creating submission template (Service)")
    finally:
        await conn.close()


# Get submission status
async def get_submission_status(project_id: str, week: int):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = """
            SELECT submission_status FROM app.submission
            WHERE project_id = $1 AND week = $2
        """
        result = await conn.fetchrow(query, project_id, week)

        return dict(result) if result else None
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error fetching submission status (Service)")
    finally:
        await conn.close()


# Register each week's progress as completed or incomplete
async def register_progress(project_id: str, progress_score: int, progress_comment: str, upload_link: str, submission_status: str):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        # Update the record with the given projectId and active week
        query = """
            UPDATE app.submission
            SET progress_rate = $1, progress_comment = $2, output_url = $3, is_active_week = False, submission_status = $4
            WHERE project_id = $5 AND is_active_week = True
        """
        result = await conn.execute(query, progress_score, progress_comment, upload_link, submission_status, project_id)
        return {"message": f"Progress registered for project {project_id}"}
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error registering progress (Service)")
    finally:
        await conn.close()


# Update the previous and next week's record
async def update_status(project_id: str):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        # Step1: Get the next and current week's submission record
        query = """
            SELECT * FROM app.submission
            WHERE project_id = $1 AND submission_status = 'Pending'
            ORDER BY week ASC LIMIT 1
        """
        next_week_submission = await conn.fetchrow(query, project_id)

        print("submission_service.py next_week_submission:", next_week_submission)

        if next_week_submission:
            current_week = next_week_submission['week'] - 1
        else:
            current_week = 4

        print("submission_service.py current_week:", current_week)

        # Step2: Update the previous week's submission status as "Completed"
        query = """
            UPDATE app.submission
            SET submission_status = 'Completed'
            WHERE project_id = $1 AND week = $2 AND submission_status != 'Incomplete'
        """
        result_submission_status = await conn.execute(query, project_id, current_week - 1)

        print("submission_service.py result_submission_status:", result_submission_status)

        # Step3: Update the next week's active week status as "True"
        query = """
            UPDATE app.submission
            SET is_active_week = True, submission_status = 'Working'
            WHERE project_id = $1 AND week = $2
        """
        result_active_week = await conn.execute(query, project_id, current_week + 1)

        print("submission_service.py result_active_week:", result_active_week)

        data = {
            "result_active_week": result_active_week,
            "result_submission_status": result_submission_status,
        }

        return data

    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error updating the previous and next week's records (Service)")
    finally:
        await conn.close()


# Get all active submissions
async def get_active_submissions():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = """
            SELECT * FROM app.submission
            WHERE submission_status = 'Reviewing'
        """
        result = await conn.fetch(query)

        # Join Project and User data as needed (assuming you have a way to join)
        return [dict(row) for row in result]

    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error fetching active submissions (Service)")
    finally:
        await conn.close()


# Get selected submission
async def get_selected_submission(submission_id: str):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = """
            SELECT * FROM app.submission
            WHERE id = $1
        """
        result = await conn.fetchrow(query, submission_id)

        return dict(result) if result else None
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error fetching selected submission (Service)")
    finally:
        await conn.close()


# Get active week's submission
async def get_active_submission(project_id: str):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        query = """
            SELECT * FROM app.submission
            WHERE is_active_week = True AND project_id = $1
        """
        result = await conn.fetch(query, project_id)

        return [dict(row) for row in result]
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail="Error fetching active week's submission (Service)")
    finally:
        await conn.close()
