from typing import Any, cast

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel, Field
from langsmith import traceable

from app.core.auth import get_current_user

router = APIRouter()


class ChatRequest(BaseModel):
    thread_id: str = Field(..., description="Identificador único da conversa")
    message: str = Field(..., min_length=1, description="Mensagem do usuário")


@traceable(name="chat")
async def run_chat(agent, thread_id: str, message: str) -> dict:
    config = {"configurable": {"thread_id": thread_id}}

    response = await agent.ainvoke(
        cast(Any, {
            "messages": [
                {"role": "user", "content": message}
            ]
        }),
        config=cast(Any, config),
    )

    return response["structured_response"].model_dump()


@router.post("/chat")
async def chat(
    request: ChatRequest,
    fastapi_request: Request,
    user=Depends(get_current_user),
):
    agent = fastapi_request.app.state.agent

    return await run_chat(
        agent=agent,
        thread_id=request.thread_id,
        message=request.message,
    )