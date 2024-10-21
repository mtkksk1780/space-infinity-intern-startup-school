from fastapi import APIRouter
from src.controllers import message_controller as controller

router = APIRouter()


@router.get("/message")
async def get_messages(take: int = 10, offset: int = 0):
    return await controller.get_messages(take=take, offset=offset)

@router.post("/message")
async def add_message(message: str):
    return await controller.add_message(message=message)

@router.get("/message/{id}")
async def get_message(id: str):
    return await controller.get_message(id=id)
