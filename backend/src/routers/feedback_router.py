from fastapi import APIRouter, Form
from src.controllers import feedback_controller as controller

router = APIRouter()

# Get all active submissions
@router.post("/feedback")
async def get_active_submissions():
    result = await controller.get_active_submissions()
    return result


# Get selected submission
@router.post("/feedback/{submission_id}")
async def get_selected_submission(submission_id: str):
    result = await controller.get_selected_submission(submission_id)
    return result


# Register feedback
@router.post("/feedback/{submission_id}/submit")
async def register_feedback(
    submission_id: str,
    evaluation_rate: int = Form(...),
    evaluation_comment: str = Form(...),
    is_anonymous: bool = Form(...),
):
    is_registered =  await controller.register_feedback(
        evaluation_rate = evaluation_rate,
        evaluation_comment = evaluation_comment,
        submission_id = submission_id,
        user_id = "cccccccc-cccc-cccc-cccc-cccccccccccc", # tentative (Need to get user_id from cookie)
        is_anonymous = is_anonymous,
    )
    print("feedback_router.py result:", is_registered)
    return is_registered