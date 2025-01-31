from fastapi import HTTPException
from src.services import project_service, history_service

async def get_history(project_id: str):
    try:
        # Get project information
        result = await project_service.get_project(project_id = project_id)

        # Ensure 'oneLiner' exists in the result, otherwise provide a default value
        project_info = {
            "name": result["name"],
            "one_liner": result["one_liner"],
            "description": result["description"],
        }

        # Get submission history
        result = await history_service.get_submission_history(project_id = project_id)
        
        # Extract necessary information
        submission_history = []
        for submission in result:
            print("history_controller.py submission:", submission)
            feedback_list = []
            feedback_list.append({
                "user_name": submission["name"],
                "evaluation_rate": submission["evaluation_rate"],
                "evaluation_comment": submission["evaluation_comment"],
                "is_anonymous": submission["is_anonymous"],
            })
            submission_history.append({
                "week": submission["week"],
                "progress_comment": submission["progress_comment"],
                "output_url": submission["output_url"],
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
        print("history_controller.py Error:", e) 
        raise HTTPException(status_code=500, detail="Error fetching progress history (Controller)")
