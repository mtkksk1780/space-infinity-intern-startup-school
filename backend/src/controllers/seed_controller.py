from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.services import seed_service as service

async def register_seed():
    try:
        result = await service.register_seed()
        print("seed_controller.py result:", result)
        if not result:
            return JSONResponse(content={"result": False, "message": "Failed to register seed.", "data": result})
        return JSONResponse(content={"result": True, "message": "Seed registered successfully!", "data": result})
    except Exception as e:
        print("seed_controller.py" ,{e})
        return JSONResponse(content={"result": False, "message": "Failed to register seed.", "error": {e}})
