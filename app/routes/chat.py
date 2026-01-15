from fastapi import APIRouter, Depends, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.auth import get_current_user

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/", response_model=ChatResponse)
def chat(
    data: ChatRequest,
    email: str = Depends(get_current_user)
):
    # Dummy AI response
    reply = f"Hello {email}, you said: {data.message}"

    return {"reply": reply}
