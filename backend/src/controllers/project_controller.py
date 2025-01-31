from fastapi import HTTPException
from src.services import project_service, submission_service
from src.helpers.date_utils import get_toronto_date
from uuid import uuid4

async def register_project(
    project_name: str,
    one_liner: str,
    description: str,
    user_id: str
):

    # Validation check
    if not project_name or not one_liner or not description:
        return {"result": False, "message": "Please fill in all fields."}

    try:
        # Generate project_id using uuid
        project_id = str(uuid4())

        # Register project information to the Project table
        result_project = await project_service.register_project(
            project_id = project_id,
            project_name = project_name,
            one_liner = one_liner,
            description = description,
            user_id = user_id
        )

        print("project_controller.py result_project:", result_project)
        if not result_project:
            return {"result": False, "message": "Project registration failed!"}

        # Register submission template records to the Submission table
        result_submission = await submission_service.create_submission_template(
            project_id = project_id
        )
        print("project_controller.py result_submission:", result_submission)
        if not result_submission:
            return {"result": False, "message": "Project registration failed!"}

        return {"result": True, "message": "Project registered successfully!"}

    except Exception as e:
        print("project_controller.py" ,{e})
        return {"result": False, "message": "Project registration failed!"}


async def get_latest_project(user_id: str):
    try:
        # Get project information
        result = await project_service.get_latest_project(user_id=user_id)
        # Extract project_id
        project_id = result["id"]
        print("project_controller.py get_latest_project project_id:", project_id)
        return project_id
    except Exception as e:
        print("project_controller.py get_latest_project Error:", {e})
        raise HTTPException(status_code=500, detail="Error fetching project information (Controller)")
