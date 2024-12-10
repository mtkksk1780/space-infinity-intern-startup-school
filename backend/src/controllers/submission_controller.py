from fastapi import HTTPException
from src.services import submission_service, project_service
from src.helpers import date_utils

async def get_project(project_id: str):
    try:
        # Get project information
        result = await project_service.get_project(project_id=project_id)
        utc_date = result.registerDate

        # Transform the start date to Toronto date
        toronto_date = date_utils.get_toronto_date(utc_date)
        # Format the start date
        formatted_date = date_utils.format_date(toronto_date)

        # Week calculation
        current_week = date_utils.get_week_number(utc_date)

        # Extract necessary information
        project_info = {
            "name": result.name,
            "one_liner": result.oneLiner,
            "start_date": formatted_date,
            "current_week": str(current_week),
        }
        print("submission_controller.py project_info:", project_info)
        return project_info
    except Exception as e:
        print("submission_controller.py Error:", {e})
        raise HTTPException(status_code=500, detail="Error fetching project information (Controller)")


async def register_progress(
    project_id: str,
    progress_score: int,
    progress_comment: str,
    upload_link: str,
    submission_status: str,
):
    try:
        # Update the submission record with the given projectId and active week
        result_progress = await submission_service.register_progress(
            project_id = project_id,
            progress_score = progress_score,
            progress_comment = progress_comment,
            upload_link = upload_link,
            submission_status = submission_status,
        )
        print("submission_controller.py result_progress:", result_progress)

        # Update the previous and next week's record
        result_update_records = await submission_service.update_status(
            project_id = project_id,
        )
        print("submission_controller.py result_update_records:", result_update_records)
       
        return True
    except Exception as e:
        print("submission_controller.py" ,{e})
        return False


