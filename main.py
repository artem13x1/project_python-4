from fastapi import FastAPI
from app.utils import get_users

app = FastAPI()

@app.get("/users")
async def get_users_list():
    users = get_users()
    return users
