from fastapi import HTTPException
from src import prisma


# Note: Need duplication check (projectId and week) before registering progress
async def register_progress(
    # project_name: str,
    # one_liner: str,
    # progress_score: int,
    progress_comment: str,
    upload_link: str
):
    try:
        result = await prisma.submission.create(data={
            "projectId": "b3aaa2f4-df42-4f21-bb9a-d89fb55abaa5", # tentative
            "week": 1, # tentative
            "progressRate": 10, # tentative
            "progressComment": progress_comment,
            "outputUrl": upload_link
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering progress (Service)")
