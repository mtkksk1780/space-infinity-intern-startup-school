from fastapi import APIRouter
from src.controllers import history_controller as controller

router = APIRouter()

@router.post("/history/{project_id}")
async def get_history(project_id: str):
    result = await controller.get_history(project_id = project_id)
    return result
