import sys
import os
from dotenv import load_dotenv
from pathlib import Path
from fastapi import FastAPI, Request, Response, HTTPException, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from src.routers import index_router as index
from src.routers import project_router as project
from src.routers import submission_router as submission
from src.routers import feedback_router as feedback
from src.routers import history_router as history
from src.routers import countdown_router as countdown
from src.routers import login_router as login
from src.routers import signup_router as signup
from src.routers import account_router as account
from src.routers import footer_router as footer
from src.routers import seed_router as seed
from src.middlewares import auth_middleware as auth
# from src.prisma.generated.client import Prisma
from src.prisma.generated.client import *

load_dotenv()
app = FastAPI()

# Prisma settings
# BASE_DIR = Path(__file__).resolve().parent
# CLIENT_PATH = BASE_DIR / "src/prisma/generated"
prisma = Client()

@app.on_event("startup")
async def startup():
    try:
        await prisma.connect()
        print("✅ Connected to the Prisma database")
    except Exception as e:
        print(f"❌ Failed to connect to the Prisma database: {e}")

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


# CORS settings
origins = [
    "http://0.0.0.0:5001",  # Local environment
    "http://localhost:5001",  # Local environment (localhost)
    "https://space-infinity-intern-startup-school.vercel.app",  # Production environment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


# Include routers
app.include_router(index.router)
app.include_router(project.router)
app.include_router(submission.router)
app.include_router(feedback.router)
app.include_router(history.router)
app.include_router(countdown.router)
app.include_router(login.router)
app.include_router(signup.router)
app.include_router(account.router)
app.include_router(footer.router)
app.include_router(seed.router)
app.include_router(auth.router)
