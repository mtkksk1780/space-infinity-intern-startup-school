from fastapi import HTTPException
from src.services import project_service, history_service

async def get_history(project_id: str):
    try:
        # Get project information
        result = await project_service.get_project(project_id = project_id)

        # Extract necessary information
        project_info = {
            "name": result.name,
            "one_liner": result.oneLiner,
            "description": result.description,
        }

        # Get submission history
        result = await history_service.get_submission_history(project_id = project_id)
        
        # Extract necessary information
        submission_history = []
        for submission in result:
            print(f"Processing Submission: {submission}")
            feedback_list = []
            for feedback in submission.Feedback:
                user_name = feedback.User.name if feedback.User and feedback.User.name else None
                feedback_list.append({
                    "user_name": user_name,
                    "evaluation_rate": feedback.evaluationRate,
                    "evaluation_comment": feedback.evaluationComment,
                    "is_anonymous": feedback.isAnonymous,
                })
            submission_history.append({
                "week": submission.week,
                "progress_comment": submission.progressComment,
                "output_url": submission.outputUrl,
                "feedback": feedback_list
            })

        # Organize the data
        data = {
            "project_info": project_info,
            "submission_history": submission_history
        }
        print("history_controller.py data:", data)
        return data
    except Exception as e:
        print("history_controller.py Error:", {e})
        raise HTTPException(status_code=500, detail="Error fetching progress history (Controller)")
