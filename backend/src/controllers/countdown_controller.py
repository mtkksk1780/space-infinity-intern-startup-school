import pytz
from fastapi import HTTPException
from src.services import project_service
from src.helpers import date_utils

async def get_project_countdown(project_id: str):
    try:
        # Get project information
        result = await project_service.get_project(project_id=project_id)
        # Extract project_date
        project_date = result["register_date"].replace(tzinfo=pytz.utc)

        # Get current week number
        current_week = date_utils.get_week_number(project_date)

        # Countdown (Eg. 2DAYS 23:59:59)
        countdown = date_utils.get_countdown(project_date, current_week)

        # Organize the information
        countdown_info = {
            "countdown": countdown,
            "current_week": current_week,
        }

        return countdown_info
    except Exception as e:
        print("project_controller.py get_project_date Error:", {e})
        raise HTTPException(status_code=500, detail="Error fetching project information (Controller)")