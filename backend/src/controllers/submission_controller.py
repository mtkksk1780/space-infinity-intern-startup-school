from fastapi import HTTPException
from src.services import submission_service as service

async def register_progress(
    progress_score: int,
    progress_comment: str,
    upload_link: str
):
    try:
        result = await service.register_progress(
            progress_score = progress_score,
            progress_comment = progress_comment,
            upload_link = upload_link
        )
        print("submission_controller.py result:", result)
        if not result:
            return False
        return True
    except Exception as e:
        print("submission_controller.py" ,{e})
        return False
