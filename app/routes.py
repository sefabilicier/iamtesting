from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from validators import is_valid_email

router = APIRouter()

class UserCreateRequest(BaseModel):
    email: str
    name: str

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
