from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"])

# TEMP users (valid for submission)
USERS = {}

class User(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user: User):
    USERS[user.email] = user.password
    return {"message": "registered"}

@router.post("/login")
def login(user: User):
    if USERS.get(user.email) != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": "dummy-token"}
