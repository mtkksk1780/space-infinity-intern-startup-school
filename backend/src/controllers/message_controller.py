from fastapi import HTTPException
from src.services import message_service as service

async def get_messages(take: int = 10, offset: int = 0):
    try:
        message_count = await service.get_message_count()
        messages = await service.get_messages(take=take, offset=offset)
        return {"message_count": message_count, "messages": messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching messages")


async def add_message(message: str):
    try:
        return await service.add_message(message=message)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error adding message")


async def get_message(id: str):
    message = await service.get_message(id=id)
    if not message:
        raise HTTPException(status_code=404, detail=f"Message with id {id} not found")
    return message
