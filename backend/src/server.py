from fastapi import FastAPI
from src.routers import index_router as index
from src.routers import message_router as message
from src.routers import project_router as project
from src.routers import submission_router as submission
from src.routers import login_router as login
from src.routers import register_router as register
from src.routers import footer_router as footer
from src.middlewares import auth_middleware as auth
from src import prisma

app = FastAPI()
app.include_router(index.router)
app.include_router(message.router)
app.include_router(project.router)
app.include_router(submission.router)
app.include_router(login.router)
app.include_router(register.router)
app.include_router(footer.router)
app.include_router(auth.router)

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
