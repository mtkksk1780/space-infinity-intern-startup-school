from fastapi import HTTPException
from src.services import seed_service as service

async def register_seed():
    try:
        result = await service.register_seed()
        print("seed_controller.py result:", result)
        if not result:
            return False
        return True
    except Exception as e:
        print("seed_controller.py" ,{e})
        return False
