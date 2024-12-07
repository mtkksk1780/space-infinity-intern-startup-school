from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from src.controllers import project_controller as controller

router = APIRouter()

@router.post("/project")
async def register_project(
    project_name: str = Form(...),
    one_liner: str = Form(...),
    description: str = Form(...),
):
    is_registered =  await controller.register_project(
        project_name=project_name,
        one_liner=one_liner,
        description=description,
        user_id="a" # tentative (Need to get user_id from cookie)
    )
    print("project_router.py result:", is_registered)

    if is_registered:
        message = "Project registered successfully!"
    else:
        message = "Project registration failed!"

    return JSONResponse(content={"result": is_registered, "message": message})
