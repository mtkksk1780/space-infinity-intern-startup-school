from fastapi import HTTPException
from src.services import project_service as service

async def register_project(
    project_name: str,
    one_liner: str,
    description: str,
    user_id: str
):
    try:
        result = await service.register_project(
            project_name=project_name,
            one_liner=one_liner,
            description=description,
            user_id=user_id
        )
        print("project_controller.py result:", result)
        if not result:
            return False
        return True
    except Exception as e:
        print("project_controller.py" ,{e})
        return False
