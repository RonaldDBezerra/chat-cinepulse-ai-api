from fastapi import APIRouter, Depends

from pydantic import BaseModel

from app.agents.movie_agent import agent

from langsmith import traceable

from app.core.auth import get_current_user


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
@traceable(name="chat")
async def chat(
    request: ChatRequest,
    user=Depends(get_current_user)
    ):

    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message
                }
            ]
        }
    )

    return {
        "response": response["messages"][-1].content
    }