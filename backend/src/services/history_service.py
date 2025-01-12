from fastapi import HTTPException

async def get_submission_history(
    project_id: str
):
    from src.server import prisma
    try:
        result = await prisma.submission.find_many(
            where = {"projectId": project_id},
            include = {
                "Project": False,
                "Feedback": {"include": {"User": True}},
            },
        )
        return result
    except Exception as e:
        print("history_service.py get_submission_history" ,{e})
        raise HTTPException(status_code = 500, detail="Error fetching progress history (Service)")


