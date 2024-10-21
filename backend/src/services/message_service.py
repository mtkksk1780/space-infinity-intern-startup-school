from fastapi import HTTPException
from src import prisma

async def get_message_count():
    try:
        return await prisma.message.count()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching message count")


async def get_messages(take: int = 10, offset: int = 0):
    try:
        return await prisma.message.find_many(take=take, skip=offset, order={"createdAt": "desc"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching messages")


async def add_message(message: str):
    try:
        return await prisma.message.create(data={"text": message})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error adding message")


async def get_message(id: str):
    message = await prisma.message.find_unique(where={"id": id})
    if not message:
        raise HTTPException(status_code=404, detail=f"Message with id {id} not found")
    return message


