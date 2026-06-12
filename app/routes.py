from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re

router = APIRouter()

class UserCreateRequest(BaseModel):
    email: str
    name: str

def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

@router.post("/register")
def register_user(payload: UserCreateRequest):
    if not is_valid_email(payload.email):
        raise HTTPException(
            status_code=400,
            detail="Invalid email format"
        )
    return {
        "message": "User created successfully",
        "email": payload.email
    }