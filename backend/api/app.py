import os
import uvicorn
import asyncpg
import asyncio
from dotenv import load_dotenv
from src.server import app

# Load environment variables
load_dotenv()

async def execute_sql_file():
    db_url = os.getenv("DATABASE_URL")
    sql_file_path = os.path.abspath(os.path.join(os.getcwd(), "src/database.sql"))

    try:
        conn = await asyncpg.connect(db_url)
        with open(sql_file_path, "r") as file:
            sql_queries = file.read()
        await conn.execute(sql_queries)
        print("Database migration completed successfully.")
    except Exception as e:
        print(f"Database migration failed: {e}")
    finally:
        await conn.close()

async def main():
    print("Migrating database")
    await execute_sql_file()
    print("Running server.py")
    backend_host = os.getenv("BACKEND_ORIGIN", "127.0.0.1")
    print("backend_host:", backend_host) 
    uvicorn.run("src.server:app", host=backend_host, reload=True)

if __name__ == "__main__":
    asyncio.run(main())