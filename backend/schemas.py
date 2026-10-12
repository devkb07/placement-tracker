from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created: str

class ApplicationCreate(BaseModel):
    company: str
    role: str
    date_applied: Optional[str] = None
    deadline: Optional[str] = None
    status: str = "Applied"
    job_url: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    created: int
    updated: int