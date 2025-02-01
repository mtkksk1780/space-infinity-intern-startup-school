from fastapi import APIRouter
from src.controllers import index_controller as controller
# from src.controllers import account_controller as controller


router = APIRouter()

router.get("/")(controller.index)

# @router.get("/")
# async def get_account(user_id: str = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"):
#     result = await controller.get_account(user_id = user_id)
#     return result