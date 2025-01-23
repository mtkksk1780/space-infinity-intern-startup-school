from fastapi import APIRouter
# from src.controllers import index_controller as controller
from src.controllers import seed_controller as controller


router = APIRouter()

# router.get("/")(controller.index)

@router.post("/")
async def register_seed():
    is_registered =  await controller.register_seed()
    print("index_router.py result:", is_registered)
    return is_registered