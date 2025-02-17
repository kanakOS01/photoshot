from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import ai, image, pack

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
def root():
    return "Hello World"