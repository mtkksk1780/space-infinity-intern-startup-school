from fastapi import APIRouter
from src.controllers import index_controller as controller


router = APIRouter()

router.get("/")(controller.index)

