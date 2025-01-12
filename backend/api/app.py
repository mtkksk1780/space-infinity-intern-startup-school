import os
import uvicorn
from src.server import app

if __name__ == '__main__':
    print("server.py is running")
    backend_host = os.getenv("BACKEND_ORIGIN", "127.0.0.1")
    print("backend_host:", backend_host) 
    uvicorn.run("src.server:app", host=backend_host, reload=True)