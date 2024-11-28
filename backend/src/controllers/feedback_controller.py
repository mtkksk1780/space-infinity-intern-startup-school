from fastapi import HTTPException
from src.services import feedback_service as service
# from src.helpers.date_utils import get_toronto_date

async def register_feedback(
    evaluation_rate: int,
    evaluation_comment: str,
    submission_id: str,
    user_id: str,
    is_anonymous: bool,
):
    try:
        result = await service.register_feedback(
            evaluation_rate = evaluation_rate,
            evaluation_comment = evaluation_comment,
            submission_id = submission_id,
            user_id = user_id,
            is_anonymous = is_anonymous
        )
        print("feedback_controller.py result:", result)
        if not result:
            return False
        return True
    except Exception as e:
        print("feedback_controller.py" ,{e})
        return False
