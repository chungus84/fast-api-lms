from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Ken",
        "email": "ken@test.com",
        },
    license_info={
        "name": "MIT",
    }
)

users = []


# Set up user class using pydantics BaseModel to handle data validation
class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

# Pydantic type classes for responses
@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The id of the user you want to retrive.", gt=2),
                   q: str = Query(None, max_length=5)
                   ):
    return {"user": users[id], "query": q}
