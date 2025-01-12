from fastapi import HTTPException

async def register_feedback(
    evaluation_rate: int,
    evaluation_comment: str,
    submission_id: str,
    user_id: str,
    is_anonymous: bool,
):
    from src.server import prisma
    try:
        result = await prisma.feedback.create(data={
            "evaluationRate": evaluation_rate,
            "evaluationComment": evaluation_comment,
            "submissionId": submission_id,
            "userId": user_id,
            "isAnonymous": is_anonymous
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering feedback (Service)")
