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

        # Update the previous and next week's record
        result_update_records = await service.update_status(
            project_id = project_id,
        )
        print("submission_controller.py result_update_records:", result_update_records)
       
        return True
    except Exception as e:
        print("submission_controller.py" ,{e})
        return False


