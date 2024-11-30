from fastapi import HTTPException
from src.services import submission_service as service

async def register_progress(
    project_id: str,
    progress_score: int,
    progress_comment: str,
    upload_link: str,
    submission_status: str,
):
    try:
        # Update the submission record with the given projectId and active week
        result_progress = await service.register_progress(
            project_id = project_id,
            progress_score = progress_score,
            progress_comment = progress_comment,
            upload_link = upload_link,
            submission_status = submission_status,
        )
        print("submission_controller.py result_progress:", result_progress)

        # Update the next week's submission record as active
        result_activation = await service.update_active_week(
            project_id = project_id,
        )
        print("submission_controller.py result_activation:", result_activation)
       
        return True
    except Exception as e:
        print("submission_controller.py" ,{e})
        return False


