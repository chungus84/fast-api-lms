
from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []


# Set up user class using pydantics BaseModel to handle data validation
class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]



# Pydantic type classes for responses
@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_user(id: int):
    return {"user": users[id]}
