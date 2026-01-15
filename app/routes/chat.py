import os
import requests
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth import get_current_user

router = APIRouter(prefix="/chat", tags=["Chat"])

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class ChatRequest(BaseModel):
    project_id: int
    message: str

@router.post("/")
def chat(req: ChatRequest, user=Depends(get_current_user)):

    if not OPENROUTER_API_KEY:
        return {"error": "OPENROUTER_API_KEY not set"}

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

    data = response.json()

    return {
        "reply": data["choices"][0]["message"]["content"]
    }
