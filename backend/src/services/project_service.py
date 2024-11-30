from fastapi import HTTPException
from src import prisma


async def get_project(
    project_id: str
):
    try:
        result = await prisma.project.find_unique(where={"id": project_id})
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error fetching project (Service)")


async def register_project(
    project_id: str,
    project_name: str,
    one_liner: str,
    description: str,
    user_id: str
):
    try:
        result = await prisma.project.create(data={
            "id": project_id,
            "name": project_name,
            "oneLiner": one_liner,
            "description": description,
            "userId": user_id,
        })
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code=500, detail="Error registering project (Service)")
