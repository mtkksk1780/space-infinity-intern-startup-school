from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from src.controllers import project_controller as controller

router = APIRouter()

# Get the user's latest project information
@router.post("/project/{user_id}")
async def get_latest_project(user_id: str):
    print("project_router.py user_id:", user_id)
    result = await controller.get_latest_project(user_id = user_id)
    return result

@router.post("/project")
async def register_project(
    project_name: str = Form(...),
    one_liner: str = Form(...),
    description: str = Form(...),
    user_id: str = Form(...)
):
    result =  await controller.register_project(
        project_name = project_name,
        one_liner = one_liner,
        description = description,
        user_id = user_id
    )
    print("project_router.py result:", result)

    is_registered = result["result"]
    message = result["message"]
    return JSONResponse(content={"result": is_registered, "message": message})
