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

    async with AsyncPostgresSaver.from_conn_string(settings.database_conn_string) as checkpointer:
        await checkpointer.setup()
        app.state.agent = build_agent(checkpointer)
        yield


app = FastAPI(title="CinePulse AI", lifespan=lifespan)

app.include_router(chat_router, prefix="/api")