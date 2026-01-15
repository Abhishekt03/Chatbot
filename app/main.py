from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes.users import router as user_router
from app.routes.projects import router as project_router
from app.routes.chat import router as chat_router

app = FastAPI(
    title="Chatbot Platform",
    docs_url="/docs",
    redoc_url=None
)

# ✅ CORS MUST BE HERE (TOP)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://chatabhi.netlify.app",  # 👈 YOUR FRONTEND
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(user_router)
app.include_router(project_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "Backend running"}
