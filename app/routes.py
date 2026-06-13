from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

router = APIRouter()

class UserCreateRequest(BaseModel):
    email: EmailStr
    name: str

@router.post("/register")
def register_user(payload: UserCreateRequest):
    return {
        "message": "User created successfully",
        "email": payload.email
    }