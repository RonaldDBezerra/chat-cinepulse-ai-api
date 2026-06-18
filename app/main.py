from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.core.firebase import initialize_firebase


app = FastAPI(title="CinePulse AI")

initialize_firebase()

app.include_router(chat_router, prefix="/api")