from fastapi import HTTPException
from src.services import feedback_service
from src.services import submission_service
# from src.helpers.date_utils import get_toronto_date

# Get all active submissions
async def get_active_submissions():
    try:
        result = await submission_service.get_active_submissions()
        print("feedback_controller.py result:", result)

        # Extract only project information
        applicable_projects = []
        for submission in result:
            applicable_projects.append({
                "submission_id": submission["id"],
                "project_name": submission.Project.name,
                "user_name": submission.Project.User.name,
            })

        print("feedback_controller.py applicable_projects:", applicable_projects)

        return applicable_projects
    except Exception as e:
        print("feedback_controller.py" ,{e})
        raise HTTPException(status_code = 500, detail="Error fetching active submissions (Controller)")


# Get selected submission
async def get_selected_submission(submission_id: str):
    try:
        result = await submission_service.get_selected_submission(submission_id = submission_id)

        # Extract necessary information
        selected_project = {
            "submission_id": result.id,
            "user_name": result.Project.User.name,
            "project_name": result.Project.name,
            "one_liner": result.Project.oneLiner,
            "note": result.progressComment,
            "submission_url": result.outputUrl,
        }

        print("feedback_controller.py selected_project:", selected_project)

        return selected_project
    except Exception as e:
        print("feedback_controller.py" ,{e})
        raise HTTPException(status_code = 500, detail="Error fetching selected submission (Controller)")


# Register feedback
async def register_feedback(
    evaluation_rate: int,
    evaluation_comment: str,
    submission_id: str,
    user_id: str,
    is_anonymous: bool,
):
    try:
        result = await feedback_service.register_feedback(
            evaluation_rate = evaluation_rate,
            evaluation_comment = evaluation_comment,
            submission_id = submission_id,
            user_id = user_id,
            is_anonymous = is_anonymous
        )
        print("feedback_controller.py result:", result)
        if not result:
            return False
        return True
    except Exception as e:
        print("feedback_controller.py" ,{e})
        return False
