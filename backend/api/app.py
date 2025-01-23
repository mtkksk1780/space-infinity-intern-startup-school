import os
import uvicorn
# import subprocess
from src.server import app

# def handler(request):
#     try:
#         # Execute prisma generate
#         result = subprocess.run(
#             ["python3", "-m", "prisma", "generate"],
#             check=True,
#             capture_output=True,
#             text=True
#         )
#         print("Prisma generate result:", result.stdout)
#         return {
#             "statusCode": 200,
#             "body": f"Prisma generate completed: {result.stdout}"
#         }
#     except subprocess.CalledProcessError as e:
#         return {
#             "statusCode": 500,
#             "body": f"Error occurred: {e.stderr}"
#         }

if __name__ == '__main__':
    print("server.py is running")
    backend_host = os.getenv("BACKEND_ORIGIN", "127.0.0.2")
    print("backend_host:", backend_host) 
    uvicorn.run("src.server:app", host=backend_host, reload=True)