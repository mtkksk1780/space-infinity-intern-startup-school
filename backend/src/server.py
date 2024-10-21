from fastapi import FastAPI
from src.routers import index_router as index, message_router as message
from src import prisma

app = FastAPI()
app.include_router(index.router)
app.include_router(message.router)


@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()



