from fastapi import HTTPException
from src.services import submission_service, project_service
from src.helpers import date_utils

async def get_project(project_id: str):

    try:
        # Get project information
        result = await project_service.get_project(project_id=project_id)
        name = result["name"]
        one_liner = result["one_liner"]
        utc_date = result["register_date"]

        # Transform the start date to Toronto date
        toronto_date = date_utils.get_toronto_date(utc_date)
        
        # Get active week
        result = await submission_service.get_active_submission(project_id=project_id)
        if not result:
            active_week = 4
        else:
            active_week = result[0]["week"]

        # Deadline calculation
        deadline = date_utils.get_deadline(toronto_date, active_week)

        # Format the start date
        formatted_deadline = date_utils.format_date(deadline)

        # Extract necessary information
        project_info = {
            "name": name,
            "one_liner": one_liner,
            "deadline": formatted_deadline,
            "current_week": str(active_week),
        }
        print("submission_controller.py project_info:", project_info)
        return project_info
    except Exception as e:
        print("submission_controller.py Error:", {e})
        raise HTTPException(status_code=500, detail="Error fetching project information (Controller)")

async def get_submission_status(project_id: str, week: int):
    try:
        result = await submission_service.get_submission_status(project_id=project_id, week=week)
        print("submission_controller.py get_submission_status result:", result)
        return result
    except Exception as e:
        print("submission_controller.py Error:", {e})
        raise HTTPException(status_code=500, detail="Error fetching submission status (Controller)")

async def register_progress(
    project_id: str,
    progress_score: int,
    progress_comment: str,
    upload_link: str,
    submission_status: str,
):

    # Validation check
    if submission_status == "Reviewing":
        if not progress_score or not progress_comment or not upload_link:
            return {"result": False, "message": "Please fill in all fields."}

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
       
        return  {"result": True, "message": "Submission registered successfully!"}
    except Exception as e:
        print("submission_controller.py" ,{e})
        return {"result": False, "message": "Submission registration failed!"}


