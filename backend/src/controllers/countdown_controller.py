from fastapi import HTTPException
from src.services import project_service
from src.helpers import date_utils

async def get_project_date(project_id: str):
    try:
        # Get project information
        result = await project_service.get_project(project_id=project_id)
        # Extract project_date
        project_date = result.registerDate
        print("countdown_controller.py get_project_date project_date:", project_date)
        # Time difference (Eg. 2DAYS 23:59)
        time_diff = date_utils.format_time_diff(project_date)

        return time_diff
    except Exception as e:
        print("project_controller.py get_project_date Error:", {e})
        raise HTTPException(status_code=500, detail="Error fetching project information (Controller)")