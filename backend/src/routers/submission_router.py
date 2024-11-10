from fastapi import APIRouter, Form
from src.controllers import submission_controller as controller

router = APIRouter()

@router.post("/submission")
async def register_progress(
    # project_name: str = Form(...),
    # one_liner: str = Form(...),
    # progress_score: int = Form(...),
    progress_comment: str = Form(...),
    upload_link: str = Form(...)
):
    is_registered =  await controller.register_progress(
        # project_name=project_name,
        # one_liner=one_liner,
        # progress_score=progress_score,
        progress_comment=progress_comment,
        upload_link=upload_link
    )
    print("submission_router.py result:", is_registered)
    return is_registered