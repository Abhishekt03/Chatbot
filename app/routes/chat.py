import os
import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.auth import get_current_user
from app.database import get_db
from app.models.chat import ChatMessage

router = APIRouter(prefix="/chat", tags=["Chat"])

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class ChatRequest(BaseModel):
    project_id: int
    message: str


@router.post("/")
def chat(
    req: ChatRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Save user message
    db.add(ChatMessage(
        project_id=req.project_id,
        user_id=user.id,
        role="user",
        content=req.message
    ))
    db.commit()

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Chatbot Platform"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "user", "content": req.message}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    reply = response.json()["choices"][0]["message"]["content"]

    # Save assistant reply
    db.add(ChatMessage(
        project_id=req.project_id,
        user_id=user.id,
        role="assistant",
        content=reply
    ))
    db.commit()

    return {"reply": reply}
