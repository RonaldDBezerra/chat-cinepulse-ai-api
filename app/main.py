from contextlib import asynccontextmanager

from fastapi import FastAPI
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

from app.api.chat import router as chat_router
from app.core.config import settings
from app.core.firebase import initialize_firebase
from app.agents.movie_agent import build_agent


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_firebase()

    if not settings.DATABASE_URL:
        raise RuntimeError("DATABASE_URL não foi configurada no ambiente")

    async with AsyncPostgresSaver.from_conn_string(settings.DATABASE_URL) as checkpointer:
        await checkpointer.setup()
        app.state.agent = build_agent(checkpointer)
        yield


app = FastAPI(title="CinePulse AI", lifespan=lifespan)

app.include_router(chat_router, prefix="/api")