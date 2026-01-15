from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes.users import router as user_router
from app.routes.projects import router as project_router
from app.routes.chat import router as chat_router

from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later you can restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user_router)
app.include_router(project_router)
app.include_router(chat_router)



@app.get("/")
def home():
    return {"message": "Server running with user registration"}
