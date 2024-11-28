from fastapi import HTTPException
from src import prisma

# Note: Need duplication check (projectId and week) before registering progress
async def register_progress(
    progress_score: int,
    progress_comment: str,
    upload_link: str
):
    try:
        result = await prisma.submission.create(data={
            "projectId": "aaa", # tentative
            "week": 4, # tentative
            "progressRate": progress_score,
            "progressComment": progress_comment,
            "outputUrl": upload_link
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering progress (Service)")
