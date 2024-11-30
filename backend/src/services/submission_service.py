from fastapi import HTTPException
from src import prisma

# Create submission template records for 4 weeks
async def create_submission_template(
    project_id: str
):
    try:
        print("project_id:", project_id)
        templates = [
            {"projectId": project_id, "week": 1, "progressRate": None, "progressComment": None, "outputUrl": None, "isActiveWeek": True, "submissionStatus": "Pending"},
            {"projectId": project_id, "week": 2, "progressRate": None, "progressComment": None, "outputUrl": None, "isActiveWeek": False, "submissionStatus": "Pending"},
            {"projectId": project_id, "week": 3, "progressRate": None, "progressComment": None, "outputUrl": None, "isActiveWeek": False, "submissionStatus": "Pending"},
            {"projectId": project_id, "week": 4, "progressRate": None, "progressComment": None, "outputUrl": None, "isActiveWeek": False, "submissionStatus": "Pending"},
        ]
        # Insert data into the database
        result = await prisma.submission.create_many(data=templates, skip_duplicates=True)
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error creating submission template (Service)")


# Register each week's progress as completed or incomplete
# Note: Need duplication check (projectId and week) before registering progress
async def register_progress(
    project_id: str,
    progress_score: int,
    progress_comment: str,
    upload_link: str,
    submission_status: str,
):
    try:
        # Update the record with the given projectId and active week
        result = await prisma.submission.update_many(
            where={
                "projectId": project_id,
                "isActiveWeek": True,
            },
            data={
                "progressRate": progress_score,
                "progressComment": progress_comment,
                "outputUrl": upload_link,
                "isActiveWeek": False,
                "submissionStatus": submission_status,
            }
        )
        
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering progress (Service)")


# Update the next week's submission template as active
async def update_active_week(
    project_id: str
):
    try:
        # Step1: Get the next week's submission record
        next_week_submission = await prisma.submission.find_first(
            where={
                "projectId": project_id,
                "submissionStatus": "Pending",
            },
            order={
                "week": "asc"
            },
        )

        if not next_week_submission:
            return None

        # Step2: Update the next week's submission record as active
        result = await prisma.submission.update(
            where={"id": next_week_submission.id},
            data={
                "isActiveWeek": True,
            }
        )

        return result

    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error updating next week (Service)")