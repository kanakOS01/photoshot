from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import ai, image, pack
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from backend.database import get_db

app = FastAPI()
ORIGINS = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ai.router)
app.include_router(image.router)
app.include_router(pack.router)


@app.get("/")
async def root():
    return "Hello World"


@app.get("/test-db")
async def test_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 'hello world'"))
        print(result.fetchall())
        return "success"
    except Exception as e:
        return e
    