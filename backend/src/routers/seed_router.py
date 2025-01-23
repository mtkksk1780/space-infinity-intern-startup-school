from fastapi import APIRouter, Form
# from src.controllers import seed_controller as controller

router = APIRouter()

# @router.post("/seed")
# async def register_seed():
#     is_registered =  await controller.register_seed()
#     print("seed_router.py result:", is_registered)
#     return is_registered