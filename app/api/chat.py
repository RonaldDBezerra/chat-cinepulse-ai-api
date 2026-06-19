from typing import Any, cast

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel, Field
from langsmith import traceable

from app.core.auth import get_current_user

router = APIRouter()


class ChatRequest(BaseModel):
    thread_id: str = Field(..., description="Identificador único da conversa (ex: id do usuário ou da sessão de chat)")
    message: str = Field(..., min_length=1, description="Mensagem do usuário")


@router.post("/chat")
@traceable(name="chat")
async def chat(
    request: ChatRequest,
    fastapi_request: Request,
    user=Depends(get_current_user),
):
    agent = fastapi_request.app.state.agent

    config = {"configurable": {"thread_id": request.thread_id}}

    response = await agent.ainvoke(
        cast(Any, {
            "messages": [
                {"role": "user", "content": request.message}
            ]
        }),
        config=cast(Any, config),
    )

    return response["structured_response"].model_dump()