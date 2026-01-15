from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.users import router as user_router
from app.routes.chat import router as chat_router
from app.routes.projects import router as project_router

app = FastAPI(title="Chatbot Platform")

# Serve frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# API routes
app.include_router(user_router)
app.include_router(project_router)
app.include_router(chat_router)

@app.get("/health")
def health():
    return {"status": "ok"}
