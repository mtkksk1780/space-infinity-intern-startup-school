from fastapi import APIRouter
from src.controllers import history_controller as controller

router = APIRouter()

@router.get("/history/{project_id}")
async def get_history(project_id: str):
    result = await controller.get_history(project_id=project_id)
    print("history_router.py result:", result)  
    return result
