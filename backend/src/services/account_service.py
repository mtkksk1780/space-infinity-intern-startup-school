from fastapi import HTTPException
# from src.prisma.generated.client import Client
# from src.prisma.generated.client import Prisma

async def get_account(
    user_id: str
):
    from src.server import prisma
    # prisma = Client()
    # prisma = Prisma()
    try:
        # await prisma.connect()
        result = await prisma.user.find_unique(where = {"id": user_id})
        # await prisma.disconnect()
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code = 500, detail = "Error fetching account (Service)")


async def update_account(
    email: str,
    user_name: str,
    password: str,
    user_id: int
):
    from src.server import prisma
    try:
        result = await prisma.user.update(
            data = {
                "email": email,
                "password": password,
                "name": user_name,
            },
            where = {"id": user_id}
        )
        return result
    except Exception as e:
        print({e})
        raise HTTPException(status_code = 500, detail = "Error updating user account (Service)")
