from fastapi import APIRouter, Form
from src.controllers import submission_controller as controller

router = APIRouter()

# Update submission records when submitting progress
@router.post("/submission/completed/{project_id}")
async def register_progress_completed(
    project_id: str,
    progress_score: int = Form(...),
    progress_comment: str = Form(...),
    upload_link: str = Form(...)
):
    submission_status = "Completed"
    is_registered =  await controller.register_progress(
        project_id = project_id,
        progress_score = progress_score,
        progress_comment = progress_comment,
        upload_link = upload_link,
        submission_status = submission_status,
    )
    print("submission_router.py completed result:", is_registered)
    return is_registered


# Update submission records when not submitting progress
@router.post("/submission/incomplete/{project_id}")
async def register_progress_incomplete(
    project_id: str,
):
    submission_status = "Incomplete"
    is_registered =  await controller.register_progress(
        project_id = project_id,
        progress_score = None,
        progress_comment = None,
        upload_link = None,
        submission_status = submission_status,
    )
    print("submission_router.py incomplete result:", is_registered)
    return is_registered