from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
class ProjectCreate(BaseModel):
    name: str

class ProjectResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class ChatRequest(BaseModel):
    project_id: int
    message: str

class ChatResponse(BaseModel):
    reply: str
