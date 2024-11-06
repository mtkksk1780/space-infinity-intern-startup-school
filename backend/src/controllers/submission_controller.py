from fastapi import HTTPException
from src.services import submission_service as service

async def register_progress(
    # project_name: str,
    # one_liner: str,
    # progress_score: int,
    progress_comment: str,
    upload_link: str
):
    try:
        result = await service.register_progress(
            # project_name=project_name,
            # one_liner=one_liner,
            # progress_score=progress_score,
            progress_comment=progress_comment,
            upload_link=upload_link
        )
        print("submission_controller.py result:", result)
        if not result:
            raise HTTPException(status_code=404, detail="Error registering progress (Controller)")
        return "Progress registered successfully"
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering progress (Controller)")
