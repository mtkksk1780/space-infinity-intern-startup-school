from fastapi import HTTPException
from src import prisma

# Create submission template records for 4 weeks
async def create_submission_template(
    project_id: str
):
    try:
        print("project_id:", project_id)
        templates = [
            {"projectId": project_id, "week": 1, "progressRate": None, "progressComment": None, "outputUrl": None, "isActiveWeek": True, "submissionStatus": "Working"},
            {"projectId": project_id, "week": 2, "progressRate": None, "progressComment": None, "outputUrl": None, "isActiveWeek": False,"submissionStatus": "Pending"},
            {"projectId": project_id, "week": 3, "progressRate": None, "progressComment": None, "outputUrl": None, "isActiveWeek": False,"submissionStatus": "Pending"},
            {"projectId": project_id, "week": 4, "progressRate": None, "progressComment": None, "outputUrl": None, "isActiveWeek": False,"submissionStatus": "Pending"},
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


# Update the previous and next week's record
async def update_status(
    project_id: str
):
    try:
        # Step1: Get the next and current week's submission record
        next_week_submission = await prisma.submission.find_first(
            where={
                "projectId": project_id,
                "submissionStatus": "Pending",
            },
            order={
                "week": "asc"
            },
        )

        print("submission_service.py next_week_submission:", next_week_submission)

        if next_week_submission:
            current_week = next_week_submission.week - 1
        else:
            current_week = 4

        print("submission_service.py current_week:", current_week)

        # Step2: Update the previous week's submission status as "Completed"
        result_submission_status = await prisma.submission.update_many(
            where={
                "projectId": project_id,
                "week": current_week - 1,
                "submissionStatus": {"not": "Incomplete"},
            },
            data={
                "submissionStatus": "Completed",
            }
        )

        print("submission_service.py result_submission_status:", result_submission_status)

        # Step3: Update the next week's active week status as "True"
        result_active_week = await prisma.submission.update_many(
            where={
                "projectId": project_id,
                "week": current_week + 1,
            },
            data={
                "isActiveWeek": True,
                "submissionStatus": "Working",
            }
        )

        print("submission_service.py result_active_week:", result_active_week)

        data = {
            "result_active_week": result_active_week,
            "result_submission_status": result_submission_status,
        }

        return data

    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error updating the previous and next week's records (Service)")


# Get all active submissions
async def get_active_submissions():
    try:
        result = await prisma.submission.find_many(
            where={
                "submissionStatus": "Reviewing",
            },
            include={
                "Project": {
                    "include": {
                        "User": True,
                    },
                },
            },
        )
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code = 500, detail="Error fetching active submissions (Service)")


# Get selected submission
async def get_selected_submission(submission_id: str):
    try:
        result = await prisma.submission.find_unique(
            where={
                "id": submission_id,
            },
            include={
                "Project": {
                    "include": {
                        "User": True,
                    },
                },
            },
        )
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code = 500, detail="Error fetching selected submission (Service)")


# Get active week's submission
async def get_active_submission(project_id: str):
    try:
        result = await prisma.submission.find_many(
            where={
                "isActiveWeek": True,
                "Project": {"id": project_id},
            },
        )
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code = 500, detail="Error fetching active week's submission (Service)")
