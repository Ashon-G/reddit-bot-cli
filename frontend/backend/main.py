from fastapi import FastAPI
from api.bot_controller import router as bot_router

app = FastAPI()

app.include_router(bot_router, prefix="/api")
