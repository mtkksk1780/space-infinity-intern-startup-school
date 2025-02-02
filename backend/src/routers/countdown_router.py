from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from src.controllers import countdown_controller as controller

router = APIRouter()

@router.post("/countdown/{project_id}")
async def get_project_countdown(project_id: str):
    result = await controller.get_project_countdown(project_id = project_id)
    return result
