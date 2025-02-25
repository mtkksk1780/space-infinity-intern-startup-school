from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from src.controllers import submission_controller as controller

router = APIRouter()

# Get an applicable project information
@router.post("/submission/project/{project_id}")
async def get_project(project_id: str):
    result = await controller.get_project(project_id = project_id)
    return result


# Get an applicable project's target week status
@router.post("/submission/status/{project_id}/{week}")
async def get_active_submission(project_id: str, week: int):
    result = await controller.get_submission_status(project_id = project_id, week = week)
    return result


# Update submission records when submitting progress
@router.post("/submission/complete/{project_id}")
async def register_progress_complete(
    project_id: str,
    # progress_score: int = Form(...),
    progress_comment: str = Form(...),
    upload_link: str = Form(...)
):
    submission_status = "Reviewing"
    result =  await controller.register_progress(
        project_id = project_id,
        progress_score = 10, # Temporary value
        progress_comment = progress_comment,
        upload_link = upload_link,
        submission_status = submission_status,
    )
    print("submission_router.py completed result:", result)

    is_registered = result["result"]
    message = result["message"]
    return JSONResponse(content={"result": is_registered, "message": message})


# Update submission records when not submitting progress
@router.post("/submission/incomplete/{project_id}")
async def register_progress_incomplete(
    project_id: str,
):
    submission_status = "Incomplete"
    result =  await controller.register_progress(
        project_id = project_id,
        progress_score = 0,
        progress_comment = "None",
        upload_link = "None",
        submission_status = submission_status,
    )
    print("submission_router.py incomplete result:", result)
    
    is_registered = result["result"]
    message = result["message"]
    return JSONResponse(content={"result": is_registered, "message": message})